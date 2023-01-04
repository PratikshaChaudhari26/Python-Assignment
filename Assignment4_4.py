#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
#Map function will calculate its square. Reduce will return addition of all that numbers.
def CheckEven(No):
    return (No % 2 == 0)

def Doubles(No):
    return No*2

def Sum(A,B):
    return A+B

def reduceX(Helper_Function,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)

    return Ans

def filterX(Helper_Function, Data):
    arr = []
    for No in Data:
        if(Helper_Function(No) == True):
            arr.append(No)
    
    return Result

def mapX(Helper_Function, Data):
    arr = []
    for No in Data:
        Value = Helper_Function(No)
        arr.append(Value)

    return Result    

def main():
    print("Enter number of elements you want to enter : ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)

    print("Data after filter is : ",Data_Filter)

    Data_Map = mapX(Doubles, Data_Filter)

    print("Data after map is : ",Data_Map)
    
    Output = reduceX(Sum,Data_Map)

    print("Result after reduce is : ",Output)

if __name__ == "__main__":
    main()