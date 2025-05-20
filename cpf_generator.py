import random
import re

class cpf_generator:
    def __init__(self):
        self.cpf = ''

    def gerar_cpf(self):
        for i in range(9):
            digito = str(random.randint(0,9))
            self.cpf += digito
    
    def validar_cpf(self):
        print(self.cpf)
        for i in self.cpf:
            print(i)
    
    def tratar_cpf(self):
        self.cpf_tratado = re.sub(
            r'[^0-9]',
            '',
            self.cpf
        )
        return self.cpf_tratado

gerador = cpf_generator()
print(gerador.validar_cpf())