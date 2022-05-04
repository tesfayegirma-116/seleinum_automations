stringg='https://www.facebook.com/Sadcasm/posts/2518476255210934'
page=''
count=0
for val in stringg:
    page = page+val
    if "/" == val:
        count+=1
        
        if count == 4:
            break


print(page)
        
           
