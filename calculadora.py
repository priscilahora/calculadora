def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a/b

def multiplicacao(a, b):
    return a*b

operacao_escolhida = input("Indique a operação desejada (+, -, /, *): ")
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))

if operacao_escolhida == "+":
    resultado = adicao(numero_um, numero_dois)
elif operacao_escolhida == "-":
    resultado = subtracao(numero_um, numero_dois)
elif operacao_escolhida == "/":
    resultado = divisao(numero_um, numero_dois)
elif operacao_escolhida == "*":
    resultado = multiplicacao(numero_um, numero_dois)
else: 
    print("Essa operação é inválida!")

print("O resultado dessa operação é: ", resultado)