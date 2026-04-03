valor = str(input("Digite algo: "))

print(valor)
print(type(valor))
print("E um numero inteiro? {}".format(valor.isnumeric()))
print("E Alfabetico? {}".format(valor.isalpha()))
print("E alfanumerico? (Letras e numeros) {}".format(valor.isalnum()))
print("Esta somente em Maiusculo? {}".format(valor.isupper()))
print("Esta somente em Minusculo? {}".format(valor.islower()))
