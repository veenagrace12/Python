import pandas as pd
import requests
from bs4 import BeautifulSoup

responce=requests.get('https://www.bikedekho.com/new-bikes')
print(responce)
soup=BeautifulSoup(responce.content,'html.parser')
print(soup.prettify())


'''
<Response [403]>
<html>
 <head>
  <title>       
   Access Denied
  </title>      
 </head>        
 <body>
  <h1>
   Access Denied
  </h1>
  You don't have permission to access "http://www.bikedekho.com/new-bikes" on this server.
  <p>
   Reference #18.6361ab8.1645273796.1952dd89
  </p>
 </body>
</html>
'''

