'''Gerar o fibonacci enquanto verifica se a multiplicação é igual ao produto do atual com o numero seguinte'''

#Melhorar e refinar o codiguin!
def productFib(limit):
    fib_seq = [0, 1]
    x = prod = 0
    while prod < limit:
        prod = fib_seq[x] * fib_seq[x + 1]
        Fn = fib_seq[x] + fib_seq[x + 1]
        fib_seq.append(Fn)
        x += 1
    return [fib_seq[x - 1], fib_seq[x], prod == limit]
print(productFib(0))
