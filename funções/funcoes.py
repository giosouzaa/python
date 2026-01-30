#definindo uma função

def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo, {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Giovanna")
exibir_mensagem_2(nome="Gi")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

#retornando valores

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

#argumentos nomeados - chave = valor

def salvar_carro(marca, modelo, ano, placa):

    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat","modelo": "Palio", "ano": 1999, "placa":"ABC-1234"})


#*args e **kwargs - *args recebe argumentos separados por vírgula e **kwargs recebe argumentos no formato chave:valor

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta, 30 jan 26","Zen os Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

#PARÂMETROS ESPECIAIS
#
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# 

#parâmetros somente por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

#inválido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#parâmetros somente por nomes

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#inválido
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

#parâmetros híbridos

def criar_carro(modelo, ano, placa, /, marca,*, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#objetos de primeira classe

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é igual a {resultado}")

exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)

#escopo local e global

salario = 2000

def salario_bonus(bonus):
    global salario #variável global
    salario += bonus
    return salario

print(salario_bonus(600))