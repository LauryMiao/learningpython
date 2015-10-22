 #!/usr/bin//env python3
 # -*- coding:utf_8 -*-
 
from urllib import request, parse

 # get
 
with request.urlopen('http://blog.csdn.net/aqcre') as f:
	data = f.read()
	print('Status: ', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
#	print('Data: ', data)
	
# advanced get:

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version.8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as ff:
	print('Status: ', ff.status, ff.reason)
	for k, v in ff.getheaders():
		print('%s: %s' % (k, v))
	print('Data: ', ff.read().decode('utf-8'))
	
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
	('username', email),
	('passwd', passwd),
	('entry', 'mweibo'),
	('client_id', ''),
	('savestate', '1'),
	('ec', ''),
	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom&jumpfrom=weibocom')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom')

with request.urlopen(req, data=login_data.encode('utf-8','ignore')) as f:
	print('Status: ', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data: ', f.read().decode('utf-8'))
