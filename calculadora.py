def soma():
    return (x+y)
    
def subtracao():
    return (x-y)
    
def multiplicacao():
    return (x*y)
    
def divisao():
    return (x/y)
    
menu =int(input("Qual operação deseja realizar? "'\n'"1:Soma"'\n'"2:Subtração"'\n'"3:Multiplicação"'\n'"4:Divisão"'\n'))
while menu != 1 and menu != 2 and menu != 3 and menu != 4:
    print("operação inválida")
    menu = int(input('Digite novamente a operação que deseja: '))
   
   
x = float(input("Digite o primeiro número: ")) 
y = float(input("Digite o segundo número: "))


if menu == 1:
    print(f'Resultado: {x} + {y} =',soma())
elif menu == 2:
    print(f'Resultado: {x} - {y} =',subtracao())
elif menu == 3:
    print(f'Resultado: {x} x {y} =',multiplicacao())
elif menu == 4:
    print(f'Resultado: {x} ÷ {y} =',divisao())
