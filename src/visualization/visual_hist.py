import matplotlib.pyplot as plt
#matplot画图工具
import pandas as pd
#pandas数据表格
import numpy as np
#numpy数据计算
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")
#bins代表边界,arange左闭右开
bins=np.arange(8.0,10.01,0.25)
#加大画布
plt.figure(figsize=(8,5))
#hist用法：plt.hist(x数值,bins分箱数，color=''柱子颜色,edgecolor描边，alpha透明度（0~1）)
'''
zip 的意思是：
把两个列表“打包”在一起。
举个例子：
counts = [3, 5, 12]
bins = [8.0, 8.1, 8.2]
zip 后变成：
(3, 8.0)
(5, 8.1)
(12, 8.2)
'''
plt.title("Distribution of Ratings",fontsize=14)
#hist直方图
counts,bins,patches=plt.hist(df['rating'],bins=bins,edgecolor='black',alpha=0.7,width=0.23)
for count, left, right in zip(counts, bins[:-1], bins[1:]):
    center = (left + right) / 2
    if count > 0:
        plt.text(center, count+0.05, int(count), ha='center', va='bottom',fontsize=10)
plt.xlabel('Rating',fontsize=12)
plt.ylabel('The number of films',fontsize=12)
mean_rating=np.sum(df['rating'])/df['rating'].count()
y_max=max(counts)
y_text=max(counts)*1.02
s=f"Mean:{mean_rating:.2f}"
#count()是python中内置方法，方法。。。.count()，只能测试其数值出现次数，len()是python内置函数，考研计算总长度
plt.axvline(mean_rating,linestyle='--',color='red',label=f'Mean: {mean_rating:.2f}')
plt.text(mean_rating+0.2,y_max,s,ha='center',fontsize=10,color="red")
plt.show()

