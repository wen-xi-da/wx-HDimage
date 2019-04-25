#coding=utf-8
# from numpy import *
import itchat
import os

import PIL.Image as Image
from os import listdir
import math

# itchat.auto_login(enableCmdQR=0)

# friends = itchat.get_friends(update=True)

# user = friends[0]["UserName"]

# print(user)

# os.mkdir(user)

# num = 0

# for i in friends:
# 	img = itchat.get_head_img(userName=i["UserName"])[0:]
# 	fileImage = open(user + "/" + str(num) + ".jpg",'wb')
# 	fileImage.write(img)
# 	fileImage.close()
# 	num += 1

# print "下载头像结束"
ls = os.listdir('./f5e04e2d800aa1d1afc5458b2f1387953beb25ed97009fa590d8bae1178b5a7d')
# pics = listdir(user)

numPic = len(ls)

print(numPic)

eachsize_line = 35
eachsize_row = 75

print(eachsize_line,eachsize_row)

# numline = int(640 / eachsize)

toImage = Image.new('RGBA', (200 * eachsize_line, 200 * eachsize_row))


# print(numline)

x = 0
y = 0

for i in range(0,2627):
	try:
		#打开图片
		img = Image.open('./f5e04e2d800aa1d1afc5458b2f1387953beb25ed97009fa590d8bae1178b5a7d' + "/" + str(i) + ".jpg")
		# if img.mode != "RGBA":
		# 	img = img.covert("RGBA")
	except IOError:
		print (i)
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((200, 200), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * 200, y * 200))
		x += 1
		if x == eachsize_line:
			x = 0
			y += 1


toImage.save('./f5e04e2d800aa1d1afc5458b2f1387953beb25ed97009fa590d8bae1178b5a7d' + "all.jpg")


itchat.send_image('./f5e04e2d800aa1d1afc5458b2f1387953beb25ed97009fa590d8bae1178b5a7d' + ".jpg", 'filehelper')
