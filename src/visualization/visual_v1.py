#正态分布是为了正态分布不是为了判断“数据可不可用”
import matplotlib.pyplot as plt
#matplot画图工具
import pandas as pd
#pandas数据表格
import numpy as np
#导入scipy库，看是否拒绝正态分布
from scipy import stats
#numpy数据计算
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")
mean_rating=df['rating'].mean()
median_rating=df['rating'].median()
standard_rating=df['rating'].std()
print(f"Mean:{mean_rating:.2}")
print("Median:",median_rating)
print(f"standard_rating:{standard_rating:.2}")
#评分高于或低于平均分概率
great_ratio=(df['rating']>mean_rating).mean()
less_ratio=(df['rating']<mean_rating).mean()
print(f"great_ratio:{great_ratio:.2}")
print(f"less_ratio:{less_ratio:.2}")
#偏度分析：右尾偏长
skewness_value=df['rating'].skew()
print(f"skewness_value:{skewness_value:.3}")
#|skewness|<0.5为基本对称状态
k2,p=stats.normaltest(df['rating'])
print("p_value:",p)
# -----------------------------
# 中心极限定理模拟
# -----------------------------
sample_means=[]
for i in range(1000):
    sample = df['rating'].sample(n=100, replace=True)  #抽取30个代码 replace=True有放回抽样
    sample_means.append(sample.mean())
#---画图---
#pandas库series的转换更便于数据列表的计算和可视化
sample_means_series=pd.Series(sample_means)
#--画布--
plt.figure(figsize=(8,5))
plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7)
plt.title("Sampling Distribution of the Mean (n=100)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.axvline(np.mean(sample_means), color='red', linestyle='--',label="Means of Sample Mean")
plt.axvline(mean_rating,color='blue',linestyle='-',label='Mean_rating')
plt.legend()
plt.show()
#给电影评分做一个95%的置信区间
#标准误差
n=len(df["rating"])
SE=standard_rating/np.sqrt(n)
#标准误差有时候很小，建议是小数点后四位
print(f"标准误：{SE:.4f}")
#置信区间:真实平均评分有95%的概率落在这个区间
lower=mean_rating-1.96*SE
upper=mean_rating+1.96*SE
print(f"电影评分95%的置信区间：[{lower:.3f} , {upper:.3f}]")
#假设检验
# -----------------------------
# 假设检验：平均评分是否高于8.8
# -----------------------------
#t值含义：样本均值离假设均值有多少个“标准误差”那么远
n=len(df['rating'])
u0 = 8.8
t_statistic = (mean_rating - u0) / (standard_rating / np.sqrt(n))
print(f"t统计量: {t_statistic:.3f}")
# 计算p值：p = 如果原假设是真的，这种结果靠运气出现的概率
#p < 0.05  → 拒绝H0
#p ≥ 0.05 → 不拒绝H0
p_value = 1 - stats.t.cdf(t_statistic, df=n-1)
print(f"p值: {p_value:.5f}")
#已知p<0.001
'''
A one‑sample t‑test shows that the average rating of Douban Top250 movies 
(M ≈ 8.95) is significantly higher than 8.8 
(t ≈ 8.70, p < 0.001).
'''






