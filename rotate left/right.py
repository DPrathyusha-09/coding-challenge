element=list(map(int,input().split()))
direction=input().lower()
position=int(input())%len(element)
if direction=="left":
    rotated=element[position:]+element[:position]
elif direction=="right":
    rotated=element[-position:]+element[:-position]
else:
    rotated=element
print(rotated)