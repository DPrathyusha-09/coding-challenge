num1=int(input())
num2=int(input())
a=num1
b=num2
while b:
    a,b=b,a%b
gcd=a
lcm=(num1*num2)//gcd
print(gcd,lcm)
