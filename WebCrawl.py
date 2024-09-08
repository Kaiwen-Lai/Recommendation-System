#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests

url ='https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list?sortby=rating'
r=requests.get(url)
soup = BeautifulSoup(r.text , 'lxml')

item_list = soup.find('div',class_ ='item-list')
items = item_list.find_all('div',class_ ='restaurant-item')
print(len(items))

for index in range(5):
    item =items[index]
    title = item.find('a',class_='title-text')
    if title: print(title.text)
    address = item.find('div',class_ = 'address-row')
    if address: print(address.text)
    avg_price = item.find('div',class_ = 'avg-price').text[2:]
    if avg_price: print(avg_price)
    message = item.fin


# # 鍋類

# In[38]:


#鍋類
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E9%8D%8B%E9%A1%9E?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','嘉義縣','屏東縣','花蓮縣','南投縣']
county2 = ['台東縣','澎湖縣','金門縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('鍋類.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 日式

# In[39]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E6%97%A5%E5%BC%8F?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','嘉義縣','屏東縣','花蓮縣','南投縣','台東縣']
county2 = ['澎湖縣','金門縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('日式.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 燒烤

# In[40]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E7%87%92%E8%82%89?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','宜蘭縣','新竹市','新竹縣','嘉義市','屏東縣']
county2 = ['苗栗縣','彰化縣','雲林縣','基隆市','澎湖縣','金門縣','花蓮縣','南投縣','台東縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('燒烤.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 精緻高級

# In[42]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E7%B2%BE%E7%B7%BB%E9%AB%98%E7%B4%9A?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','屏東縣','花蓮縣','南投縣','台東縣']
county2 = ['嘉義縣','澎湖縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('精緻高級.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 早午餐

# In[44]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E6%97%A9%E5%8D%88%E9%A4%90?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','屏東縣','花蓮縣','南投縣','台東縣']
county2 = ['嘉義縣','澎湖縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('早午餐.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 甜點類

# In[45]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E7%94%9C%E9%BB%9E%E9%A1%9E?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','嘉義縣','屏東縣','花蓮縣','台東縣','澎湖縣','南投縣']
county2 = ['金門縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('甜點類.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 約會餐廳

# In[46]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E7%B4%84%E6%9C%83%E9%A4%90%E5%BB%B3%E9%A1%9E?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','屏東縣','台東縣','花蓮縣','南投縣']
county2 = ['嘉義縣','澎湖縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('約會餐廳.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 韓式

# In[47]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E9%9F%93%E5%BC%8F?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','新竹市','彰化縣','嘉義市']
county2 = ['嘉義縣','屏東縣','花蓮縣','南投縣','雲林縣','新竹縣','苗栗縣','基隆市','宜蘭縣','台東縣','澎湖縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('韓式.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 餐酒館/酒吧

# In[48]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E9%A4%90%E9%85%92%E9%A4%A8%2F%E9%85%92%E5%90%A7?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','台中市','台南市','高雄市']
county2 = ['桃園市','台東縣','澎湖縣','基隆市','宜蘭縣','新竹市','新竹縣','苗栗縣','彰化縣','雲林縣','嘉義市','屏東縣','花蓮縣','南投縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('餐酒館_酒吧.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# # 居酒屋

# In[49]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv,re,time

URL ='https://ifoodie.tw/explore/{}/list/%E5%B1%85%E9%85%92%E5%B1%8B?page={}'
ua = UserAgent()
headers = {'user-agent':ua.random}
county1 = ['台北市','新北市','桃園市','台中市','台南市','高雄市','宜蘭縣','新竹市','新竹縣']
county2 = ['苗栗縣','基隆市','台東縣','澎湖縣','彰化縣','雲林縣','嘉義市','嘉義縣','屏東縣','花蓮縣','南投縣']    #只有一頁
result=[['餐廳名稱','地址','均消','評分']]    

for co in county1:
    for page in range(1,100):
        url = URL.format(co,page)
        print('抓取： 第'+str(page)+'頁 網路資料中.....')
        r = requests.get(url,headers = headers)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            all_items =[]
            item_list = soup.find('div' , class_ = 'item-list')
            items = item_list.find_all('div' ,class_ = 'restaurant-item')
            for item in items:
                title = item.find('a',class_='title-text').text
                address = item.find('div',class_ = 'address-row').text
                avg_price = item.find('div',class_ = 'avg-price')
                if avg_price is None:
                    avg_price=''
                else:
                    avg_price = avg_price.text[2:]
                rating =item.find('div',class_='text')
                if rating is None:
                    rating = ''
                else:
                    rating = rating.text
                restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
                all_items.append(restaurant)
            result = result+all_items
            if soup.find('li',class_='next disabled') :
                print('{}完成！'.format(co))
                break
            print('等待五秒鐘...')
            time.sleep(3)
        else:
            print('HTTP請求錯誤...')

for co in county2:
    url = URL.format(co,1)
    print('抓取： 第1頁 網路資料中.....')
    r = requests.get(url,headers = headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'lxml')
        all_items =[]
        item_list = soup.find('div' , class_ = 'item-list')
        items = item_list.find_all('div' ,class_ = 'restaurant-item')
        for item in items:
            title = item.find('a',class_='title-text').text
            address = item.find('div',class_ = 'address-row').text
            avg_price = item.find('div',class_ = 'avg-price')
            if avg_price is None:
                 avg_price=''
            else:
                 avg_price = avg_price.text[2:]
            rating =item.find('div',class_='text')
            if rating is None:
                rating = ''
            else:
                rating = rating.text
            restaurant = [title.strip(),address.strip(),avg_price.strip(),rating.strip()]
            all_items.append(restaurant)
        result = result+all_items        
        print('{}完成！'.format(co))
        print('等待五秒鐘...')
        time.sleep(3)
    else:
        print('HTTP請求錯誤...')            
with open('居酒屋.csv','w+',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    for item in result:
        writer.writerow(item)
        


# In[ ]:




