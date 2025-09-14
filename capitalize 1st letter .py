sentence=input().split()
capitalized=[]
for ch in sentence:
    if ch:
        cap=ch[0].upper()+ch[1:]
        capitalized.append(cap)
capitalized_sen=' '.join(capitalized)
print(capitalized_sen)