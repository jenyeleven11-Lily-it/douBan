import pandas as pd
df = pd.read_csv(r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv")

high_score_movies=df[df['rating']>=9]
print("基础分析情况：")
#shape返回元组形式（行数，列数）
print(f"总电影数量：{df.shape[0]}部")
print(f"平均评分：{df['rating'].mean():.2f}")
print(f"评分大于9.5的有：")
print(f"{high_score_movies[['cn_title','rating']].to_string(index=False)}")
