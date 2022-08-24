from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario, diretor=None):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        self._diretor = False if diretor is None else True

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    @property
    def salario(self):
        if self._salario >= 100000 and self._diretor:
            self._salario -= self._salario * 0.1

        return self._salario

    def idade(self):
        data_nasciemnto_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O salário não possui bônus.")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
