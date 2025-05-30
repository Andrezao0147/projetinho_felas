def converter_celsius_para_fahrenheit(graus_celsius):
  if not(isinstance(graus_celsius, int)):
    print("Não consegue né moisés, preciso receber um INT")

    return

  graus_fahrenheit = graus_celsius * 9/5 + 32

  return f"A temperatura:{graus_celsius} equivale a {graus_fahrenheit}"
