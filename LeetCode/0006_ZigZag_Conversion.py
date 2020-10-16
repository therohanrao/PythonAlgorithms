'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1 or len(s) < numRows:
            return s
        newstr = ""
        for i in range(numRows):
            i_2 = i
            newstr += s[i]
            while True:
                if i != 0 and i != numRows - 1 and i_2 + 2*numRows - 2 - 2*i < len(s):
                    newstr += s[i_2 + 2*numRows - 2 - 2*i]
                if i_2 + 2*numRows - 2 >= len(s):
                    break
                newstr += s[i_2 + 2*numRows - 2]
                i_2 += 2*numRows - 2
        return newstr