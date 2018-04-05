# -*- coding: utf-8 -*-python3.6 python-Levenshtein
"""
Created on Wed Apr  4 10:07:46 2018

@author: cimepc19
"""
'''

'''
import Levenshtein
'''
fnm1=str(input("Enter the name of 1st file: "))
ini1=int(input("Enter the start line of 1st file: "))-1

        
fnm2=str(input("Enter the name of 2nd file: "))
ini2=int(input("Enter the start line of 2nd file: "))-1
diffdu=int(input("Enter the tolerated number of letter: ")) 
'''  
'''
设置文件名和行数
'''      
fnm1=str(input("输入第1个文件名-含后缀: "))
ini1=int(input("输入第一条专利开始的行号(文件1): "))-1
        
fnm2=str(input("输入第2个文件名-含后缀: "))
ini2=int(input("输入第一条专利开始的行号(文件2): "))-1
diffdu=int(input("输入能够容忍的不重复字数-推荐30: "))        
#file = open("zh.lmp", "rb")   #,encoding='gb18030'
#file1 = open("zh.lmp", encoding='utf-8',errors='ignore') 
#file2 = open("eng.lmp", encoding='utf-8',errors='ignore') 
'''
读取文件并且
'''
file1 = open(fnm1, encoding='utf-8',errors='ignore') 
file2 = open(fnm2, encoding='utf-8',errors='ignore') 

cont1 = file1.readlines()
cont2 = file2.readlines()
#print(cont1)
contlen1=len(cont1)
contlen2=len(cont2)
'''
打印两个文件行数
'''
print(contlen1)#打印两个文件行数
print(contlen2)
#ind=list(range(contlen1))
#res=list(range(contlen1))

#
#for tp in range(ini1):
#    res[tp]=9999
       

finalmatch=list(range(contlen2))
#indd=tuple(range(contlen1))
#dic={indd:""}
#
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

#file = open("matchresult.txt", "w")
#amount_written = file.write(finalmatch)

#file.close()
    
#print(resind,res[resind])       
'''
zzz=finalmatch[4][2]  

finalmatch2=list(finalmatch)

#file = open("matchresult.txt", "w")
#amount_written = file.write(finalmatch)
##print(amount_written)
#file.close()

fl = open("matchresult.txt", "w")
for i in finalmatch:
    
    fl.write(str(i))
    fl.write("\n")
fl.close()

'''
    
    
#txt_a='本发明公开了一种制备热镀锌高强钢过程中镀层的方法，属于钢铁冶金领域。本发明要解决的技术问题是提供一种成本低廉、工艺简单、镀锌效果优异的制备热镀锌高强钢过程中镀层的方法。一种制备热镀锌高强钢过程中镀层的方法，该方法包括热镀锌退火工艺：700℃以下加热过程中露点为‑15～‑25℃，700℃及以上加热和保温过程中露点为‑30～‑40℃，入锌锅温度根据带钢厚度控制。本发明采用预氧化还原工艺控制镀锌表面质量，预氧化在表面形成一层氧化铁复合物，使Si、Mn原子处于次表层；还原工艺在高温均热过程中将氧化铁还原为海绵铁，Si、Mn原子形成的氧化物处于海绵铁的覆盖层以下，明显改善镀锌表面质量，具有显著的经济效益和社会效益。'
#txt_b='一种无表面缺陷且具有改善的镀锌特性和合金化特性的高锰热轧镀锌钢板通过使用高锰热轧钢板而制造。提供了高锰热轧镀锌钢板和制造所述高锰热轧镀锌钢板的方法。所述高锰热轧镀锌钢板包括：含有5重量％至35重量％的锰的热轧钢板；以及在热轧钢板上形成的锌镀层，其中，在朝向锌镀层的热轧钢板的内部区域中形成内部氧化物层。'
#txt_c='一种无表面缺陷且具有改善的镀锌特性和合金化特性的高锰热轧镀锌钢板通过使用高锰热轧钢板而制造。提供了高锰热轧镀锌钢板和制造所述高锰热轧镀锌钢板的方法。所述高锰热轧镀锌钢板包括：含有5％重量至35％重量的锰的热轧钢板；以及在热轧钢板上形成的锌镀层，其中，在朝锌镀层的热轧钢板的内部区域中形成内部氧化物层。'
#txt_d='一种去除助溶剂中铁离子的方法，用以润湿铁材对象的表面，该方法包括：以溶剂、氯化锌及氯化铵而在配制槽中配制助溶剂并送至处理槽；浸泡铁材对象于助溶剂中以溶出表面的部分铁并产生润湿作用；加入高氧化性气体以氧化助溶剂中的铁离子，形成氧化铁而沉淀；抽取出助溶剂并利用多层滤网过滤出已沉淀的氧化铁；以及将过滤后的助溶剂回流至处理槽中，并重复上述的铁材对象浸泡处理，以持续去除铁材对象浸泡处理中所产生的铁离子。本方法可维持助溶剂中氯化锌及氯化铵的浓度，确保钢铁表面上的润湿作用，而不需额外补充氯化锌及氯化铵。'
#txt_e='热冲压制品的制造方法包括：成形工序，对其上形成有镀锌层(12)的镀锌钢板(1)进行加热并通过热冲压将经加热的镀锌钢板(1)成形；除去工序，在成形工序后对形成于镀锌层(12)的表面上的氧化膜(13)照射激光以除去氧化膜(13)；涂装工序，在除去工序后在通过热冲压成形的镀锌钢板(1)上进行涂装处理。'
#txt_f=''
#txt_g=''
#print(Levenshtein.distance(txt_a,txt_b))
#print(Levenshtein.distance(txt_a,txt_b))
#
#print(Levenshtein.distance(cont1[1],cont2[0]))
#print(Levenshtein.distance(txt_c,txt_d))
#print()
#print()
#print()
#print()