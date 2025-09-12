items=['a','a','a','c']
count={}
for ele in items:
    if ele in count:
        count[ele]+=1
    else:
        count[ele]=1
print(count)