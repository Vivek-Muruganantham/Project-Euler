#Returns true if the number is prime else false
import math
def IsPrime(number):
    # If number is 2, 3, 5 or 7, return IsPrime as true
    if(number == 2 or number == 3 or number == 5 or number == 7):
        return True
    # If number is divisible by 2,3,5 or 7, return IsPrime as False
    elif(number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0):
        return False
    else:
        # It is enough to check till square root of number
        N = int(math.sqrt(number))
        # Since we have verified above till 7 and we are checking only odd numbers
        for i in range(11,N,2):
            if (number % i == 0):
                return False
        return True