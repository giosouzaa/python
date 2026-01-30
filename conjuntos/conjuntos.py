#set - elimina os elementos repetidos, pois, em conjuntos, os elementos não se repetem

print(set([1,2,3,1,3,4])) 

print(set("abacaxi"))

print(set(("palio","gol", "celta", "palio")))

linguagens = {"python", "java", "python"} #conjuntos também podem ser declarados com {}
print(linguagens)

#acessando os dados 

numeros = {1,2,3,2}

numeros = list(numeros) #converte o conjunto em uma lista para ser possível trabalhar com indexação

print(numeros)
print(numeros[0])

#iterar conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")