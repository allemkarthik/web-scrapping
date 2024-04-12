import requests
from bs4 import BeautifulSoup
import pandas as pd
response=requests.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_7bb45b72-b83a-4af2-be2c-591ce41a0d72_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_='_4rR01T')
names_list=[]
for i in names[0:20]:
    n=i.get_text()
    names_list.append(n)
print(names_list)

print("-"*150)
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price_list=[]
for i in price[0:20]:
    n=i.get_text()
    price_list.append(n)
print(price_list)


print("-"*150)
rating=soup.find_all('div',class_="_3LWZlK")
rating_list=[]
for i in rating[0:20]:
    n=i.get_text()
    rating_list.append(n)
print(rating_list)

print("-"*150)
image=soup.find_all('img',class_="_396cs4")
image_list=[]
for i in image[0:20]:
    n=i['src']
    image_list.append(n)
print(image_list)

print("-"*150)
link=soup.find_all('a',class_="_1fQZEK")
link_list=[]
for i in link[0:20]:
    n="https://www.flipkart.com"+i['href']
    link_list.append(n)
print(link_list)

df=pd.DataFrame()
df['names']=names_list
df['price']=price_list
df['rating']=rating_list
df['images']=image_list
df['links']=link_list

df.to_csv('laptops.csv')