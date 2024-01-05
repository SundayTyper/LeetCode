"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""

### Psudo logic

# copy/define conversion dictionary
# convert roman numeral string to an array
# read array and begin conversion as per dictionary
# add checks for subtraction numerals e.g. IV = 5-1 = 4

class Solution:
    def romanToInt(self, s: str) -> int:
        
        numeralKey = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        #Convert string s into an array
        num = [i for i in s]
        answer = 0
        
        #read array from left to right, select one digit and the next digit
        j = 0
        while j < len(num):
            
            digit_current = num[j]
            
            if j < (len(num) -1):
                digit_next = num[j+1]
            
            #determine if numeral is to be added or subtracted
                if numeralKey[digit_current] >= numeralKey[digit_next]:
                    answer += numeralKey[digit_current]
            
                else:
                    answer -= numeralKey[digit_current]
            else:
                answer += numeralKey[digit_current]

            j += 1
                    
        return answer