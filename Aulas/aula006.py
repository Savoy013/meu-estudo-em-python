"""nome = str(input("Qual é seu nome?: "))
print(f"Prazer em te conhecer {nome:=^20}!")"""

n1 = int(input("Um Valor: "))
n2 = int(input("Outro Valor: "))
soma = (n1+n2)
m = (n1*n2)
d = (n1 / n2)
di = (n1 // n2)
e = (n1 ** n2)
print(f"A soma vale {soma}")
print(f"A multiplicação vale {m}")
print(f"A divisão vale {d:.2f}")
print(f"A divisão inteira vale {di}")
print(f"A potência vale {e}")
# end="" para junta com a linha de baixo 
# \n = para quebrar a linha