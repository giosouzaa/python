# Desafio: A Aventura do Explorador
#Entrada
#Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade 
#de passos que o explorador deve dar na floresta.

#Saída
#O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de 
#repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância 
#percorrida até o momento.

#//TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#// Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#// Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.


quantidade_passos = int(input("Insira a quantidade de passos que o explorador deve dar na floresta:\n"))

if quantidade_passos > 0:
  for passo in range(quantidade_passos):
    if passo +1 == 1:
      print(f"Explorador: {passo +1} passo")
    else:
      print(f"Explorador: {passo +1} passos")
elif quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")
else:
  print("Número de passos inválido.")