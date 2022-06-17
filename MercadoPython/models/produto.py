from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:  # Parametros
        self.__codigo: int = Produto.contador  # Atributos da Classe
        self.__nome: str = nome  # Atributos da Classe
        self.__preco: float = preco  # Atributos da Classe
        Produto.contador += 1  # Atributos da Classe

    @property
    def codigo(self: object) -> int:  # Metodo
        return self.__codigo

    @property
    def nome(self: object) -> str:  # Metodo
        return self.__nome

    @property
    def preco(self: object) -> float:  # Metodo
        return self.__preco

    def __repr__(self):  # Metodo
        return "Test nome:% s preço:% s" % (self.nome, self.preco)

    def __str__(self) -> str:  # Metodo
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}\n'

