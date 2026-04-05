"""
Programa que ler um salario e calcula
o aumento de 15%
"""

salario = float(input("Salário do funcionario: "))

aumento = salario + (salario * 15 / 100)

print(f"Aumento do salário em 15% será {aumento:.2f}")