import random

def generate():
  return random.randint(1, 6)

print(">> BEM-VINDO(A/E) AO DESAFIO DO DADO! <<")

print("Você gostaria de jogar o dado?")
answer = input()
if ( answer == "Sim" or answer == "sim" or answer == "s" or answer == "S"):
  result = generate()
  print("O resultado de seu dado foi: ",result)

while True:
  print("Gostaria de jogar o dado novamente?")
  answer = input()
  if ( answer == "Sim" or answer == "sim" or answer == "s" or answer == "S"):
    result = generate()
    print("O resultado de seu dado foi: ",result)
  if ( answer == "Não" or answer == "não" or answer == "n" or answer == "N"):
    print("Até a próxima!!!")
    break
  else:
    print("Respota inválida, digite novamente.") 