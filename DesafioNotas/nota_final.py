nota1 = int(input("Digite a primeira nota: "))

if (nota1 < 0 or nota1 > 10):
  print("Nota inválida. Por favor, digite a nota de 0 à 10")
  nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

if (nota2 < 0 or nota2 > 10):
  print("Nota inválida. Por favor, digite a nota de 0 à 10")
  nota2 = int(input("Digite a segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))
if (nota3 < 0 or nota3 > 10):
  print("Nota inválida. Por favor, digite a nota de 0 à 10")
  nota3 = int(input("Digite a terceira nota: "))

nota4 = int(input("Digite a quarta nota: "))

if (nota4 < 0 or nota4 > 10):
  print("Nota inválida. Por favor, digite a nota de 0 à 10")
  nota4 = int(input("Digite a quarta nota: "))
else: 
  notaTotal = nota1 + nota2 + nota3 + nota4
  print(notaTotal)

if (notaTotal == 0):
  print("REPROVADO")
else:
  mediaFinal = notaTotal / 4

if (mediaFinal <= 5.9 or mediaFinal <= 4):
  print("|" + str(nota1) + "|" + str(nota2) + "|" + str(nota3) + "|" + str(nota4) + "|" + "->" + str(mediaFinal) + " EM RECUPERAÇÃO")

if (mediaFinal <= 3.9):
  print("|" + str(nota1) + "|" + str(nota2) + "|" + str(nota3) + "|" + str(nota4) + "|" + "->" + str(mediaFinal) + " REPROVADO")
  
if (mediaFinal >= 6):
  print("|" + str(nota1) + "|" + str(nota2) + "|" + str(nota3) + "|" + str(nota4) + "|" + "->" + str(mediaFinal) + " APROVADO")