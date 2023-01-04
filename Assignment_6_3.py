#Write a program which contains one class named as Numbers.Arithmetic class contains one instance variables as Value.
#Inside init method initialise that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false. Factors() method will display all factors of instance variable. 
#SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required. 
#After designing the above class call all instance methods by creating multiple objects.


class Number:

    def __init__(self,value):
        self.value=value


    def ChkPrime(self):
        n=self.value
        if (n <= 1):
            return False
        if (n <= 3):
            return True

            # This is checked so that we can skip
            # middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0):
            return False

        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

    def ChkPerfect(self):
        n = self.value
        sum1 = 0
        for i in range(1, n):
            if (n % i == 0):
                sum1 = sum1 + i
        if (sum1 == n):
            return True
        else:
            return False
    def SumFactors(self):
        n = self.value
        sum1 = 0
        for i in range(1, n):
            if (n % i == 0):
                sum1 = sum1 + i
        return sum1

    def Factors(self):
        x=self.value
        lst=[]

        for i in range(1, x + 1):
            if x % i == 0:
                lst.append(i)
        return lst


def main():
    lst=[]
    num = int(input("enter number"))

    Obj1 =Number(num)

    print("numver is prime:{0}".format(Obj1.ChkPrime()))
    print("numver is perfect:{0}".format(Obj1.ChkPerfect()))
    print("sum of factors of number is :{0}".format(Obj1.SumFactors()))
    lst=Obj1.Factors()
    print("factors are :{0}".format(lst))

    num = int(input("enter number"))

    Obj2 = Number(num)
    print("numver is prime:{0}".format(Obj2.ChkPrime()))
    print("numver is perfect:{0}".format(Obj2.ChkPerfect()))
    print("sum of factors of number is :{0}".format(Obj2.SumFactors()))
    lst = Obj2.Factors()
    print("factors are :{0}".format(lst))





if __name__=="__main__":
    main()
