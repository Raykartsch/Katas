'''
Katas:
*Fix string case*

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
'''
def solve(string):
    mat = [0, 0] #upper, lower
    for x in range(len(string)):
        if string[x].isupper():
            mat[0] += 1
        else:
            mat[1] += 1   
    string_r = string.lower() if mat[0] < mat[1] else string.lower() if mat[0] == mat[1] else string.upper()
    return string_r

solve("CODe")