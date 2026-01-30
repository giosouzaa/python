frutas = [] #criação de lista vazia
print(frutas) 

frutas = ["laranja", "maca", "uva"]
print(frutas)

letras = list("python") #separação de cada elemento de modo iterável
print(letras) 

numeros = list(range(10))
print(numeros)

carro = ["Ferrari","F8", 4200000, 2020, 2900, "São Paulo", True] #lista mista
print(carro)

#selecionando elementos de uma lista

print(frutas[0])
print(frutas[2])

#índices negativos - leitura da direita para a esquerda a partir de -1

print(frutas[-1])
print(frutas[-3])

#listas aninhadas/matrizes

matriz = [
        [1,"a",2],
        ["b", 3, 4],
        [6,5,"c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#fatiamento [inicial:final:step]

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

#iterar listas

carros = ["gol", "celta","palio"]

for carro in carros:
    print(carro)

#função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

#compreensão de listas - para filtrar ou modificar uma lista já existente

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)


pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)

quadrado = []
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)