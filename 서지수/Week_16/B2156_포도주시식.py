import sys

input=sys.stdin.readline

n=int(input())

arr=[0]*10000
for i in range(n):
  arr[i]=int(input())

new_arr=[0]*10000
new_arr[0]=arr[0]
new_arr[1]=arr[0]+arr[1]
new_arr[2]=max(arr[2]+arr[0], arr[2]+arr[1], new_arr[1])

for i in range(3,n):
  new_arr[i]=max(arr[i]+new_arr[i-2], arr[i]+arr[i-1]+new_arr[i-3], new_arr[i-1])

print(max(new_arr))