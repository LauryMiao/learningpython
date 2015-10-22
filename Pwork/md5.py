#！/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())



# verify the status of login (with regiester)

# get MD5 value
def calc_md5(password):
	p_md5 = hashlib.md5()
	p_md5.update(password.encode('utf-8'))
	return p_md5.hexdigest()

# Initialize the database	
db = {
	'michael':'e10adc3949ba59abbe56e057f20f883e',
	'bob':'878ef96e86145580c38c87f0410ad153',
	'alice':'99b1c2188db85afee403b1536010c2c9'
}

# regiester for new users
def regiester(name, pw):
	db[name] = calc_md5(pw)

# login
def login(user, password):
	
	if user in db.keys():
		if calc_md5(password) == db[user]:
			print('%s Log in: Successful' % user)
		else:
			print('%s Log in: Failed' % user)
	else:
		print('%s is not regiested in the database!!!' % user)

# main codes		
regiester('Lisa','x1010')	
login('Michael','123435')
login('Lisa','x1010')
		