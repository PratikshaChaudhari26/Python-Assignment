


# Write a program which contains one lambda function which accepts one parameter and return power of two..

def main():
    print("Enter one number")
    No1 = int(input())
    
    Square = lambda No1 :  2 ** No1
    
    Ans = Square(No1)
    print("Value of power of two",Ans)


if __name__ == "__main__":
   main()
   