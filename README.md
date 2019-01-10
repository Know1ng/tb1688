# tb1688

淘宝1688采购批发网站https://www.1688.com/
爬虫，爬取商品原价以及批发价格等相关信息。

1、爬虫涉及：

requests请求，随机UA，随机代理ip，cookie登陆，多进程爬取，xpath解析，保存至mongoDB。

2、关于代理

网上很多免费的代理都不太稳定，付费又觉得没有必要，这里使用的是别人维护好了代理池，感觉还是比较好用的。


3、运行

运行爬虫程序之前，先要运行proxy_pool-master路径下的代理，运行方法可以参考文件里面的readme文档，或者访问https://github.com/jhao104/proxy_pool
；代理运行好之后再打开config.py文件，赋值KEYWORD，添加用户登陆后的COOKIE即可。


最后感谢一下代理池的原作者https://github.com/jhao104/
。
