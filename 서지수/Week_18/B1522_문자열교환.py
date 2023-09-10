arr=input()
a=arr.count('a')

arr+=arr[0:a-1]
minimum=float('inf')

for i in range(len(arr)-(a-1)):
    minimum=min(minimum, arr[i:i+a].count('b'))

print(minimum)