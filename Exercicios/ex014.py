"""
Programa que ler uma temperatura em
Celsius e converte em fahrenheit!
"""
print("Conversor de Temperatura")
print("-=" *12)
c = float(input("Temperatura em Celsius: "))

f = (c * 1.8) + 32

print("-="*25)
print(f"A temperatura {c:.0f} C convertida para \nFahrenheit e equivalente a {f:.0f} F")
print("-="*25)

print("Fim!")
print("Volte Sempre :)")