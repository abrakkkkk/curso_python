# FORMATAÇÃO COM FORMAT

a = 'A'
b = 'B'
c = 1.1
string = 'a = {nome1}\nb = {nome2}\nc = {nome3:.2f}'
formato = string.format(
    nome1=a, # parametro nomeado
    nome2=b, 
    nome3=c
)

print(formato)

frase = 'Este {comida} está {adjetivo}.'.format(
    comida = 'ovo', 
    adjetivo = 'absolutamente horrível'
)

print(frase)