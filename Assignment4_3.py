#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70
 #and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
 
 
 from functools import reduce
 
def main():
    print("Enter number of elements you want to enter : ")
    iSize = int(input())
    
    arr = []
    print("Please enter the data ")
    for iCnt in range(0,iSize):
        Value = int(input())
        arr.append(Value)
    
        print("Data is",arr)
    
    greatnum = list(filter(lambda value: ((value >= 70) & (value <= 90)), arr ))
    print("filter",greatnum)
    
    brr = list(map(lambda value: value + 10, greatnum))
    print("Map", brr)
    ans = 1
    drr = reduce(lambda value, value1: value * value1, brr)
    print("Reduce", drr)
   
    
    


if __name__ == "__main__":
   main()
   