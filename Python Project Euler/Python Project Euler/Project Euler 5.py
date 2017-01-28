"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import PrimeNumber
import math
ListOfPrimes = []
NumberDivisibleTill = 20
result = 1
# Loop from 2 to 20 and find list of prime numbers
for i in range(2,(NumberDivisibleTill+1)):
    if (PrimeNumber.IsPrime(i)):
        ListOfPrimes.append(i)
# Finding smallest positive number that is divisible till 20
for i in ListOfPrimes:
    a = math.floor(math.log(NumberDivisibleTill)/math.log(i))
    result = result * math.pow(i,a)
print(result)
