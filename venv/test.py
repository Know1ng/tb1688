import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").text

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

import random
import re
import time

import pymongo
import requests
from config import *
from urllib.parse import quote

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
item_id = set()

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").text

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

def getHtml():
    # 重试次数
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('http://httpbin.org/get', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
def get_one_page(page):
    try:
        print('正在爬取第%d页' % page)
        for syncreq in range(1, MAX_SYNCREQ + 1):

            url = 'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json'
            data = {
                'beginpage': str(page),  # 页数，可变
                'syncreq': str(syncreq),  # 同步请求数，可变
                'keywords': KEYWORD  # 关键词，可变
            }
            headers = {

                'User_Agent': random.choice(USER_AGENT),
                'Referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?keywords=' + quote(KEYWORD) +'&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA',
                'Cookie': COOKIE,

            }

            response = requests.get(url=url, headers=headers, params=data,timeout=5 )
            time.sleep(3)
            if response.status_code == 200:
                data = response.json()
                print(response.url)
                get_info(data=data)


    except TimeoutError:
        print('请求超时，重新发起请求..')
        get_one_page()


def get_info(data):
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
            # print(result)
            save_to_mongo(result=result)
    except TypeError:
        pass


def find_max_page():
    pass


def save_to_mongo(result):
    try:
        # 去除标题相同的商品
        if result:
            if result['标题'] in item_id:
                print('发现重复item，丢弃--->%s<---' % result['标题'])
            else:
                item_id.add(result['标题'])
                if db[MONGO_TABLE].insert(result):
                    print('保存成功', result['标题'])
    except pymongo.errors.InvalidOperation:
        pass


def main():
    # for page in range(1, MAX_PAGE + 1):
    page = 1
    get_one_page(page)


if __name__ == '__main__':
    main()

# def getHtml():
#     proxy = get_proxy()
#     html = requests.get('http://httpbin.org/get', proxies={"http": "http://{}".format(proxy)})
#     print(html.text)

getHtml()