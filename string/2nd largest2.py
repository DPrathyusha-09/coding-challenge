arr=list(map(int,input().split()))
first=second=('-inf')
for i in arr:
    if i>first:
        second,first=first,i
    elif i>second and i!=first:
        second=i
if second!=float('-inf'):
    print(second)
else:
    print("not")