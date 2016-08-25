import os
import re
import urllib
from urllib import request
from urllib.request import urlopen

url = 'http://tieba.baidu.com/p/4750932015'


def downLoad(data):
    dir = '0013'
    if not os.path.exists(dir):
        os.mkdir(dir)

    for url in data:
        imgurlData = urllib.request.urlopen(url).read()
        # 名称
        name = re.split('/', url)[-1]
        path = dir + '/' + name
        print(path)
        f = open(path, 'wb')
        try:
            f.write(imgurlData)
        except:
            print("except")
        f.close()


def getImageUrl(param):
    re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
    data = re_Imageurl.findall(param)
    downLoad(data)


def read_url(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE /360/ /chrome/ig)')
    with request.urlopen(req) as f:
        #         获取data
        getImageUrl(f.read().decode('utf-8'))


read_url(url)
