import random
import re
import time
import pymongo
import requests
from urllib.parse import quote
from multiprocessing import Pool
from config import *

'''
爬取淘宝1688商品信息，运行前请先打开代理
'''


client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
item_id = set()



def get_proxy():
    '''
    获取代理
    '''
    return requests.get("http://127.0.0.1:5010/get/").text


def get_one_page(page):
    '''
    得到单页商品信息
    '''
    try:
        print('正在爬取第%d页' % page)
        # for syncreq in range(1, MAX_SYNCREQ + 1):
        proxy = get_proxy()
        url = 'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json'
        data = {
            'beginpage': str(page),  # 页数
            'syncreq': '1',  # 同步请求参数  str(syncreq)
            'keywords': KEYWORD  # 搜索关键词
        }
        headers = {
            'User_Agent': random.choice(USER_AGENT),
            'Referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?keywords=' + quote(
                KEYWORD) + '&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA',
            'Cookie': COOKIE,
        }
        proxies = {"http": "http://{}".format(proxy)}
        response = requests.get(url=url, headers=headers, params=data, proxies=proxies, timeout=5)
        time.sleep(1)
        if response.status_code == 200:
            data = response.json()
            get_info(data=data)
    except Exception:
        print('出现异常，重新爬取第%d页' % page)
        return get_one_page(page)


def get_info(data):
    '''
    得到并保存商品信息
    '''
    try:
        print('正在获取商品信息..')
        items = data['data']['content']['offerResult']
        # item为每一个商品
        for item in items:
            param1 = item['attr']['company']
            company = param1['name']
            type = param1['bizTypeName']
            city = param1['city']
            province = param1['province']
            param2 = item['attr']['tradePrice']['offerPrice']
            originalValue = param2['originalValue']['integer'] + param2['originalValue']['decimals'] / 10
            quantityPrices = param2['value']['integer'] + param2['value']['decimals'] / 10
            param3 = item['attr']['tradeQuantity']
            sales = param3['number']
            saleType = param3['sortType']
            detailUrl = item['eurl']
            imgUrl = item['imgUrl']
            originaltitle = item['title']
            title = re.sub('<.*>', '', originaltitle)
            result = {
                '标题': title,
                '原价': originalValue,
                '最低批发价': quantityPrices,
                '销售量': sales,
                '销售形式': saleType,
                '详细链接': detailUrl,
                '图片链接': imgUrl,
                '公司': company,
                '公司类型': type,
                '城市': city,
                '省份': province,
            }
            save_to_mongo(result=result)
    except TypeError:
        pass


def save_to_mongo(result):
    '''
    信息保存至mongoDB
    '''
    # 去除标题相同的商品
    if result['标题'] in item_id:
        print('发现重复item，丢弃--->%s<---' % result['标题'])
    else:
        item_id.add(result['标题'])
        if db[MONGO_TABLE].insert(result):
            print('成功保存至mongoDB', result['标题'])



def main(page):
    get_one_page(page)
    print('有效商品数为%d'%len(item_id))  # 打印有效商品数量


if __name__ == '__main__':
    page = [x for x in range(1, MAX_PAGE + 1)]
    # 多进程
    pool = Pool()
    pool.map(main, page)


# todo 待解决问题：
'''
关于遍历syncreq获取单页更多信息，每页的第一个请求正常，
后续获得商品重复，怀疑与请求头里面的一些参数有关，若无
法分析参数规律，该爬虫只可扩大MAX_PAGE获得更多采集量。
或者换用selenium的方式来爬取。
2019.1.10
'''
