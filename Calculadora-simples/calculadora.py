print('Olá pessoal, esse é meu primeiro projeto com Python, uma calculadora simples, espero que gostem!')

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o Segundo valor: '))
opr = input('Digite o operador: +, -, /, *: ')

if opr == "+":
    result = num1 + num2
    print('O resultado é:', result)

elif opr == "-":
    result = num1 - num2
    print('O resultado é:', result)

elif opr == "/":
    result = num1 / num2
    print('O resultado é:', result)

elif opr == "*":
    result = num1 * num2
    print('O resultado é:', result)    

else:
    print('Esse operador não é válido')
    