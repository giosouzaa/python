# Old Style % (unusual)

nome = "Giovanna"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo %s, tenho %d, sou %s e utilizo a linguagem de programação %s" % (nome, idade, profissao, linguagem))

# Método format

nome = "Giovanna"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo {}, tenho {}, sou {} e utilizo a linguagem de programação {}" .format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}, tenho {2}, sou {1} e utilizo a linguagem de programação {0}" .format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}, tenho {idade}, sou {profissao} e utilizo a linguagem de programação {linguagem}" .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#com uso de dicionário
pessoa = {"nome": "Giovanna", "idade": 25, "profissao": "Programadora", "linguagem": "Python"}
print("Olá, me chamo {nome}, tenho {idade}, sou {profissao} e utilizo a linguagem de programação {linguagem}" .format(**pessoa)) 

# f-string

nome = "Giovanna"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print(f"Olá, me chamo {nome}, tenho {idade}, sou {profissao} e utilizo a linguagem de programação {linguagem}")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

