# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def soma(x,y):
    return int(x)+int(y)
def sub(x,y):
    return int(x)-int(y)
def div(x,y):
    return int(x)/int(y)
def mult(x,y):
    return int(x)*int(y)

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\n Digite a operação desejada: \n")

num1 = input("\nInforme o primeiro número: \n")
num2 = input("\nInforme o segundo número: \n")

if escolha == "1":
    print("\n")
    print(num1 ,"+" ,num2, "=", soma(num1,num2))
    print("\n")

elif  escolha == "2":
    print("\n")
    print(num1, "-", num2, "=", sub(num1,num2))
    print("\n")  

elif escolha == "3":
    print("\n")
    print(num1, "*", num2, "=", mult(num1,num2))
    print("\n")

elif escolha == "4":
    print("\n")
    print(num1, "/", num2, "=", div(num1,num2))
    print("\n")

else: print("Operação inválida!")
