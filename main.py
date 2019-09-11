from math import ceil as roundUP
textoInit = 'diego garcia'
chave = 'arroz'

texto = textoInit.replace(' ', '')
chaveC = (chave * roundUP(len(texto) / len(chave)))[:len(texto)]
final = ''

alfabetoLetras = 'abcdefghijklmnopqrstuvwxyz'
def crip(a, b):
    a = (alfabetoLetras.find(a))
    b = (alfabetoLetras.find(b))
    return alfabetoLetras[a+b-26] if a + b >= 26 else alfabetoLetras[a+b]

menor = 0
for num in range(len(textoInit)):
    if textoInit[num] == ' ':
        final += ' '
        menor += 1
    else:
        final += crip(texto[num - menor], chaveC[num - menor])

print(final)