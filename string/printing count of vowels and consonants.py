n=input()
vcount=0
ccount=0
for char in n:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vcount+=1
        else:
            ccount+=1
print("Vowels: ",vcount)
print("Consonants: ",ccount)
