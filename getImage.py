#! /usr/bin/python3
import urllib.request
import re
import time
import os

#显示下载进度
def schedule(a,b,c):
	'''''
	a:已经下载的数据块
	b:数据块的大小
	c:远程文件的大小
   '''
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print ('%.2f%%' % per)

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	html = html.decode('utf-8')
	return html

def downloadImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	#定义文件夹的名字
	t = time.localtime(time.time())
	foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))
        #下载到的本地目录
	picpath = '/Users/ruxiankun/Desktop/pythonGetImage/images'
	
	if not os.path.exists(picpath):   #路径不存在时创建一个
		os.makedirs(picpath)   
	x = 0
	for imgurl in imglist:
		target = picpath+'//%s.jpg' % x
		print ('Downloading image to location: ' + target + '\nurl=' + imgurl)
		image = urllib.request.urlretrieve(imgurl, target, schedule)
		x += 1
	return image;

	
	
if __name__ == '__main__':
	print ('''			*************************************
			**	  Welcome to use Spider	  **
			**	 Created on  2016-11-20	  **
			**	   @author: ruxiankun		   **
			*************************************''')
	
	html = getHtml("http://tieba.baidu.com/p/2460150866")

	downloadImg(html)
	print ("Download has finished.")
