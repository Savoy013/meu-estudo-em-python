"""
Programa que calcula a área de uma parede
e calcula o quanto de tinta sera preciso
sabendo que 1 litro de tinta pinta 2m²
"""

largura = float(input("largura (M): "))
altura = float(input("Altura (M): "))

area = (largura * altura)
litros = (area / 2)

print(f"Sera preciso {litros:.2f} litros de tinta para pinta a área!")