from NumberComplexo import Complexo

c1 = Complexo(2, 3)
c2 = Complexo(4, 7)
c3 = Complexo(2)
c4 = Complexo()

print(c1.__str__()) # Mostra c1
print(c4.__str__()) # Mostra c4
print(c1.sum(c4)) # Realiza a soma
print(c3.__str__()) # Mostra c3
print(c1.sum(c3)) # Realiza a soma

print(c1.equals(c2))  # Verifica se são iguais
print(c1.sum(c2))  # Realiza a soma
print(c1.sub(c2))  # Realiza a subtração
print(c1.mult(c2))  # Realiza a multiplicação
print(c1.div(c2))  # Realiza a divisão
print(c3.div(c4))  # Realiza a divisão
