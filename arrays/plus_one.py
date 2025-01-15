""" 
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

"""

# from ast import List


def plusOne(digits: int):
    pass 
    # loop for the last value or MSV
    for i in range(len(digits) - 1, -1, -1):
        # check if sum of 1 and l=last value (9) is zero
        if digits[i] != 0:
            digits[i] += 1
            return digits
        
        # else digits[i] = 0
        digits[i] = 0

        if i == 0:
            return [1] + digits
        

digits = [1,2,9]

x = plusOne(digits)
print(x)
