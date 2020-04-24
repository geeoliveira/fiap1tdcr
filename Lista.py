listaDeEmails = []
listaDeEmails.append('lucas.lima@gmail.com')
listaDeEmails.append('joao.soares@hotmail.com')
listaDeEmails.append('jose.silva@outlook.com')
inserir = "Sim"
existeNaLista = False

pergunta = input("Qual é o email que está buscando?")

for email in listaDeEmails:
    if pergunta == email:
        existeNaLista = True 
        print("Encontrei o email buscado")
        break

if not existeNaLista:
      print("O email não existe")
