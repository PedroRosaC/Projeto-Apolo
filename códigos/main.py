def radiciacao(x,y):
    radiciacao = x**1/y
    print(radiciacao)
    
def exponenciacao(x,y):
    exponenciacao = x**y
    print(exponenciacao)

def divisao(x,y):
    divisao = x/y
    print(divisao)

def multiplicacao(x,y):
    multiplicacao = x*y
    print(multiplicacao)

def subtracao(x,y):
    subtracao = x-y
    print(subtracao)

def soma(x,y):
    soma = x+y
    print(soma)
'''(soma); -(subtração); *(multiplicação); /(divisão); **(exponenciação).'''    
    

print("escolha sua opção: ")
print("Opção 1 : Adição")
print("Opção 2 : subtração")
print("Opção 3 : multiplicação")
print("Opção 4 : divisão")
print("Opção 5 : exponenciação")
print("Opção 6 : Radiciação")
print("Opção 7 : Encerrar o programa")
opcao = int(input("Entre com a sua opção"))
x = int(input("entre com o numero x : "))
y = int(input("entre com o numero y : "))

while opcao != 7:
    
    
    if opcao == 1:
        soma(x,y)
    if opcao == 2:
        subtracao(x,y)
    if opcao == 3:
        multiplicacao(x,y)
    if opcao == 4:
        divisao(x,y)
    if opcao == 5:
        exponenciacao(x,y)
    if opcao == 6:
        radiciacao(x,y)
    
    print("escolha sua opção: ")
    print("Opção 1 : Adição")
    print("Opção 2 : subtração")
    print("Opção 3 : multiplicação")
    print("Opção 4 : divisão")
    print("Opção 5 : exponenciação")
    print("Opção 6 : Radiciação")
    print("Opção 7 : Encerrar o programa")
    opcao = int(input("Entre com a sua opção"))
    x = int(input("entre com o numero x : "))
    y = int(input("entre com o numero y : "))
    
    
    
    





