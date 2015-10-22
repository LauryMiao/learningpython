#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request as request
import urllib.parse as parse
import string
import re
import os
import urllib.error as error
print('''
++++++++++++++++++++++++++++++++++++++
Download the specific page on a website
Save as a html file
Version: python34
++++++++++++++++++++++++++++++++++++++
''')


def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page + 1):
        sName = ('f:/test/') + str(i).zfill(5) + ('.html')
        print('正在下载第' + str(i) + '个页面，并保存为' + sName)
        m = request.urlopen(url + str(i)).read()
        # create dir to store the picture
        dirpath = 'f:/test/'
        dirname = str(i)
        new_path = os.path.join(dirpath, dirname)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        page_data = m.decode('GBK', 'ignore')
        page_image = re.compile('\img src=\"(.+?)\"')
        count = 0
        for image in page_image.findall(page_data):
            pattern = re.compile(r'^http://.*.png$')
            if pattern.match(image):
                try:
                    image_data = request.urlopen(image).read()
                    image_path = dirpath + dirname + '/' + str(count) + '.png'
                    count += 1
                    print(image_path)
                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_data)
                except error.URLError as e:
                    print('Download failed')
        # print(m)
        with open(sName, 'wb') as file:  # b: binary
            file.write(m)
        file.close()

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/3872508923?pn='
    begin_page = 1
    end_page = 3
    baidu_tieba(url, begin_page, end_page)
