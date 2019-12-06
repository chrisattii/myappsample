


Question 1
# usr/bin/python3
def is_prime():
    num = int(input("Enter integer to be checked here: "))
    
    if num > 1:
        for d in range(2, num):
           if (num % d) == 0:
               print("False")
               return None
        else:
            print("True")
            return None
    else : 
        print("False")
        return None 


is_prime()



