#hist是直方图
#引入工具
import matplotlib.pyplot as plt
#matplot画图工具
import pandas as pd
#pandas数据表格
import numpy as np
#numpy数据计算
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")
#bins代表边界,arange左闭右开
bins=np.arange(8.0,10.01,0.25)
#计算
mean_rating=df['rating'].mean()
median_rating=df['rating'].median()
standard_rating=df['rating'].std()
#设置画布
plt.figure(figsize=(8,5))
#画画
counts,bin_edges,patches=plt.hist(df['rating'],bins=bins,edgecolor='black',alpha=0.7)
y_max=max(counts)
plt.title("Distribution of Ratings",fontsize=14)
for count, left, right in zip(counts, bin_edges[:-1], bin_edges[1:]):
    center = (left + right) / 2
    if count > 0:
        plt.text(center, count+0.05, int(count), ha='center', va='bottom',fontsize=10)
plt.xlabel('Rating',fontsize=12)
plt.ylabel('The number of films',fontsize=12)
#count()是python中内置方法，方法。。。.count()，只能测试其数值出现次数，len()是python内置函数，计算总长度
plt.axvline(mean_rating,linestyle='--',color='red',label=f'Mean: {mean_rating:.2f}')
plt.axvline(median_rating,linestyle='--',color='blue',label=f'Median_rating: {median_rating:.2f}')
plt.axvline(mean_rating+standard_rating,linestyle=':',color='green',label=f'1+ std_rating: {mean_rating+standard_rating:.2f}')
plt.axvline(mean_rating-standard_rating,linestyle=':',color='green',label=f'-1 std_rating: {mean_rating-standard_rating:.2f}')
plt.legend(loc='upper right', fontsize=9)
plt.show()
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
