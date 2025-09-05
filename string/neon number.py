n=int(input())
s=n*n
p=((s%10) + (s//10)%10 + (s//100)%10)
if n==p:
    print(n,"neon number")
else:
    print(n,"is not a neon number")
