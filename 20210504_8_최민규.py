#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    age=int(input('나이를 입력하세요:'))
except:
    print('입력이 정확하지 않습니다')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다')
        


# In[2]:


try:
    age=int(input('나이를 입력하세요:'))
except:
    print('입력이 정확하지 않습니다')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다')
        


# In[7]:


class MyError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# In[10]:


say_nick("천사")


# In[11]:


import math


# In[13]:


math.sin(1)


# In[14]:


math.tan(1)


# In[15]:


from math import sin, tan


# In[16]:


sin(1)


# In[17]:


from math import *


# In[18]:


cos(1)


# In[21]:


import math as m


# In[22]:


m.sin(1)


# In[23]:


import random
print("# random 모듈")

print("- random():", random.random())
print("- uniform(10, 20):", random.uniform(10, 20))
print("- randrange(10):", random.randrange(10))
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))


# In[24]:


print("- sample(range(1, 45), k=6):", random.sample(range(1, 45), k=6))


# In[25]:


import sys
print(sys.argv)


# In[31]:


print("getwindowsversion:()", sys.getwindowsversion())


# In[29]:


print("copyright:", sys.copyright)


# In[32]:


print("version:", sys.version)


# In[33]:


sys.exit()


# In[34]:


import os
print("현재 운영체재:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())


# In[35]:


os.mkdir("hello")
os.rmdir("hello")


# In[36]:


with open("origitnal.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")


# In[37]:


os.remove("new.txt")


# In[38]:


os.system("dir")


# In[40]:


import datetime
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()


# In[46]:


print("# 시간을 포멧에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,            now.month,            now.day,            now.hour,            now.minute,            now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()


# In[49]:


from urllib import request
target = request.urlopen("https://google.com")
output = target.read()
print(output)


# In[50]:


get_ipython().system('pip install beautifulsoup4')


# In[51]:


from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()
    


# In[52]:


get_ipython().system('pip install flask')


# In[53]:


from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


# In[ ]:


set FLASK_APP=

