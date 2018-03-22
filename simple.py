# coding=utf-8
import urllib2
import re
# 通过规律可以发现page后面的数字为页码。
page = 1
# 对URL进行字符串地址的拼接；
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# 请求头
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 将请求头封装成字典的形式以参数的形式，用于客户端的请求访问。
headers = {'User-Agent': user_agent}
print('测试A')
# 因为网络连接是不稳定的，也可能会造成请求失败，所以要进行URLEOOR的异常捕获。
try:
    # url作为Request()方法的参数，构造并返回一个Request对象
    request = urllib2.Request(url, headers=headers)
    # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    response = urllib2.urlopen(request)
    # 将服务器的响应的内容解码并读取出来。
    content = response.read().decode('utf-8')
    # print(content)
    # re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
    pattern = re.compile('<h2>(.*?)</h2>.*?<span>(.*?)</span>', re.S)
    print('测试B')
    items = re.findall(pattern, content)
    print('测试C')
    # (.*?)代表一个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。
    for item in items:
        print item[0], item[1]
except urllib2.URLError, e:
    # hasattr属性可以提前对属性进行判断；
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason