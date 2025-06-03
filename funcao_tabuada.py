def tabuada(numero, limite):
  for i in range(0, limite  + 1):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")

n = int(input("Insira o número que deseja:"))
l = int(input("Digite até onde quer ver a tabuada:"))

tabuada(n, l)
