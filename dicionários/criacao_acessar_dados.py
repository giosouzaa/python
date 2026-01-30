#{key:value}

pessoa = {"nome": "Giovanna", "idade": 25}
print(pessoa)

pessoa = dict(nome="Giovanna", idade=25)
print(pessoa)

pessoa["telefone"] = "4002-8922" #adiciona uma nova chave a um dicionários pré-existente
print(pessoa)

#acessar os dados

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#sobrescrevendo os valores

pessoa["nome"]="Maria"
pessoa["idade"]=26
pessoa["telefone"]="9100-1091"
print(pessoa)

#dicionários aninhados/matrizes

contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 25, "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

print(contatos["giovanna@gmail.com"]["telefone"])

#iterar dicionários

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)