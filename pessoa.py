class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def calcular_ano_nascimento(self):
        ano_atual = 2024
        return ano_atual - self.__idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade