from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import datetime
from scripts.ExtractTXT import parsePDF
import requests
from selenium.webdriver.support.ui import WebDriverWait
import os
from settings import location1,location2,interval
from selenium.webdriver.common.by import By 

def write_pdf(file_name,url):
    path = location2+ file_name + ".pdf"
    response = requests.get("http://"+url, stream="TRUE")
    with open(path, 'wb') as file:
        for data in response.iter_content():
            file.write(data)
        file.close()
    path2 = os.path.join(location1,file_name+'.md')
    parsePDF(path,path2)

def pdfurl(url):
    findlink = re.compile(r'href="//(.*?)" target="_blank">')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    bs=BeautifulSoup(driver.page_source,'html5lib').body
    a = bs.find_all("tbody")
    link = ""
    for item in a:
        if "关于终止对" in item.text:
            link = re.findall(findlink,str(item))[0]
            break
    driver.close()
    return link

def kechuangban():
    findlink = re.compile(r'<a href="(.*?)" target="_blank">')

    limit_date = datetime.datetime.now() + datetime.timedelta(days=-interval - 1)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://kcb.sse.com.cn/renewal/")
    flag =0
    IPO=[]
    REF = []
    REP = []
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        ipo = page.find('div', class_="container", id="stock_list").tbody
        ipogsxm = ipo.find_all('td', class_="td_break_word_7")
        ipoalltime = ipo.find_all('td', class_="td_no_break")
        ipoallzt = ipo.find_all('td',class_ = "td_break_word_3")
        for i in range(0,len(ipogsxm)):
            ipolink = re.findall(findlink, str(ipogsxm[i]))[0]
            ipodate = ipoalltime[4*i+2]
            ipozt = ipoallzt[2*i]
            compare_date = datetime.datetime.strptime(ipoalltime[4 * i + 2].string, '%Y-%m-%d')
            if compare_date<limit_date:
                flag = 1
            else:
                if "终止" in ipozt.text:
                    innerlink = pdfurl("https://kcb.sse.com.cn"+ipolink)
                    write_pdf(ipogsxm[i].text, innerlink)
                IPO = IPO+[ipogsxm[i].text,"https://kcb.sse.com.cn"+ipolink,ipozt.text,ipodate.string]

        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID,"dataList1_container_next"))
        except Exception as e:
            flag =1
            pass
        js = 'document.getElementById("dataList1_container_next").click()'
        driver.execute_script(js)


    flag = 0
    driver.find_element(By.XPATH,'/html/body/div[6]/ul/li[3]/a').click()
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        refinance = page.find('div', class_="container", id="stock_list2").tbody

        refgsxm = refinance.find_all('td', class_="new_min_width")
        refalltime = refinance.find_all('td', class_="td_no_break")
        refallzt = refinance.find_all('td', class_="new_min_width td_break_word_3")
        for i in range(0,len(refgsxm),3):
            reflink = re.findall(findlink, str(refgsxm[i]))[0]
            refdate = refalltime[int(i)+1]
            compare_date = datetime.datetime.strptime(refalltime[int(i) + 1].string, '%Y-%m-%d')
            if compare_date<limit_date:
                flag = 1
            else:
                if "终止" in refallzt[int(i/3)].text:
                    innerlink = pdfurl("https://kcb.sse.com.cn"+reflink)
                    write_pdf(refgsxm[i].text, innerlink)
                REF = REF+[refgsxm[i].text,"https://kcb.sse.com.cn"+reflink,refallzt[int(i/2)].text,refdate.string]

        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("dataList1_container_next"))
        except Exception as e:
            flag=1
            pass
        js = 'document.getElementById("dataList1_container_next").click()'
        driver.execute_script(js)

    flag = 0
    driver.find_element(By.XPATH,'/html/body/div[6]/ul/li[4]/a').click()
    while flag == 0:
        page = BeautifulSoup(driver.page_source, 'html5lib').body
        reproperty = page.find('div', class_="container", id="stock_list1").tbody

        repgsxm = reproperty.find_all('td', class_="new_min_width")
        repalltime = reproperty.find_all('td', class_="td_no_break")

        for i in range(0,len(repgsxm),2):
            replink = re.findall(findlink, str(repgsxm[i]))[0]
            repzt = repgsxm[i+1].text
            repdate = repalltime[int(3/2*i)+1]
            compare_date = datetime.datetime.strptime(repalltime[int(3/2*i)+ 1].string, '%Y-%m-%d')
            if compare_date<limit_date:
                flag = 1
            else:
                if "终止" in repzt:
                    innerlink = pdfurl("https://kcb.sse.com.cn"+replink)
                    write_pdf(repgsxm[i].text, innerlink)
                REP = REP+[repgsxm[i].text,"https://kcb.sse.com.cn"+replink,repzt,repdate.string]


        print(driver.find_element(By.ID,'dataList1_container_next').text)
        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID,"dataList1_container_next"))
        except Exception as e:
            flag=1
            pass
        js = 'document.getElementById("dataList1_container_next").click()'
        driver.execute_script(js)


    driver.close()
    return IPO,REF,REP


