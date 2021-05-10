def getTotalPage(m,n):
    if m % n == 0:
        page =  m//10 
    else: 
        page = m //10 + 1
    return page

print(getTotalpage(5,10))
print(getTotalpage(15,10))
print(getTotalpage(30,10))

