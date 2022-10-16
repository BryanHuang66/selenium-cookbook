from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from settings import interval
from selenium.webdriver.common.by import By

def xinggufaxing():
    finddate = re.compile(r'<span title="(.*?)">')
    findtitle = re.compile(r'title="(.*?)">')
    findnumbername = re.compile(r'">(.*?)</a>')
    findlink = re.compile(r'<a href="//(.*?)">')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(options = chrome_options)
    driver.get("http://data.eastmoney.com/xg/xg/default.html")


    HuZhuban = []
    ShenZhuban = []
    Kechuangban = []
    Chuangyeban = []

    limit_date = datetime.datetime.now() + datetime.timedelta(days=-interval - 1)
    # 创业
    flag = 0
    driver.get("http://data.eastmoney.com/xg/xg/default.html")
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[5]'))
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[5]').click()
    time.sleep(2)
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        info = page.find_all("tr")
        for item in info:
            if "<tr data-index=" in str(item):
                date = re.findall(finddate, str(item))[-1]
                if date != "-":
                    compare_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    if compare_date < limit_date:
                        flag = 1
                    else:
                        title = re.findall(findtitle, str(item))[0]
                        number = re.findall(findnumbername, str(item))[0]
                        number_split = re.findall(r'<(.*?)>',number)
                        for subitem in number_split:
                            number = number.replace(subitem,'')
                        number = number.replace('<','')
                        number = number.replace('>','')
                        
                        
                        name = re.findall(findnumbername, str(item))[1]
                        name_spilit = re.findall(r'<(.*?)>',name)
                        for subitem in name_spilit:
                            name = name.replace(subitem,'')
                        name = name.replace('<','')
                        name = name.replace('>','')
                        
                        link = re.findall(findlink, str(item))[-1]
                        Chuangyeban = Chuangyeban + [number, name, date, link]

            try:
                WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.XPATH,"//a[@target='_self']")[-5])
                driver.find_elements(By.XPATH,"//a[@target='_self']")[-5].click()
            except Exception as e:
                flag = 1
                pass

    # 深A
    flag = 0
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[4]'))
    button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[4]/div[1]/ul/li[4]")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        info = page.find_all("tr")
        for item in info:
            if "<tr data-index=" in str(item):
                date =re.findall(finddate,str(item))[-1]

                if date != "-":
                    compare_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    if compare_date<limit_date:
                        flag = 1
                    else:
                        title = re.findall(findtitle,str(item))[0]
                        number = re.findall(findnumbername, str(item))[0]
                        number_split = re.findall(r'<(.*?)>',number)
                        for subitem in number_split:
                            number = number.replace(subitem,'')
                        number = number.replace('<','')
                        number = number.replace('>','')
                        
                        
                        name = re.findall(findnumbername, str(item))[1]
                        name_spilit = re.findall(r'<(.*?)>',name)
                        for subitem in name_spilit:
                            name = name.replace(subitem,'')
                        name = name.replace('<','')
                        name = name.replace('>','')
                        link = re.findall(findlink,str(item))[-1]
                        ShenZhuban = ShenZhuban + [number,name,date,link]

            try:
                driver.find_elements(By.XPATH,"//a[@target='_self']")[-5].click()
            except Exception as e:
                flag = 1
                pass

    driver.close()
    # 沪A
    flag = 0
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://data.eastmoney.com/xg/xg/default.html")
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[2]'))
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[2]').click()
    time.sleep(2)
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        info = page.find_all("tr")
        for item in info:
            if "<tr data-index=" in str(item):
                date =re.findall(finddate,str(item))[-1]

                if date != "-":
                    compare_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    if compare_date<limit_date:
                        flag = 1
                    else:
                        title = re.findall(findtitle,str(item))[0]
                        number = re.findall(findnumbername, str(item))[0]
                        number_split = re.findall(r'<(.*?)>',number)
                        for subitem in number_split:
                            number = number.replace(subitem,'')
                        number = number.replace('<','')
                        number = number.replace('>','')
                        
                        
                        name = re.findall(findnumbername, str(item))[1]
                        name_spilit = re.findall(r'<(.*?)>',name)
                        for subitem in name_spilit:
                            name = name.replace(subitem,'')
                        name = name.replace('<','')
                        name = name.replace('>','')
                        link = re.findall(findlink,str(item))[-1]
                        HuZhuban = HuZhuban + [number,name,date,link]

            try:
                WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath("//a[@target='_self']")[-5])
                driver.find_elements_by_xpath("//a[@target='_self']")[-5].click()
            except Exception as e:
                flag = 1
                pass

    # 科创
    flag = 0
    driver.get("http://data.eastmoney.com/xg/xg/default.html")
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[3]'))
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div[1]/ul/li[3]').click()
    time.sleep(2)
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        info = page.find_all("tr")
        for item in info:
            if "<tr data-index=" in str(item):
                date =re.findall(finddate,str(item))[-1]

                if date != "-":
                    compare_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    if compare_date<limit_date:
                        flag = 1
                    else:
                        title = re.findall(findtitle,str(item))[0]
                        number = re.findall(findnumbername, str(item))[0]
                        number_split = re.findall(r'<(.*?)>',number)
                        for subitem in number_split:
                            number = number.replace(subitem,'')
                        number = number.replace('<','')
                        number = number.replace('>','')
                        
                        
                        name = re.findall(findnumbername, str(item))[1]
                        name_spilit = re.findall(r'<(.*?)>',name)
                        for subitem in name_spilit:
                            name = name.replace(subitem,'')
                        name = name.replace('<','')
                        name = name.replace('>','')
                        link = re.findall(findlink,str(item))[-1]
                        Kechuangban = Kechuangban + [number,name,date,link]

            try:
                WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.XPATH,"//a[@target='_self']")[-5])
                driver.find_elements(By.XPATH,"//a[@target='_self']")[-5].click()
            except Exception as e:
                flag = 1
                pass

    return HuZhuban,ShenZhuban,Kechuangban,Chuangyeban



