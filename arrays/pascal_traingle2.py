'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Could you optimize your algorithm to use only O(rowIndex) extra space?

return the row values of the integer recieved(given)

First of all, we initialize row = [1], because the frist row in the triangle row is 1.

After that, we add [0] to the first position and the last position respectively.

Now we have

[0,1] (order of left number)
[1,0] (order of right number)

Pascal Triangle I, I created [0,1,0] for the first row.

order of left number is the first two numbers [0,1] in [0,1,0]
order of right number is the last two numbers [1,0] in [0,1,0]
'''

def getRow(rowIndex):
    row = [1]

    for _ in range(rowIndex):
        row = [left + right for left, right in zip([0]+row, row+[0])]
        
    return row 


print(getRow(3))
