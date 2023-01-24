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


#Programa Principal
linha()
entrada = "| Olá! Insira a operação matemática desejada |\n"
entrada += "| Soma                     ->   [+]          |\n"
entrada += "| Subtração                ->   [-]          |\n"
entrada += "| Multiplicação            ->   [*]          |\n"
entrada += "| Divisão                  ->   [/]          |\n"

operacao = input(entrada)

if operacao == '+':
    adicao()
elif operacao == '-':
    subtracao()
elif operacao == '*':
    multiplicacao()
elif operacao == '/':
    divisao()
else:
    linha()
    print("Entrada Incorreta")
    linha()