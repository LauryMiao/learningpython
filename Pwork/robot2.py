import urllib.request
import os
import re

print('''
######################################
Software: web_robot for www.douban.com
@Author:  Laury Miao
Version: 2.0
Coding: Python3.4
Date: 18 Jul 2015
######################################
''')
'''
http://www.douban.com
http://www.163.com
http://www.ifeng.com
'''

abs_Dir = 'D:/Pwork/robot2/'  # absolute path for storing files
Queue = ['http://www.douban.com', ]  # url queue, initial value: the main site
fetch_List = []  # link list for thosed crawled
img_List = []   # img list for thosed downloaded
# regex for the url inside the main site
rg_inner = re.compile(r'http://www.[\S]+?.com[\S]*?')


def saveLinks(link_list):
    for link in link_list:
        if rg_inner.findall(link):  # inner website of the main site
            if link not in Queue:  # new links
                Queue.append(link)


def makepath(path):   # make dirs
    if not os.path.isdir(path):
        os.makedirs(path)
        return 1
    else:
        return 0


def getHtml(url, p_path):
    # print(url_name)
    html_name = p_path + url_name[0] + '.html'
    makepath(p_path)

    urllib.request.urlretrieve(url, html_name)  # store .html
    fetch_List.append(url)


def getDate(url):  # get data from the given url
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=req_header)
    data = urllib.request.urlopen(req).read().decode('UTF-8', 'ignore')
    return data


def getLinks(url):  # get href_links from the given url

    data = getDate(url)
    # re_link = re.compile(r'<a[^>]*?href="([\S]*?)">(.*?)</a>')# a bug for
    # chinese characters sets
    # >(.*?)</a>') a bug for chinese characters sets
    re_link = re.compile(r'<a[^>]*?href="(http://[\S]*?)">')
    link_url = list(set(re_link.findall(data)))
    # print(link_url)
    with open('D:/Pwork/robot2/www.txt', 'a+') as uf:
        for per_link in link_url:
            uf.write(per_link + '\n')
    uf.close()
    return link_url


def getImgUrl(url):
    data = getDate(url)  # call getDate function
    re_pic = re.compile(r'(http:[^\s<>""]*?\.(jpg|png|bmp))')
 #       r'(http:[^\s<>""]*?\.jpg|http:[^\s<>""]*?\.png|http:[^\s<>""]*?\.gif|http:[^\s<>""]*?\.bmp)')
    pic_url = re_pic.findall(data)
    # print(pic_url)
    return pic_url


def downloadImg(pic_url, p_path):  # imgurl passed from getImgUrl
    # create img file
    for image in pic_url:
        img_suffix = image[1]
        # print(img_suffix)
        img_path = p_path + img_suffix + '/'
        img_name = img_path + str(i) + '.' + img_suffix
        makepath(img_path)
        # download
        urllib.request.urlretrieve(image, img_name)
        img_List.append(image)


i = 1
for web in Queue:
    if web not in fetch_List:  # not crawled yet!
        # Queue.pop(web)
        # match the site name
        re_html = re.compile(r'^[\S]+?://[\S]+?\.([\S]+?)\.[\S]{2,4}.*?')
        url_name = re_html.findall(web)
        p_path = abs_Dir + url_name[0] + '/'
        # get html
        getHtml(web, p_path)
        # get links, and add them to Queue
        saveLinks(getLinks(web))
        # get img and download them
        for web_img in getImgUrl(web):
            if web_img not in img_List:
                downloadImg(web_img, p_path)
        # img_List.append(web_img)
                i += 1
        # add fetch_List
        fetch_List.append(web)
        print(web)
        with open('D:/Pwork/robot2/web.txt', 'a+') as web_file:
            web_file.write(web + '\n')
        web_file.close()
