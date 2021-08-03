'''Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''
def decoding_roman_numbers(decode_text):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    total = cont = 0
    while cont < len(decode_text):  
        value = roman_numbers.get(decode_text[cont])
        if cont < len(decode_text) - 1:
            next_value = roman_numbers.get(decode_text[cont + 1])
        else:
            next_value = 0
        if value < next_value:
            next_value = next_value - value
            total += next_value
            decode_text = decode_text[:cont] + decode_text[cont+2:]
        else:
            total += value      
            cont += 1           
    return total

decoding_roman_numbers('CMLXXXIV')