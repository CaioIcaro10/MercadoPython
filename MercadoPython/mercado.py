from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('====================================')
    print('=========== Bem-vindo(a) ===========')
    print('============== FL Shop =============')
    print('====================================')

    print('Selecione uma das opções abaixo: ')
    print('1 -  Cadastrar produto')
    print('2 -  Listar produto')
    print('3 -  Comprar produto')
    print('4 -  Visualizar Carrinho')
    print('5 -  Fechar pedido')
    print('6 -  Sair do Sistema')

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida!!')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print('===================')
    print('Cadastro de Produto')
    print('===================\n')

    nome: str = input('Infome o nome do Produto: ')
    preco: float = float(input('Informe o Preço do produto: '))

    produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O Produto {produto.nome} Foi Cadastrado com Sucesso!!')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('==================')
        print('Listando o Produto')
        print('==================\n')
        for produto in produtos:
            print(produto)
            print('------------------')
            sleep(1)
        menu()
    else:
        print('Não existe Produtos Cadastrados!!\n')
        sleep(2)
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo do produto que deseja adicionar ao carrinho: ')
        print('============================================================= ')
        print('================== Produtos Disponiveis =====================')
        for produto in produtos:
            print(produto)
            print('---------------')
            sleep(1)
        codigo: int = int(input())

        produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.\n')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho\n')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O Produto {produto.nome} foi adicionado ao Carrinho\n')
                sleep(2)
                menu()

        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não temos produto para vender. ')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do Carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(f'Objeto: {dados[0].nome}')
                print(f'Quantidade: {dados[1]}')
                print('----------------------------------------\n')
                sleep(1)
        menu()
    else:
        print('Ainda não existem produtos no carrinho\n')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(str(dados[0].nome))
                print(f'quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre\n')
        carrinho.clear()
        sleep(3)
    else:
        print('Ainda não existem Produtos no Carrinho!!\n')
        sleep(2)
        menu()

def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
