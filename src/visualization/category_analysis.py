import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")
#各类电影top
#apply是用于遍历某一列中的所有元素
df['category']=df['tail'].apply(lambda x:x.split('/')[-1])
df['category'] = df['category'].apply(lambda x: [i.strip() for i in x.split(' ')])
df_explode = df.explode('category')
category_counts=df_explode['category'].value_counts()
print(category_counts)
#可视化-绘制柱状图
category_counts.plot(kind='bar',figsize=(12,6))
plt.xticks(ticks=np.arange(len(category_counts)), labels=category_counts.index, rotation=45)
plt.title('Movie Categories Frequency')
plt.xlabel('Category',fontsize=8)
plt.ylabel('Count',fontsize=8)
plt.tight_layout()
plt.show()
#-------------各类电影Top------------#
df_sorted= df_explode.sort_values(['category','rating'], ascending=[True,False])
category_top=df_sorted.groupby('category').head(5)
print(category_top)