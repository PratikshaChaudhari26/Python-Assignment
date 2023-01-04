#Write a program which contains one class named as Arithmetic.
#Arithmetic class contains three instance variables as Value1, Value2.
#Inside init method initialise all instance variables to 0.
#There are three instance methods inside class as Accept(), Addition(), Subtraction(),
#Multiplication(), Division(). Accept method will accept value of Value1 and Value2 from user. 
#Addition() method will perform addition of Value1,Value2 and return result. 
#Subtraction() method will perform subtraction of Value1,Value2 and return result.
 #Multiplication() method will perform multiplication of Value1,Value2 and return result. 
 #Division() method will perform division of Value1,Value2 and return result. 
 #After designing the above class call all instance methods by creating multiple objects.
 
 
 class Arithmetic:
 
    def __init__(self, Value1, Value2)
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self)        
        print("Enter your first Value  : ")
        self.Value1 = input()

        print("Enter your second Value : ")
        self.Value2 = int(input())
    
    
    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans 

    def Substraction(self):
        Ans = self.Value1 - self.Value2
        return Ans
        
    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans  

    def Division(self):
        Ans = self.Value1 / self.Value2
        return Ans        
        
        
    def main():

    obj1.Arithmetic()
    obj2.Arithmetic()
    
    obj1.Accept()
    obj2.Accept()
    
    obj1.Addition()
    obj2.Addition()
    
    obj1.Substraction()
    obj2.Substraction()

    obj1.Multiplication()
    obj2.Multiplication()
    
    obj1.Division()
    obj2.Division()

if __name__ == "main":
   main()    