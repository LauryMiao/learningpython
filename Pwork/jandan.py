#-*- coding:utf-8 -*-

import urllib.request as ur
import re

# 设置代理,不需要代理的此段注释掉


def set_proxy(ser_ip, port):
    proxy_support = ur.ProxyHandler({'http': '%s:%s' % (ser_ip, port)})
    opener = ur.build_opener(proxy_support)
    ur.install_opener(opener)

# 设置正则表达式
pattern = re.compile(
    r'<a[\s\S]+?>(\d+)<[\s\S]+?img src="(http://.+?.jpg)"')
# <li[\s\S]+?>#(\d+)<[\s\S]+?img src="(http://.+?)"[\s\S]+?</li>
pa_cur_page = re.compile(
    r'<span class="current-comment-page">\[(\d+)\]</span>')  # get the last page

# 全局变量
url_base = 'http://jandan.net/ooxx/page-%s#comments'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml; "
    "q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "text/html",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 6253.0.0) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/39.0.2151.4 Safari/537.36"
}


def get_img_set(start_page, end_page):
    start_page, end_page = int(start_page), int(end_page)
    img_set = set()
    req = ur.Request(url='http://jandan.net/ooxx', headers=headers)
    last_data = ur.urlopen(req).read().decode()
    last_page = int(pa_cur_page.findall(last_data)[0])
    print('last page:%s' % last_page)
    end_page = end_page if end_page < last_page else last_page
    print('page:%s-%s' % (start_page, end_page))

    for p in range(start_page, end_page + 1):
        url = url_base % p
        req = ur.Request(url=url, headers=headers)
        data = ur.urlopen(req).read().decode()
        img_list = pattern.findall(data)
        print('page:%5s : pictures:%2s' % (p, len(img_list)))
        img_set1 = set([(p,) + i for i in img_list])
        # list ((1531, '146', 'http://ww3.sinaimg.cn/mw600/4a55952egw1eviwe4ox5pj20xc1clgve.jpg'))
        img_set = img_set.union(img_set1)

    return img_set


def down_load(img_set, path):
    result = {'s': 0, 'f': 0}
    count = 0
    total = len(img_set)
    for s in img_set:
        count += 1
        try:
            url = s[2]
            gs = url.rsplit('.', 1)[1]
            # 保存路径和文件名称，命名规则：page_图片楼层号
            path_1 = '%s/%s_%s.%s' % (path, s[0], s[1], gs)
            ur.urlretrieve(url, path_1, headers)
            print('[%4s/%4s]' % (count, total), path_1, 'get !')
            result['s'] += 1
        except:
            print(s, 'get failed !')
            result['f'] += 1
    return result


if __name__ == '__main__':
    img_set = get_img_set(1530, 1531)
    print('共有%s张图片' % len(img_set))
    r = down_load(img_set, 'D:/jiandan/')
    print('下载完成,succeed:%s;failed:%s' % (r['s'], r['f']))
