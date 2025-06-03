def soma_de_numeros(numero1, numero2):
  if not(isinstance(numero1, int)) or not(isinstance(numero2, int)):
    print("Só aceitamos números inteiros")

    return
  soma = numero1 + numero2

  return f"A soma dos números é igual a {soma}"

num1 = int(input("Insira o primeiro número"))
num2 = int(input("Insira o segundo número"))
soma_de_numeros(num1, num2)
