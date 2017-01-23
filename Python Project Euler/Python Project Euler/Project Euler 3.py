"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
import math
import PrimeNumber 
Number = 600851475143
# Largest prime factor has to less than twice the square root of Number 600851475143
value = int(math.sqrt(Number) * 2)
# For loop from largest number to 1 in descending order
for i in range(value,1,-1):
    # Check if number is divisible by i; if true check if number is prime
    if (Number % i == 0) and PrimeNumber.IsPrime(i):
        print (i)
        break