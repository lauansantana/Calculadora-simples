entrada = "| Olá! Insira a operação matemática desejada |\n"
entrada += "| Soma                     ->   [+]          |\n"
entrada += "| Subtração                ->   [-]          |\n"
entrada += "| Multiplicação            ->   [*]          |\n"
entrada += "| Divisão                  ->   [/]          |\n"

operacao = input(entrada)

if operacao == '+':
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1+n2))
elif operacao == '-':
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1-n2))
elif operacao == '*':
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1*n2))
elif operacao == '/':
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Total: {}".format(n1/n2))
else:
    print("Informação incorreta")