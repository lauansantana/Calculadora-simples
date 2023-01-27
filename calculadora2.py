#Funçoes
def linha():
    print('_'*46)

def adicao():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1+n2))

def subtracao():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1-n2))

def multiplicacao():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1*n2))

def divisao():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1/n2))

def porcentagem():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo Número: "))
    print("Total: {}%".format(n1*n2/100))

def sair():
    exit

#Programa Principal

linha()
entrada = "| Olá! Insira a operação matemática desejada |\n"
entrada += "| Soma                     ->   [+]          |\n"
entrada += "| Subtração                ->   [-]          |\n"
entrada += "| Multiplicação            ->   [*]          |\n"
entrada += "| Divisão                  ->   [/]          |\n"
entrada += "| Porcentagem              ->   [%]          |\n"
entrada += "| Sair                     ->   [S]          |\n"


operacao = input(entrada)

if operacao == '+':
    adicao()
elif operacao == '-':
    subtracao()
elif operacao == '*':
    multiplicacao()
elif operacao == '/':
    divisao()
elif operacao == '%':
    porcentagem()
elif operacao == 's'or'S':
    sair()
else:
    linha()
    print("Entrada Incorreta")
    linha()
