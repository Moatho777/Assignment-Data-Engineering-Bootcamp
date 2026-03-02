from bs4 import BeautifulSoup
import requests
import pandas as pd

url = ("https://results.su.edu.ye/results/search?q=search&year=aHk5TlpxYVZlQkpCdGRFd1A1cThNUT09&for_high_studies=0"
       "&faculty=ZHE5UjBRN3hPWmJrRW1od3pCQ1EvRmhKckZXc1hURkRHWTBicmlCTFFiWT0&major=SUg1SmZhVEtwbi82MlBrMFEwdW5aUT09"
       "&system=cGF2S2t3UkNtemdzT3ZGbVlSSzVxZz09&gendar=0")

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

cols = soup.find_all('th', class_='small text-center')

text_col = [col.text.strip() for col in cols]
print(text_col)

df = pd.DataFrame(columns=text_col)

rows = soup.find_all('tr', class_=['result-row limegreen','result-row orangered'])
for row in rows:
    row_data = row.find_all('td')
    row_data = [data.text.strip() for data in row_data]
    print(row_data)
    length = len(df)
    df.loc[length] = row_data

raw_data = df.to_csv('../data/raw_data.csv', index=False)


# text_row = [row.text.strip() for row in rows]
# print(rows)
