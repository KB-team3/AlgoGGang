import sys
import math
input=sys.stdin.readline

n=int(input())

def function(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        print(1)
        return
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            print(2)
            return
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                print(3)
                return
    print(4)

function(n)