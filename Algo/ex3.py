arr = input().split(" ")
target = int(input())
ind = -1
for i in range(len(arr)):
    if int(arr[i]) >= target:
        break
    else:
        ind = i
print(ind + 1)
