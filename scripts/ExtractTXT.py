# -*- coding: UTF-8 -*-

"""
1.加载一个指定路径文件夹内的所有pdf文内容
2.解析所有pdf内容并提取指定内容
3.把解析出来的指定内容写入Excel表格
"""

#################
import xlrd  # 打开excel文件
from xlutils.copy import copy
from pathos.multiprocessing import ProcessingPool as Pool
import os
import re
import sys
import importlib
import pdfminer
importlib.reload(sys)
import pdfplumber
import logging
logging.basicConfig(level=logging.ERROR)


# 解析PDF文件，转为txt格式
def parsePDF(PDF_path, TXT_path):
    try:
        with pdfplumber.open(PDF_path,password=b'') as pdf:
            with open(TXT_path, 'w', encoding='UTF-8', errors='ignore') as f:
                num = 0
                for page in pdf.pages:
                    num = num+1
                    print("\r正在处理%s的第%d页"%(os.path.basename(PDF_path),num),end="")
                    f.write(page.extract_text())
            f.close()
        print('\r'+os.path.basename(PDF_path)+' 处理完成')
    except Exception as e:
        print(PDF_path+"没有成功读取")
        pass
    print(' ',end='')


