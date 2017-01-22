"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""
# Intialize sum variable to zero
sum = 0
# Loop from 0 to 999
for i in range (1000):
    # Check if number is multiples of 3 or 5
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print (sum)