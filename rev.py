arr=list(map(int,input().split()))
rev_list=[]
for i in range(len(arr)-1,-1,-1):
    rev_list.append(arr[i])
print(rev_list)
