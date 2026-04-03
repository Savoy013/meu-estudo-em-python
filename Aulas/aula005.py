"""n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro: "))

s = (n1 + n2)
print("A soma entre {} e {} vale {}".format(n1, n2, s))"""

n = str(input("Digite algo: "))
print(type(n))
print(n.isnumeric()) # E um numero inteiro?
print(n.isalpha())  # E um alfabetico?
print(n.isalnum())  # E alfanumerico
print(n.isupper()) # So tem Maiusculo?
print(n.islower()) # So tem Minusculo?