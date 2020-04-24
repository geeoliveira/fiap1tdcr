listaDeEmails = []
listaDeEmails.append('lucas.lima@gmail.com')
listaDeEmails.append('joao.soares@hotmail.com')
listaDeEmails.append('jose.silva@outlook.com')
listaDeEmails.append('gloria.bonalde@outlook.com')
listaDeEmails.append('jack.ryan@yahoo.com')
listaDeEmails.append('jim.greer@uol.com')
listaDeEmails.append('josh.cahn@outlook.com')
listaDeEmails.append('julio.salvatti@outlook.com')
listaDeEmails.append('luiz.barbosa@outlook.com')
listaDeEmails.append('lucas.silveira@gmail.com')
listaDeEmails.append('marlene@yahoo.com')
listaDeEmails.append('maria@gmail.com')
listaDeEmails.append('josue@hotmail.com')
listaDeEmails.append('guilherme@hotmail.com')
listaDeEmails.append('thais@yahoo.com')
listaDeEmails.append('eduardo@uol.com')
listaDeEmails.append('sandra@uol.com')
listaDeEmails.append('vanderlei@terra.com')
listaDeEmails.append('dolores@yahoo.com')
listaDeEmails.append('mariana@gmail.com')
listaDeEmails.append('katia@outlook.com')
listaDeEmails.append('pedro@outlook.com')
listaDeEmails.append('barbara@terra.com')
listaDeEmails.append('teresa@gmail.com')
listaDeEmails.append('valter@hotmail.com')
listaDeEmails.append('vitor@hotmail.com')
listaDeEmails.append('mirele@yahoo.com')
listaDeEmails.append('yasmin@uol.com')
listaDeEmails.append('laura@terra.com')
listaDeEmails.append('milena@gmail.com')
existeNaLista = False

pergunta = input("Qual é o email que está buscando?")

for email in listaDeEmails:
    if pergunta == email:
        existeNaLista = True 
        print("Encontrei o email buscado")
        break

if not existeNaLista:
      print("O email não existe")
