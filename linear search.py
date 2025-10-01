def linear_search(data,target):
    try:
        return data.index(target)
    except:
        return -1
num=list(map(int,input().split()))
print(linear_search(num,45))