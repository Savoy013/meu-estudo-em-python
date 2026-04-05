"""
Programa que calcular o total a pagar sabendo
que cada dia e 60 R$ e cada km rodado e R$ 0.15
"""

print("-="*15)
print("CARROS ALUGADOS")
print("-="*15)
km = float(input("Km percorrido: "))
dia = int(input("Dias alugado: "))

total_pagar = (dia * 60) + (0.15 * km)

print(f"O total a pagar é {total_pagar:.2f} R$ !.")

print("FIM!")
print("Volte Sempre :D")
