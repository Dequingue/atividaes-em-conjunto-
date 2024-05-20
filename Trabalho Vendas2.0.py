import os
import time

os.system("cls || clear")

login_cadastrado = "admin"
senha_cadastrada = 123

lista = []

class addProduto:
    def __init__(self, descricao, tamanho, preco, cor, quantidade,tipo):
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco
        self.cor = cor
        self.quantidade = quantidade
        self.tipo = tipo

def limpar():
    os.system("cls || clear")

def logo():
    print("="*5, "URBAN OUTFIT ", "="*5)

def opcoes_cadastro():
    print("1 - Camisas")
    print("2 - Shorts")
    print("3 - Sapatos")
    
def cadastrar_produto(tipo):
    descricao = input("Digite a descrição da camisa: ")
    tamanho = input("Digite o tamanho da camisa: ")
    preco = float(input("Digite o preço :"))
    cor = input("Digite a cor da camisa: ")
    quantidade = int(input("Digite a quantidade desejada: "))
    lista.append(addProduto(descricao,tamanho,preco,cor,quantidade,tipo))
    limpar()
    print(f"{tipo} cadastrado(a) com sucesso !! ")
    
    
def comprar_produto():
    if not lista:
        print("Não há Itens disponíveis para compra ..")
        return
    
    print("Produtos Disponíveis:")
    for i in range(len(lista)):
        addProduto = lista[i]
        print(f"{i+1} - {addProduto.tipo} - {addProduto.descricao} - ({addProduto.tamanho} , {addProduto.cor}) - R$ {addProduto.preco} - {addProduto.quantidade} Unidades Disponíveis.")
    
    escolha = int(input("Escolha o número do Item que deseja: ")) - 1
    
    if 0 <= escolha < len(lista):
        
        quantidade = int(input("Digite a quantidade desejada: "))
        addProduto = lista[escolha]
        
        if quantidade <= addProduto.quantidade:
            custoTotal = addProduto.preco * quantidade
            addProduto.quantidade -= quantidade
            print(f"Você comprou {quantidade} {addProduto.tipo}. Custo Total : R$ {custoTotal :.2f}")
        else:
            print("Produto não está disponível no estoque..")
    else:
        print("Opção Inválida, tente Novamente...")
        

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
                cadastrar_produto("Camisa")
            elif escolha == 2:
                cadastrar_produto("Short")
            elif escolha == 3:
                cadastrar_produto("Sapato")
            else:
                print("Opção Inválida, tente novamente...")
                time.sleep(2)
                limpar()
        else:
            limpar()
            print("Login e senha Inválidos, tente novamente...")
            time.sleep(2)
            limpar()
    elif opcao == 2:
        limpar()
        logo()
        comprar_produto()
        time.sleep(3)
        limpar()
        

    elif opcao == 3:
        os.system("cls || clear")
        logo()
        if lista:
            for produto in lista:
                print("===== PRODUTO =====")
                print(f"Tipo: {produto.tipo}")
                print(f"Descrição: {produto.descricao}")
                print(f"Preço: R$ {produto.preco}")
                print(f"Cor: {produto.cor}")
                print(f"Tamanho: {produto.tamanho}")
                print(f"Quantidade: {produto.quantidade}\n")
        else:
            print("Nenhum produto cadastrado.")
        input("Pressione Enter para continuar...")
        os.system("cls || clear")
    elif opcao == 4:
        os.system("cls || clear")
        logo()
        print("Finalizando o programa...")
        time.sleep(3)
        break
    else:
        print("Opção inválida. Tente novamente.")
        os.system("cls || clear")

