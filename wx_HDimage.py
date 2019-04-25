#coding=utf-8

# 导入Itchat，一个封装好的微信接口库
import itchat
import os
# 导入Pillow，Python的图像处理库
import PIL.Image as Image
from os import listdir

itchat.auto_login(enableCmdQR=0)

friends = itchat.get_friends(update=True)

user = friends[0]["UserName"]

print(user)

os.mkdir(user)

num = 0
#列表下载所有好友头像并存储在/user
for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])[0:]
	fileImage = open(user + "/" + str(num) + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	num += 1

ls = os.listdir(user)

numPic = len(ls)

print(numPic)

eachsize_line = int(math.sqrt(ls))
eachsize_row = int(math.sqrt(ls))

print(eachsize_line,eachsize_row)


toImage = Image.new('RGBA', (110 * eachsize_line, 110 * eachsize_row))

x = 0
y = 0

for i in ls:
	try:
		#从./images打开图片
		img = Image.open('user' + "/" + str(i) + ".jpg")
	except IOError:
		print (i)
		print("异常捕获，不影响结果")
	else:
		#按微信640*640等比例缩放64倍
		img = img.resize((110, 110), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * 110, y * 110))
		x += 1
		if x == eachsize_line:
			x = 0
			y += 1

toImage.save('user' + "all.jpg")

itchat.send_image('user' + ".jpg", 'filehelper')
