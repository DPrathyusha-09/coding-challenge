n=list(map(int,input().split()))
index=0
for i in range(len(n)):
    if n[i]!=0:
        n[index],n[i]=n[i],n[index]
        index+=1
print(n)
