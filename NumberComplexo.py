i = complex(0, 1)


class Complexo:

    # Inicializa um número
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    # Imprime um número
    def __str__(self):
        print(self.re, self.im*i)

    # Verifica a igualdade
    @staticmethod
    def equals(outro):
        if outro == Complexo:
            return True
        else:
            return False

    # Soma
    def sum(self, outro):
        soma = self.re + outro.re + (self.im + outro.im)*i
        return "A soma é %s" % soma

    # Subtrai
    def sub(self, outro):
        subtracao = (self.re - outro.re) + (self.im - outro.im)*i
        return "A subtração é %s" % subtracao

    # Multiplica
    def mult(self, outro):
        #re = (self.re * outro.re) - (self.im * outro.im)
        #im = (self.re * outro.im) + (self.im * outro.re)
        multiplica = ((self.re * outro.re) - (self.im * outro.im)) + ((self.re * outro.im) + (self.im * outro.re))*i
        return "A multiplicação é %s" % multiplica

    # Divisão
    def div(self, outro):
        if outro.re ** 2 + outro.im ** 2 != 0:
            divisao = ((self.re * outro.re + self.im * outro.im) / (outro.re ** 2 + outro.im ** 2)) + ((self.im * outro.re - self.re * outro.im) / (outro.re ** 2 + outro.im ** 2))*i

            return "A divisão é %s" % divisao
        else:
            return "Não ocorrerá a divisão, pois o denominador é 0"
