from sqlalchemy.util import non_memoized_property
# Academico: Rodrigo Estevão Rottava - RA: 60001962

print("\n")

print ("1- Variaveis e Tipos de Dados")

name = "Rodrigo Estevão Rottava"
print (name)

idade = 22
print (idade)

altura = 1.77
print (altura)

print("\n")

#============================================================

print ("2- Strings")

title = "Python é Incrivel!!"
print (title)

concactene = "Olà " + "Mundo"
print (concactene)

convercao = int("123") + 10
print (convercao)

print("\n")

#============================================================

print ("3- Listas")

nums = [1, 2, 3, 4, 5]
print(nums)

nums.append(6)
print(nums)

nums.remove(3)
print(nums)

print("\n")

#============================================================

print ("4- Dicionarios")

dados = {"nome": "Rodrigo", "idade": 25, "cidade": "Curitiba"}
print(dados)

dados["país"] = "Brasil"
print(dados)

del dados["cidade"]
print(dados)

print("\n")

#============================================================

print ("5- Tuplas")

tupla = (1, 2, 3)
print (tupla)

tupla = (5)
print (tupla)

print("\n")

#============================================================

print ("6- Operadores Aritmeticos")

soma = (10 + 20)
print (soma)
print (50 - 30)
print (5 * 6)
print (100 / 4)

print("\n")

#============================================================

print ("7- Operadores de Comparação")

print (10 > 5)
print (20 == 20)
print (15 != 10)

print("\n")

#============================================================

print ("8- Operadores Logico")

print (10 > 5 and 20 < 30)
print (10 > 5 and 20 > 30)
print (not (10 > 20))

print("\n")

#============================================================

print ("9- Condicionais")

numero = int(input("Coloque um Numero:"))
if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("zero")

numero = int(input("Coloque um Numero:"))
print("par" if numero % 2 == 0 else "impar")

idadee = int(input("Coloque sua Idade:"))
print("Vote no 25.555" if idadee >= 16 else "Não pode Votar")

print("\n")

#============================================================

print ("10- Loops")

for i in range(1, 11):
    print(i)

number = 10
while number >= 1:
    print(number)
    number -= 1

print(sum(range(1, 101)))

while int(input("Coloque um numero:")) != 0:
    pass

