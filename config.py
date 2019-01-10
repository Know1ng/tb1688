KEYWORD = '裤子' # 搜索商品的关键字
MONGO_URI = 'localhost'
MONGO_DB = 'tb_1688'
MONGO_TABLE = KEYWORD # 以搜索关键词为表名


COOKIE = 'hng=CN%7Czh-CN%7CCNY%7C156; cna=AxdKEs8m2RACAduGcv5qQ+6P; lid=lydxy8712595; ali_ab=112.94.190.68.1541738239945.7; UM_distinctid=167973c6c0421-0933721fc41371-3f674706-e1000-167973c6c05120; cookie2=1c09e08d0a833d700ad885a8f7ed2af4; t=7a35e71798c14cce9578dc27c01de3e0; _tb_token_=e8ebdeef63487; csg=6817fd56; ali_apache_track=c_mid=b2b-1982205558|c_lid=lydxy8712595|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; last_mid=b2b-1982205558; _csrf_token=1546940566457; __rn_alert__=false; _m_h5_tk=55aacf07e73e663cd842896ee1394c81_1546951845061; _m_h5_tk_enc=69232611cfad80853509ab12d3582c2f; _is_show_loginId_change_block_=b2b-1982205558_false; _show_force_unbind_div_=b2b-1982205558_false; _show_sys_unbind_div_=b2b-1982205558_false; _show_user_unbind_div_=b2b-1982205558_false; __cn_logon__=false; h_keys="%u7537%u88c5#%u94c5%u7b14#2b%u94c5%u7b14#%u7535%u8111#%u5973%u88c5#%u9422%u75af%ue5ca#%u82f9%u679c%u7535%u8111#%u9996%u8111"; alicnweb=touch_tb_at%3D1546957799904%7ChomeIdttS%3D02311510086060039350646378218473773050%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3Dlydxy8712595; ad_prefer="2019/01/08 22:31:03"; JSESSIONID=02A3D63FA0C66C4C92F5CFA545869319; l=aBtooWOxyYLmTq9pkMaTBSHDg707ADZPe51y1Mam2TEhNn5aDjCL1z8b-VwRj_qC5BGy_K-59; isg=BAcHbUCSF6qRX5MWB7euHJX8lrsRpMQsWmgW9dn0GBbhSCcK4d9CPg1O7kizpLNm'
USER_AGENT = [
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
]

# 每页全部同步请求数
# MAX_SYNCREQ = 6 # 改参数请求的商品产生重复，未解决

# 最大页数,可自定义
MAX_PAGE = 100
