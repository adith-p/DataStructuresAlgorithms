""" 
Problem statement
Given an array 'arr' containing 'n' elements, rotate this array left once and return it.



Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.



Example:
Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.

https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278

"""

def rotateArray(arr: list, n: int) -> list:
    
    temp = arr[0]
    del arr[0]
    arr.append(temp)

    return arr
def addOneToNumber(arr):
    digit  = 0

    for i in arr:
        digit += i
        digit *= 10
    
    digit //= 10
    digit += 1
    arr.clear()
    for i in str(digit):
        arr.append(int(i))

    return arr
addOneToNumber([0,2])