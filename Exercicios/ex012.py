"""
Programa que ler um preço e calcula 
o desconto de 5%1
"""

preço = float(input("Preço do produto: "))

desconto = preço - (preço * 5 / 100)

print(f"O preço com desconto de 5% vai ser {desconto:.2f}")