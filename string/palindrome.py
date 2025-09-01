n=int(input())
reverse=int(str(n)[::-1])
if n==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")