import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")
#各类电影top
#apply是用于遍历某一列中的所有元素
df['category']=df['tail'].apply(lambda x:x.split('/')[-1])
df['category'] = df['category'].apply(lambda x: [i.strip() for i in x.split(' ') if i.strip()!=''])
df_explode = df.explode('category')
category_counts=df_explode['category'].value_counts()
print(category_counts)
#可视化-绘制柱状图
category_counts.plot(kind='bar',figsize=(12,6))
plt.xticks(ticks=np.arange(len(category_counts)), labels=category_counts.index, rotation=45)
plt.title('Movie Categories Frequency')
plt.xlabel('Category',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.tight_layout()
plt.show()
#-------------各类电影Top------------#
df_sorted= df_explode.sort_values(['category','rating'], ascending=[True,False])
category_top=df_sorted.groupby('category').head(5)
print(category_top)
#-------------每类电影的平均评分------------#
category_mean=df_explode.groupby('category')['rating'].mean().sort_values(ascending=False)
print(category_mean)
#-----画图------
category_mean.plot(kind='bar',figsize=(12,6))
plt.xticks(ticks=np.arange(len(category_mean)), labels=category_mean.index, rotation=45)
plt.title('Movie Categories Name')
plt.xlabel('Category',fontsize=12)
plt.ylabel('Mean Rating',fontsize=12)
plt.tight_layout()
plt.show()
#---------------------年份趋势分析------------------
#--提取年份
df['year']=df["year"].astype(str).str.extract(r'(\d{4})')
#--缺失值检查--
print(df["year"].isna().sum())
#groupby锁定整个表，不用单独一列
year_mean=df.groupby("year")["rating"].mean()
year=year_mean.index
#--画折线图--
plt.figure(figsize=(20,6))
plt.plot(year,year_mean,marker="o",linestyle="-")
plt.xlabel('Years',fontsize=12)
plt.ylabel('Mean Rating',fontsize=12)
plt.tight_layout()
plt.show()