#coding=utf-8

# 导入Itchat，一个封装好的微信接口库
import itchat
import os
# 导入Pillow，Python的图像处理库
import PIL.Image as Image
# 导入用来获取头像列表
from os import listdir
# 导入math做开平方使用
import math

#自动登陆，会出现二维码，扫码确认后登陆微信
itchat.auto_login(enableCmdQR=0)
#get_friends获取所有好友信息函数，返回list存储到friends变量
friends = itchat.get_friends(update=True)

user = friends[0]["UserName"]

print(user)
# 在当前路径下创建文件夹
os.mkdir(user)

num = 0
#列表下载所有好友头像并存储在/user
for i in friends:
	#赋值当前需要保存的图片的名称
        image_name = str(num)+'.jpg'
	#使用itchat自带函数get_head_img获取好友头像图片的二进制流
	img = itchat.get_head_img(userName=i["UserName"])[0:]
	#将图片二进制流img变量写入到images/文件夹下对应jpg文件
	fileImage = open(user + "/" + image_name + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	num += 1
# 获取返回得好友头像存储到ls
ls = os.listdir(user)

eachsize_line = int(math.sqrt(ls))
eachsize_row = int(math.sqrt(ls))

print(eachsize_line,eachsize_row)

#新建底图，长宽为行数*110px,列数*110px
toImage = Image.new('RGBA', (110 * eachsize_line, 110 * eachsize_row))

x = 0
y = 0
#循环粘贴每一个头像图片
for i in ls:
	try:
		#循环读取i对应的头像图片
		img = Image.open('user' + "/" + str(i) + ".jpg")
	except IOError:
		print (i)
		print("异常捕获，不影响结果")
	else:
		#按微信640*640等比例缩放64倍
		img = img.resize((110, 110), Image.ANTIALIAS)
		##计算图片粘贴的位置并拼接图片
		toImage.paste(img, (x * 110, y * 110))
		x += 1
		if x == eachsize_line:
			x = 0
			y += 1
# 保存图片
toImage.save('user' + ".jpg")
# 发送给文件助手
itchat.send_image('user' + ".jpg", 'filehelper')
