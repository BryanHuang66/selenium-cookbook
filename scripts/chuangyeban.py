from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import datetime
import requests
from selenium.webdriver.support.ui import WebDriverWait
from scripts.ExtractTXT import parsePDF
import os
from settings import location1,location2,interval
from selenium.webdriver.common.by import By 
def write_pdf(file_name,url):

    path = location2+ file_name + ".pdf"
    response = requests.get(url, stream="TRUE")
    with open(path, 'wb') as file:
        for data in response.iter_content():
            file.write(data)
        file.close()
    path2 = os.path.join(location1,file_name+'.md')
    parsePDF(path,path2)

def pdfurl(url):
    findlink = re.compile(r'<td><a href="(.*?)" target="_blank"')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.CLASS_NAME,"info-disc-table"))
    bs=BeautifulSoup(driver.page_source,'html5lib').body
    a = bs.find_all("tbody")
    link = ""
    for item in a:
        if "关于终止对" in item.text:
            link = re.findall(findlink,str(item))[0]
            break
    driver.close()
    return link




def chuangyeban(name):
    limit_date = datetime.datetime.now()+datetime.timedelta(days=-interval-1)
    findname = re.compile(r'target="_blank">(.*?) </a></td>')
    findlink = re.compile(r'<td><a href="(.*?)" target="_blank">')
    findzt = re.compile(r'">(.*?)</span></td> ')
    finddate = re.compile(r' <td class="text-center">(.*?)</td>')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(options = chrome_options)
    driver.get("http://listing.szse.cn/projectdynamic/"+name+"/index.html")
    time.sleep(1)
    flag=0
    IPO = []
    while flag == 0:
        page=BeautifulSoup(driver.page_source,'html5lib').body
        info = page.find_all("tr")

        for item in info:
            item = str(item)
            if re.findall(findname,item) != []:
                title = re.findall(findname,item)[0]
                link = re.findall(findlink,item)[0]
                zt = re.findall(findzt,item)[1]
                date = re.findall(finddate,item)[2]
                # print(date)
                compare_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                if compare_date < limit_date:
                    flag = 1
                    break
                finallink = "http://listing.szse.cn/" + link

                if "终止" and "撤回" in zt:
                    innerlink = pdfurl(finallink)
                    write_pdf(title, innerlink)
                IPO = IPO + [title] + [finallink] + [zt] + [date]
        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CLASS_NAME,'next'))
            time.sleep(1)
            a = driver.find_element(By.CLASS_NAME,'next')
            a.click()
        except Exception as e:
            flag = 1
            pass
    driver.close()
    return IPO