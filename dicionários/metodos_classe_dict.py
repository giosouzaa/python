#{}.clear

contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 25, "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

contatos.clear()
print(contatos)

#{}.copy

contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 25, "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

copia = contatos.copy()
print(copia)

#{}.fromkeys 

print(dict.fromkeys(["nome", "telefone"])) #cria chaves vazias

#usar dict.fromkeys para criar dicionários no ato do método

print(dict.fromkeys(["nome", "telefone"], "vazio")) #cria chaves com um valor padrão

#{}.get - acessar dados

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

#contatos["chave"] #keyerror

print(contatos.get("chave"))
print(contatos.get("chave",{})) #caso a chave nao seja localizada, apresentar valor padrão vazio
print(contatos.get("giovanna@gmail.com", {}))

#items

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

print(contatos.items())


#keys

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

print(contatos.keys())

#pop

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

print(contatos.pop("giovanna@gmail.com"))
print(contatos.pop("giovanna@gmail.com",{})) #retorna valor padrão caso a chave não seja encontrada

#popitem

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

#print(contatos.pop())
#print(contatos.pop()) #KeyError

#setdefault

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

print(contatos.setdefault("nome","Guilherme"))
print(contatos)

print(contatos.setdefault("idade",25))
print(contatos)


#update

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"}
}

contatos.update({"giovanna@gmail.com":{"nome": "Gi"}})
print(contatos)

contatos.update({"giovanna@gmail.com":{"nome": "Gi", "telefone": "9018-0919"}})
print(contatos)

#values

contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 25, "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

print(contatos.values())

#in

contatos = {
    "giovanna@gmail.com": {"nome": "Giovanna", "idade": 25, "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

print("giovanna@gmail.com" in contatos)
print("idade" in contatos["guilherme@gmail.com"])
print("gi@gmail.com" in contatos)
print("telefone" in contatos["giovanna@gmail.com"])

#del

contatos = {
    "giovanna@gmail.com" : {"nome": "giovanna", "telefone": "4002-8922"},
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 26, "telefone": "4968-8665"},
}

del contatos["giovanna@gmail.com"]["telefone"]
print(contatos)

del contatos["guilherme@gmail.com"]
print(contatos)
