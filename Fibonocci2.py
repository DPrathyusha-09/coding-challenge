def Fibonocci(num):
    a,b=0,1
    if num==1:
        print("null")
    elif num==2:
        print(a)
        print(b)
    elif num>2:
        print(a)
        print(b)
    for i in range(num-2):
        c=a+b
        a,b=b,c
        print(c)
num=Fibonocci(int(input()))
