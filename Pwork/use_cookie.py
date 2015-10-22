#!/usr/bin//env python3
# -*- coding:utf_8 -*-

from urllib import request

req = request.Request('http://www.qiushibaike.com/hot/page/1')
req.add_header('User-Agent', 'Mozilla/6.0')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
        pat = re.compile('<div.*?>')
        items = re.findall(pat, f)
        for item in items:
            haveImg = re.search("img", item[3])
            if not haveImg:
                print(item[0], item[1], item[2], item[4])
