# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:14:30 2018

@author: cimepc19
"""

import sys
import os
import win32api
import Levenshtein
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog 

qtCreatorFile = "second.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
#        self.finalfiles.clicked.connect(self.CalculateTax)
        self.finalfiles.clicked.connect(self.Producefile)
        self.file1Button.clicked.connect(self.msg1)#定义第一个选文件的按钮关联的函数@@@定义按钮名
        self.file2Button.clicked.connect(self.msg2)
    
    def msg1(self):  

        (fileName1,tp1) = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "./",  
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔；选取本文件夹内容  
#        print(fileName1)  
        strfileName1=str(fileName1)
        self.file1.setText(strfileName1)#把第一个框框里设置成第一个文件路径
    def msg2(self):  

        (fileName2,tp2) = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "./",  
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔；选取本文件夹内容  
#        print(fileName1)  
        strfileName2=str(fileName2)
        self.file2.setText(strfileName2)#把第一个框框里设置成第一个文件路径

#    def CalculateTax(self):
#        price = int(self. file1. toPlainText())
#        tax = (self.lineof1.value())
#        total_price = price  + ((tax / 100) * price)
#        total_price_string = "The total price with tax is: " + str(total_price)
#        self.label1.setText(total_price_string)

    def Producefile(self):
         ini1=(self.lineof1.value())-1
         ini2=(self.lineof2.value())-1
         diffdu=int(self.diffdu.value())
         fnm1=str(self.file1.toPlainText())
         fnm2=str(self.file2.toPlainText())
         file1 = open(fnm1, encoding='utf-8',errors='ignore') 
         file2 = open(fnm2, encoding='utf-8',errors='ignore') 
         cont1 = file1.readlines()
         cont2 = file2.readlines()
         contlen1=len(cont1)
         contlen2=len(cont2)
         print(contlen1)
         print(contlen2)
         finalmatch=list(range(contlen2))
         count=0
         for j in range(ini2,contlen2):
           res=[9999]*contlen1#初始化存储差异度数量的向量-元素个数等于文档一的行数，并把所有差异度设为9999
           if len(cont2[j])<=1:#如果文件2的是空行，那么就跳过
               continue
           
           for i in range(ini1,contlen1):
             res[i]=Levenshtein.distance(cont1[i],cont2[j])#对于文档2第j+1行，遍历文档1求出文档1的每行针对这一行的差异度，
             
           resind=res.index(min(res))#求出文档1中与文档2 j+1行 差异最小的 （行数-1）
           if res[resind]<diffdu:
               count+=1
           finalmatch[j]=[resind+1,j+1,res[resind]]#汇总到【文件1，文件2，差异度】格式，按文件2的行数存储
         
         print("finalmatchnumber:",count)
         
         #写文件，如果是没有存储list的index就跳过，如果差异度小于定义的就保留
         fl = open("matchresult.txt", "w")
         for i in finalmatch:
             if type(i)==int:
                 continue
             
             elif i[2]<diffdu:
                  fl.write(str(i))
                  fl.write("\n")
         fl.close() 
         cupath=os.getcwd()
         zttext="匹配完成，请查看自动打开的文件，或者进入"+cupath+"查看matchresult.txt文件。\n就能得到按excel文件最左行号对应的match结果(文件1行号，文件2行号，不重复度)"
         #字符串的拼接可以用+，否则会组成一个list或者tuple
         self.zhuangtai.setText(zttext)
#         os.system('notepad matchresult.txt')
         win32api.ShellExecute(0, 'open', 'notepad.exe', 'matchresult.txt','',1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    


