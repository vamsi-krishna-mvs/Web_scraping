import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
  header={}
  url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

  source=requests.get(url)
  print(source.status_code)
except:
  print('error in the code')

soup=BeautifulSoup(source.content,'html.parser')

a=soup.find('tbody')

tr_tags=a.find_all('tr')

col_titles=tr_tags[0].find_all('th')
col_names=[]
for col in col_titles:
  col_names.append(col.text.strip())
#print(col_names)

df=pd.DataFrame(columns=col_names)
df
len(df)

for tr in tr_tags[1:]:
  row_data=[]
  for td in tr.find_all('td'):
    row_data.append(td.text.strip())
  df.loc[len(df)]=row_data
df

print(df)

df.to_excel(r'C:\Users\VAMSI\Desktop\companies.xlsx',index=False)