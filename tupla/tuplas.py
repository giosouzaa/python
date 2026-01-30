#tuplas são estruturas imutáveis

frutas = ("laranja", "pera", "uva",) #boa prática usar uma vírgula ao final da declaração de elementos da tupla para diferenciar de operadores em python
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4]) #ao passar uma lista, os valores serão convertidos em tuplas e eles se tornarão imutáveis
print(numeros)

pais = ("Brasil",)
print(pais)

#acesso aos elementos da tupla

print(frutas[0])
print(frutas[2])

#índices negativos

print(frutas[-1])
print(frutas[-3])

#tuplas aninhadas/matrizes

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#fatiamento

tupla = ("p","y","t","h","o","n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])


#iterar tuplas

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)


#enumerate


for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")