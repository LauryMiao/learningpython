import urllib.request
import re

url = 'http://www.douban.com'
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
req = urllib.request.Request(url=url, headers=req_header)
data = urllib.request.urlopen(req).read().decode('UTF-8')
re_link = re.compile(r'<a[^>]*?href="([\S]*?)">')#>(.*?)</a>') a bug for chinese characters sets
link_url = re_link.findall(data)
print(link_url[:2])
with open('D:/Pwork/robot2/link2.txt','w') as L_file:
	for x in link_url:
		L_file.write(x)
L_file.close()