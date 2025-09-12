st=input().split()
new_list=[]
for word in st:
    new_list.append(word[::-1])
output=" ".join(new_list)
print(output)
