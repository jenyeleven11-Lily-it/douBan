import pandas as pd

#清洗数据NBSP，以及前后空格
origin_folder=r"D:\Studywork\studySpace\douBan\data\raw\douban_top250_raw.csv"
object_folder=r"D:\Studywork\studySpace\douBan\data\proceed\douban_top250_proceed.csv"

df=pd.read_csv(origin_folder)
df['title']=df['title'].str.strip()
df['title']=df['title'].str.replace('\u00A0','',regex=False)
#中英文分开,expand用于多列表
split_cols = df['title'].str.split('/', expand=True)
df['cn_title']=split_cols[0].str.strip()
df['en_title']=split_cols.iloc[:,-1].str.strip()
#.shape → Pandas 的固定属性（不是方法，所以后面没有括号！！
#清洗original_title列，df['original_title'].fillna('') 的作用是：把列中所有的 缺失值 NaN 替换成「空字符串」（Python 里的 ''）
df['original_title']=df['original_title'].fillna('')
temp=df['original_title'].str.split('/', expand=True)
df['original_title']=temp.iloc[:,-1]
df['original_title']=df['original_title'].str.strip()
print(df[['cn_title', 'en_title', 'original_title']].head())
df.to_csv(object_folder,index=False)


