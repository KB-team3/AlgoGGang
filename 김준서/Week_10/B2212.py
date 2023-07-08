N = int(input())
K = int(input())
sensor = sorted(list(set(map(int,input().split(" ")))))
dist = sorted([sensor[i+1]-sensor[i] for i in range(len(sensor)-1)])
if K-1>=len(dist):
    print(0)
    exit()
for _ in range(K-1):
    dist.pop()
print(sum(dist))
