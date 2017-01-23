#Returns true if Number is Palindrome example: It returns true if number 9009
def IsPalindrome(number):
    # Convert number to list
    NumberAsList = [int(i) for i in str(number)]
    LengthOfList = len(NumberAsList)
    # Loop till half of the list of numbers
    for i in range(0, int(LengthOfList/2)):
        if (NumberAsList[i] != NumberAsList[LengthOfList-1-i]):
            return False
    return True
