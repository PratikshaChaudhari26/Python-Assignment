#Write a program which contains filter(), map() and reduce() in it. 
#Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers. Map function will multiply each number by 2. 
#Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions)...


import functools
from functools import *
from typing import List

from prime_module import *


def main():
    print("Filter Map Reduce")
    arr = list()
    num = input("Enter the number of element you want:::")
    for i in range(0, int(num)):
        n = input("num:")
        arr.append(n)

    filterarr = list(filter(prime, arr))
    print("List of Filter", filterarr)
    maparr = list(map(lambda no: int(no) * 2, filterarr))
    print("List of Map", maparr)

    # reducearray = reduce(pr, maparr)
    # reducearray=reduce(functools.partial(Max, some_var=True), crr)
    reducearray = reduce(Max, maparr)
    # reducearray=reduce(lambda max, current: max if (max > current) else current, crr)
    print("Reduce {} is".format(reducearray))


if __name__ == "__main__":
    main()