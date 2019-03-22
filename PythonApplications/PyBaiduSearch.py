#coding=utf-8
from selenium import webdriver
import time
import re
import random
from pyquery import PyQuery as pq

# 实现自动模拟鼠标点击爬虫
# form: https://blog.csdn.net/weixin_42551465/article/details/80817552
# 环境设置参考网页，安装selenium-base，pyquery；下载chrome浏览器和chromedriver


def  openurl(url, click_num):        
    browser  = webdriver.Chrome()  #打开浏览器        
    browser.get(url)               #进入相关网站          
    browser.get(url)               #进入相关网站          

    browser.get(url)               #进入相关网站          

    browser.get(url)               #进入相关网站          

    # 输入 + 点击按钮操作
    browser.find_element_by_id("kw").send_keys("美女")
    cnt=0

    while(1):	    
        browser.find_element_by_id("su").click() 
        cnt+=1
        print("Click: ",cnt)
                
        time.sleep(0.2+ random.randint(0,200)/200.0)  #make 0.2~0.4S delay
        if(cnt>click_num):
            break
	
	# 因为百度支持输入关键字后  回车搜索  所以这样做是可以的
	# browser.find_element_by_id("kw").send_keys("美女\r\n")   
	
	# find by ID - it is ok
	#browser.find_element_by_id("su").click()  

	# find by Class - it is ok too
	# browser.find_element_by_class_name("s_btn_wr").click()       


if __name__ == "__main__":
    url='https://www.baidu.com/'
    dict=openurl(url,100)

    print(dict)

