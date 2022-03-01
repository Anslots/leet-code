'''
function findMax() takes in a list li
it should then return the maximum number in that list

Examples:
[1, 6, 12, 7] return 12
[2, 17, 8, 7] return 17
[1, 1, 1, 2, 1, 1] return 2
[-3, -4, -2] return -2
[-15, -13, -27] return -13
'''
def findMax(li):
    maxim = li[0]
    for i in li:
        if i > maxim:
            maxim = i
    return maxim


