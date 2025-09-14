n=int(input())
p=n
sum=0
while(n>0):
    rem=n%10
    sum+=rem
    n=n//10
if(p%sum==0):
    print("Harshad num")

