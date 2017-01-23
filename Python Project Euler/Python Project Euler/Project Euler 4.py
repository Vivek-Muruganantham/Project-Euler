"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 � 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
import Palindrome
def LargestPalindromic():
    Number = 999 * 999
    # Loop from product of 999 * 999 till 100000
    for i in range(Number,100000-1):
        # Find palindrome number
        if (Palindrome.IsPalindrome(i)):
            for j in range(999,100,-1):
                # Find two 3 digit numbers
                if (i%j == 0 and len(str(i//j)) == 3):
                    print(i)
                    return

LargestPalindromic()