
from ast import excepthandler


def collatz(num):
    if num % 2 == 0:
        return num//2
    elif num % 2 == 1:
        return 3*num+1
    else:
        print("error")


coll_series = []
try:
    num = int(input())
    while num != 1:
        print(collatz(num))
        num = collatz(num)
        coll_series.append(num)
except ValueError:
    print("valueEroor")

print(len(coll_series))
