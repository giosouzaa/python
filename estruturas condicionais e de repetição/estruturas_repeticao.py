
#FOR
# Utilizando um iterável

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


#RANGE
#range(stop) -> range object
#range(start, stop[,step]) -> range object

print(list(range(4)))

for numero in range(0,51, 5):
    print(numero, end=" ")
    
print("\n")

# Utilizando a função built-in range
# Receba um número do teclado e exiba os 2 números seguintes

a = int(input("Informe um número inteiro:"))
print(a)

for numero in range(0,2):
    a += 1
    print(a)

#WHILE

#Exemplo 1
opcao = -1

while opcao !=0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrato ...")

#Exemplo 2 - break

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

#Exemplo - for e continue

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")