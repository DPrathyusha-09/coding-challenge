text=input()
vowels="aeiouAEIOU"
result=""
for char in text:
    if char in vowels:
        result+=char
print(result)
