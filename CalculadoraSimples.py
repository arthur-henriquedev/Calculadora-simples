print("Olá, vamos começar!")

#Coleta dos números e operação
valor_a = int(input("Escreva o primeiro número: "))
print("Operações disponíveis: +, -, *, /")
operacao = input("Escreva a operação: ").strip()
valor_b = int(input("Escreva o segundo número: "))

#Exibição do resultado
while True:
 if operacao == "+":
    print("A soma é:", valor_a + valor_b)
    break   
 elif operacao == "-":
    print("A subtração é:", valor_a - valor_b)
    break
 elif operacao == "*":
    print("A multiplicação é:", valor_a * valor_b)
    break
 elif operacao == "/":
    print("A divisão é:", valor_a / valor_b)
    break

 else: 
  operacao != "+" or "-" or "*" or "/"
  print("Operação inválida")
  continue