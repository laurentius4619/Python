#!/usr/bin/env python
# coding: utf-8

# In[3]:


def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")
hello()


# In[ ]:




