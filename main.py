def cadastrar(dado):
    key = input("Digite nome: ")
    dado[key] = [
        input("Digite email: "),
        input("Digite senha: ")
    ]

    input("Dado cadastrado com sucesso!")
    menu() 
     

def consultar(dado):
    key = input ("Qual nome deseja buscar? ")
    if key in dado.keys():
        print("E-mail: ", dado[key][0])
        print("Senha: ", dado[key][1])
    else:
        print("Item não encontrado")
    
    menu() 
    

def deletar(dado): 
    key = input("Qual item deseja deletar? ")
    if key in dado.keys():
        del dado[key]
        print(key + " foi deletado com sucesso!")
    else:
        print("Item não encontrado")
    
    menu() 

dado = {
    "Lucas":["lucas.lima@gmail.com", "8765"],
    "Joao":["joao.soares@hotmail.com", "1234"],
    "Gloria":["gloria.bonalde@outlook.com", "2288"]
}

def menu():
    opcao = int(input( '''
    Escolha uma opção
    1 - Cadastrar
    2 - Consultar
    3 - Deletar
    0 - Fechar Menu 
    Escolha:  ''')) 
    if opcao == 1:
        cadastrar(dado)
    elif opcao == 2:
        consultar(dado)
    elif opcao == 3:
        deletar(dado)
    elif opcao == 0:
        print("Bye bye!")
        exit()
    else:
        print("Escolha uma opção válida")

menu()