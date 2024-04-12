import requests
from bs4 import BeautifulSoup
import pandas as pd

response=requests.get("https://www.flipkart.com/tyy/4io/~cs-q7uz6kwr4y/pr?sid=tyy%2C4io&collection-tab-name=iphone+15&param=6762&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJpbmNsIG9mIG9mZmVycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbImlQaG9uZSAxNSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUQUdQTk1aQTVQVTUiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

print("*"*50)

#if your data want to be in sturctured format
#names of phones
names=soup.find_all("div",class_="_4rR01T")
names_list=[]
for i in names:
    d=i.get_text()
    names_list.append(d)
print(names_list)

print("*"*100)

#price list of phones
price=soup.find_all("div",class_="_30jeq3 _1_WHN1")
price_list=[]

for i in price:
    d=i.get_text()
    price_list.append(d)
print(price_list)

print("*"*100)

#rating of phones
rating=soup.find_all("div",class_="_3LWZlK")
rating_list=[]

for i in rating:
    d=i.get_text()
    rating_list.append(d)
print(rating_list)

print("*"*100)

#images of phones
image=soup.find_all("img",class_="_396cs4")
image_list=[]

for i in image:
    d=i['src']
    image_list.append(d)
print(image_list)

print("*"*100)

#links
links=soup.find_all("a",class_="_1fQZEK")
links_list=[]

for i in links:
    d="https://www.flipcart.com"+i['href']
    links_list.append(d)
print(links_list)

df=pd.DataFrame()
df['names']=names_list
df['price']=price_list
df['rating']=rating_list
df['images']=image_list
df['links']=links_list
df.to_csv("flipkartmobiles.csv")