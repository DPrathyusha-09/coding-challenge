n=int(input())
if n<0:
    sign=-1
    n=abs(n)
else:
    sign=1
rev=str(n)[::-1]
r=int(rev)
result=int(rev)
print(result)
