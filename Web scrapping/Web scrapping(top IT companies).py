import pandas as pd
import requests
from bs4 import BeautifulSoup

responce=requests.get('https://www.goodfirms.co/it-services/india')
print(responce)
soup=BeautifulSoup(responce.content,'html.parser')
#print(soup.prettify())

names=soup.select('h3')

name=[]
for i in names:
    name.append(i.get_text())
#print(name)    

ratings=soup.find_all('span',class_="listinv_review_label")

rating=[]
for i in ratings:
    rating.append(i.get_text())
#print(rating)

services=soup.find_all('div',class_="circle-progress-value")

service=[]
for i in services:
    service.append(i.get_text())
#print(service)


founded=soup.find_all('div',class_="firm-founded")
link=[]
for i in founded:
    link.append(i.get_text())
#print(link)    

employees=soup.find_all('div',class_="firm-employees")
loc=[]
for i in employees:
    loc.append(i.get_text())
#print(loc)   

   

df=pd.DataFrame()
df['company_Name']=name
df['rating']=rating
df['IT services']=service
df['founded']=link
df['Employees']=loc


print(df)
df.to_csv('Top 50 IT companies_data.csv')





