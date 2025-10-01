arr=list(map(int,input().split()))
min_val=arr[0]
max_val=arr[0]
for num in arr[1:]:
    if num<min_val:
        min_val=num
    elif num>max_val:
        max_val=num
print(f"Max:{max_val},Min:{min_val}")