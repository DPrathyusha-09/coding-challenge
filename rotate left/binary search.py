pos=-1
def serach(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
    
list=[2,24,13,45,67]
list.sort()
n=int(input())
if serach(list,n):
    print("Found at",pos+1)
else:
    print("Notfound")