#Write a program which contains one lambda function which accepts two parameters and return its multiplication.


def main():
    print("Enter first number")
    No1 = int(input())
    
    print("Enter second number")
    No2 = int(input())
    
    Multi = lambda No1,No2 : No1*No2
    
    Ans = Multi(No1,No2)
    print("Multiplication of number is",Ans)


if __name__ == "__main__":
   main()
   