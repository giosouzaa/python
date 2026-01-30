#{}.union

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

#{}.intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

#{}.difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#{}.symmetric_difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b))

#{}.issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#{}.issuperset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#{}.isdisjoint - verifica se são conjuntos independetens, sem intersecções entre os conjuntos

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#{}.add

sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
    
sorteio.add(42)
print(sorteio)
    
sorteio.add(25)
print(sorteio)

#{}.copy

s2 = sorteio.copy()
print(s2)

#{}.discard

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)
numeros.discard(1)
numeros.discard(45) #se o elemento não existe ele ignora
print(numeros)

#{}.pop - retira os primeiros elementos (esquerda para direita)

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.pop()
numeros.pop()
print(numeros)

#{}.remove

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.remove(0)
#numeros.remove(45) #se o elemento não existe ele apresenta erro

print(numeros)

#len

print(len(numeros))

#in - verifica se um elementos faz parte do conjunto

print(1 in numeros)
print(10 in numeros)