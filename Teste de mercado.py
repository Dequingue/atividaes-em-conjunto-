import os
import time

os.system("cls || clear")

login_cadastrado = "admin"
senha_cadastrada = 123

lista = []

class addProduto:
    def __init__(self, descricao, tamanho, preco, cor, quantidade):
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco
        self.cor = cor
        self.quantidade = quantidade

def limpar():
    os.system("cls || clear")

def logo():
    print("="*5, "URBAN OUTFIT ", "="*5)

def opcoes_cadastro():
    print("1 - Camisas")
    print("2 - Shorts")
    print("3 - Sapatos")

def menu():
    print("="*5, "URBAN OUTFIT ", "="*5)
    print("1 - Cadastrar Produto ")
    print("2 - Comprar um Produto")
    print("3 - Verificar Estoque ")
    print("4 - Sair do Página ")

while True:
    menu()
    opcao = int(input("Escolha a opção desejada: "))


    if opcao == 1:
        limpar()
        logo()
        login = input("Informe o seu login: ")
        senha = int(input("Informe a sua senha: "))

        if login == login_cadastrado and senha == senha_cadastrada:
            limpar()
            logo()
            print("Bem Vindo!! ")
            time.sleep(2)
            limpar()
            logo()
            opcoes_cadastro()
            escolha = int(input("Escolha a opção que deseja cadastrar: "))
            
            if escolha == 1:
                descricao = input("Digite a descrição da camisa: ")
                tamanho = input("Digite o tamanho da camisa: ")
                preco = float(input("Digite o preço :"))
                cor = input("Digite a cor da camisa: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                lista.append(addProduto(descricao,tamanho,preco,cor,quantidade))
                limpar()

            elif escolha == 2:
                limpar()
                logo()
                descricao = input("Digite a descrição do Short: ")
                tamanho = input("Digite o tamanho do Short: " )
                cor = input("Digite a cor do Short: ")
                preco = float(input("Digite o preço :"))
                quantidade = int(input("Digite a quantidade desejada: "))
                lista.append(addProduto(descricao,tamanho,preco,cor,quantidade))
                limpar()
            elif escolha == 3:
                limpar()
                logo()
                descricao = input("Digite a descrição do Sapato: ")
                tamanho = int(input("Digite o tamannho do Sapato(EX = 38): "))
                cor = input("Digite a cor do Sapato: ")
                preco = float(input("Digite o preço :"))
                quantidade = int(input("Digite a quantidade desejada: "))
                lista.append(addProduto(descricao,tamanho,preco,cor,quantidade))
                limpar()
        else:
            limpar()
            print("Login e senha Inválidos, tente novamente...")
            time.sleep(2)
            limpar()
    if opcao == 2:
        limpar()
        logo()
        opcoes_cadastro()
        escolha = int(input("Escolha a opção desejada : "))
        if escolha == 1 or escolha == 2 or escolha == 3:
            limpar()
            descricao_compra = input("Digite a descrição do produto que deseja comprar: ")
        for produto in lista:
            if produto.descricao == descricao_compra and produto.quantidade > 0:
                produto.quantidade -= 1
                limpar()
                print("Compra realizada com sucesso! Uma unidade de [{}] foi removida do estoque.".format(descricao_compra))
                break
        else:
            limpar()
            print("Produto não encontrado no estoque ou estoque esgotado.")

    if opcao == 3:
        for addProduto in lista:
            limpar()
            print("\n===== PRODUTO =====")
            print("Descrição do Produto: {}".format(addProduto.descricao))
            print("Preço: R${: .2f}".format(addProduto.preco))
            print("Cor: {}".format(addProduto.cor))
            print("Tamanho: {}".format(addProduto.tamanho))
            print("Quantidade: {}\n".format(addProduto.quantidade))
            

    if opcao == 4:
        limpar()
        logo()
        print("Finalizando do programa ....")
        time.sleep(3)
        break
