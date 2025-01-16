''' 
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

This problem can be solved using 3 solutions:
Recursions (base-case recursion), combinatorial/formula based approach and dynamic programing approach
'''

# Recursion approach
# Reason: Good time complexity but not memory efficient because it uses 2D arrays
# Intuition: In Pascal's triangle, each element is the sum of the two elements directly above it. 

from typing import List


def generate(numRows: int) -> List[List[int]]:
        # Base case: If numRows is 1, return [[1]].
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

    # Recursively generate the triangle for numRows - 1.
        prevRows = generate(numRows - 1)
        newRow = [1] * numRows 

    # Calculate the current row by summing adjacent elements from the previous row.

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows

print(generate(numRows=5))


# Using Combinatorial Formula
# Use the binomial coefficient formula C(n, k) to calculate each element.
# Build the triangle row by row using the formula.


def generatePascalForm(numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        
        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)
        
        return result 

print(generatePascalForm(numRows=5))


# Dynamic Programming with 1D Array:
# Initialize a 1D array to store the current row.
# Iterate through numRows and update the array for each row.

def generateDynamic(numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prev_rows = generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows 
print(generateDynamic(numRows=5))