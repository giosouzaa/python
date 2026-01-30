#[].append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

#[].clear

lista.clear()

print(lista)

#[].copy

lista = [1, "Python", [40,30,20]]

l2 = lista.copy()

print(l2)
print(id(l2), id(lista)) #objetos diferentes, mesmo com o conteúdo copiado

#[].count - número de repetição de um termo na lista

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#[].extend - inclui novos termos, podendo concatenar duas listas

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#[].index - posição da primeira ocorrência de um determinado objeto

print(linguagens.index("java"))

print(linguagens.index("python"))

#[].pop - remove o último elemento que foi adicionado à lista (da direita para a esquerda)

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0)) #permite indicar o índice que se deseja remover

#[].remove - remove a primeira ocorrência do elemento indicado

linguagens = ["python", "js", "c","java", "csharp"]

linguagens.remove("c")

print(linguagens)

#[].reverse

linguagens = ["python", "js", "c","java", "csharp"]

linguagens.reverse()

print(linguagens)

#[].sort - ordena a lista

linguagens = ["python", "js", "c","java", "csharp"]
linguagens.sort() #ordem alfabética A-Z
print(linguagens)

linguagens = ["python", "js", "c","java", "csharp"]
linguagens.sort(reverse=True) #ordem alfabética Z-A
print(linguagens)

linguagens = ["python", "js", "c","java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #ordem de tamanho menor-maior
print(linguagens)

linguagens = ["python", "js", "c","java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse = True) #ordem de tamanho maior-menor
print(linguagens)

#len - mostra o número de termos/tamanho da lista

linguagens = ["python", "js", "c","java", "csharp"]

print(len(linguagens))

#sorted - também ordena a lista como o sort, mas é uma função

print(sorted(linguagens))

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))