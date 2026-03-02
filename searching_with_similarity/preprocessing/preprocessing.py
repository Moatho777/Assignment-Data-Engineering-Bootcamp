import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw_data.csv')
num_feature = ['الترتيب في كشف النتيجة','رقم دخولالاختبار','رقم التنسيق']
dobule_feature = ['معدلالثانوية','مجموع درجاتالمواد','النسبة من  الثانوية 30%','النسبة من  الاختبار 70%','نتيجةالمفاضلة']

df[num_feature] = df[num_feature].astype(int)
df[dobule_feature] = df[dobule_feature].astype(float)


processed_data = df.to_csv('../data/processed_data.csv', index=False)

print(df['رقم دخولالاختبار'])
