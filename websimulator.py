from selenium import webdriver
import os
import time
from bs4 import  BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient

#启动模拟浏览器
def simulator():
    chrome_driver = os.path.abspath("C:\chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chrome_driver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=D:/User Data")
    chrome = webdriver.Chrome(executable_path=chrome_driver,chrome_options=options)
    return chrome

#输入url得到含有文字信息的post存到数据库中
def getposts(url):
    chrome.get(url)
    lastHeight = chrome.execute_script("return document.body.scrollHeight")
    while(True):
        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1.5)
        newHeight = chrome.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    posts=chrome.page_source
    soup = BeautifulSoup(posts, 'lxml')
    name=soup.find_all('a',class_="_2nlw")
    #print(name[0].text)
    if name:
        cot=0
        postcollection=[]
        for k in soup.find_all('div',class_='fbUserContent _5pcr'):
            posttime=k.find_all('a',class_="_5pcq")
            poo=k.find_all('div',class_='_5pbx userContent')
            if poo:
                cot=cot+1
                po=poo[0].find_all('p')
                for i in po:
                    postinfo={"datatime":posttime[0].text,"post":i.text}
                    postcollection.append(postinfo)
        information={"name":name[0].text,"postcollect":postcollection}
    db.facebook.insert(information)
    print("get  "+str(cot)+"  posts"+" from  "+url)

#连接数据库
def startdatabase():
    client=MongoClient('*',27017)
    db=client.Crawler
    db.authenticate('***','***',mechanism='***')
    return db

db=startdatabase()
chrome=simulator()
while(True):
    c=input("输入url/*输入quit退出*/:")
    if c=="quit":
        break
    getposts(c)
chrome.close()
