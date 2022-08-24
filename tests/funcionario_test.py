import pytest
from pytest import mark
from codigo.funcionario import Funcionario


class TestFuncionario:

    def test_idade_funcionario(self):
        lucas = Funcionario("lucas", "12/11/1990", 111)

        assert lucas.idade() == 32

    def test_valida_sobrenome_funcionario_informado(self):
        lucas = Funcionario("lucas salicano", "12/11/1990", 111)

        assert lucas.sobrenome == "salicano"

    def test_desconto_dez_porcento_salario_acima_igual_cem_mil(self):
        lucas = Funcionario("lucas salicano", "12/11/1990", 100000, True)

        assert lucas.salario == 90000

    def test_sem_desconto_dez_porcento_salario_abaixo_cem_mil(self):
        maria = Funcionario("maria", "18/01/1995", 99000)

        assert maria.salario == 99000

    @mark.calcular_bonus
    def test_calculo_bonus_dez_porcento_salario_menor_que_mil(self):
        maria = Funcionario("maria", "18/01/1995", 1200)

        assert maria.calcular_bonus() == 120

    @mark.calcular_bonus
    def test_exception_sem_bonus_dez_porcento_salario_maior_que_mil(self):
        with pytest.raises(Exception) as exception:
            maria = Funcionario("maria", "18/01/1995", 120000)
            assert maria.calcular_bonus()
            assert exception.value == "O salário não possui bônus."
