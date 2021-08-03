#Fazer usando set!
from collections import Counter
def is_pangram(s):
    s = sorted(''.join(st for st in s if st.isalpha()).lower())
    res = Counter(s)
    return True if len(res.keys()) == 26 else False

pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram(pangram)

lista = [[1,5],[10, 20],[1, 6],[16, 19],[5, 11]]
lista.sort()
print(lista)
