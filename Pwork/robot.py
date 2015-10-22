import urllib.request
import os
import re

print('''
######################################
Software: web_robot for www.douban.com
@Author:  Laury Miao
Version: 1.0
Coding: Python3.4
Usage: get the main page of www.douban.com and download its jpg and png files
######################################
''')

# make dirs for douban_robot, jpg, png
dirpath = 'D:/Pwork/webrobot/'
if not os.path.isdir(dirpath):
    os.makedirs(dirpath)
jpg_path = dirpath + 'jpgfiles/'
png_path = dirpath + 'pngfiles/'
if not os.path.isdir(jpg_path):
    os.makedirs(jpg_path)
if not os.path.isdir(png_path):
    os.makedirs(png_path)


douban_robot = dirpath + 'douban.html'


url = "http://www.douban.com"

#get .html
req_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=req_header)
data = urllib.request.urlopen(req).read().decode('UTF-8')
urllib.request.urlretrieve(url, douban_robot)

'''
with open(douban_robot, 'wb') as dbr:
	dbr.write(bytes(data, 'UTF-8'))
dbr.close()
'''
# create regex
re_jpg = re.compile(r'(http:[^\s<>""]*?jpg)')
re_png = re.compile(r'(http:[^\s<>""]*?png)')
jpg_data = re_jpg.findall(data)
png_data = re_png.findall(data)
print(jpg_data)
print()
print(png_data)

# get jpg files
i = 1
for image in jpg_data:
    image = urllib.request.urlopen(image).read()
    jpg_name = jpg_path + str(i) + '.jpg'
    #urllib.request.urlretrieve(image, jpg_name)

    with open(jpg_name, 'wb') as jpg_file:
        jpg_file.write(image)
    jpg_file.close()
    i += 1

for image in png_data:
    #image = urllib.request.urlopen(image).read()
    png_name = png_path + str(i) + '.png'
    urllib.request.urlretrieve(image, png_name)
#	with open(png_name, 'wb') as png_file:
#		png_file.write(image)
#	png_file.close()
    i += 1
