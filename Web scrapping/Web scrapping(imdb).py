
import pandas as pd
import requests
from bs4 import BeautifulSoup

responce=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# print(responce)  # 200
soup=BeautifulSoup(responce.content,'html.parser')
#print(soup.prettify())

names=soup.select('td.titleColumn a')

name=[]
for i in names:
    #print(i.get_text())
    name.append(i.get_text()) 


year=soup.find_all('span',class_="secondaryInfo")

yr=[]
for i in year:
    #print(i.get_text())
    yr.append(i.get_text())


ratings=soup.find_all('strong')

rating=[]
for i in ratings:
    #print(i.get_text())
    rating.append(i.get_text())  
 
images=soup.find_all('img')

imgs=[]
for i in images:
    #print(i.get_text())
    imgs.append(i['src'])


links=soup.select('td.titleColumn a')

link=[]
for i in links:
    #print(i)
    url = 'https://www.imdb.com'
    #print(i['href'])
    link.append(url+i['href'])
# links=soup.select('td.tltleColumn a')

# link=[]
# for i in links:
#     #print(i['href'])
#     url = 'https://www.imdb.com'
#     link.append(url+i['href'])
df=pd.DataFrame()
df['Movie_Name']=name
df['Year']=yr
df['rating']=rating
df['Images']=imgs
df['Links']=link
print(df)
df.to_csv('IMDb_Movies_Data.csv')