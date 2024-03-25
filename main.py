#Programa que solicita 10 números e mostra se ele é zero, negativo ou positivo
for i in range(1,11):
  numero = float(input("Digite um número aleatório: "))
  if numero < 0:
    print("Número negativo!")
  elif numero == 0:
    print("Zero!")
  else:
    print("Número positivo!")

#Programa que imprima todos número entre 0 (inclusive) e 100 (inclusive)
i = 0
while i <= 100:
  print(i)
  i += 1

#Programa que imprima os valores entre o valor digitado pelo usuário e erro caso n1 > n2
num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
if num1 < num2:
  while num1 <= num2:
    print(num1)
    num1 += 1
else:
  print("Erro!")

#Programa que imprima os valores entre o valor digitado pelo usuário
num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
if num1 < num2:
  while num1 <= num2:
    print(num1)
    num1 += 1
else:
  while num1 >= num2:
    print(num1)
    num1 -= 1

#Programa que impra na tela a soma de todos os valores entre 1 100
soma = 0
numero = 1
while numero <= 10:
    soma = soma + numero
    numero = numero + 1
print(soma)

#Programa que solicita números positivos e pares caso diferente imprima a soma
soma = 0
while True:
    numero = int(input("Digite um número positivo e par, ou outra número para encerrar:"))
    if numero < 0:
        break
    soma += numero 
print("A soma dos números positivos e pares digitados é:", soma)

#Programa que solicite usuário e senha e ao acertar imprima acesso liberado
usuario = "USER10"
senha = "PASSWORD1234"
while True:
  usuario_digitado = input("Digite o usuário:")
  senha_digitada = input("Digite a senha:")
  if usuario_digitado == usuario and senha_digitada == senha:
    print("LOGIN EFETUADO COM SUCESSO!")
    break
  else:
    print("Usuário ou senha incorretos, tente novamente!")

#Programa que solicite usuário e senha caso errar por 3x imprimir aviso
usuario = "USER10"
senha = "PASSWORD1234"
tentativas = 0
while tentativas < 3:
    usuario_digitado = input("Digite o usuário: ")
    senha_digitada = input("Digite a senha: ")
    if usuario_digitado == usuario and senha_digitada == senha:
        print("LOGIN EFETUADO COM SUCESSO!")
        break
    else:
        print("Usuário ou senha incorretos, tente novamente!")
        tentativas += 1
if tentativas == 3:
    print("Você excedeu o número máximo de tentativas. Acesso bloqueado.")