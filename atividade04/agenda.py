import os
import pickle

agenda = []

def apaga():
    global agenda
    nome = input("Digite o nome da pessoa a ser removida: ")
    agenda = [contato for contato in agenda if contato['nome'] != nome]

def altera():
    global agenda
    nome = input("Digite o nome da pessoa a ser alterada: ")
    for contato in agenda:
        if contato['nome'] == nome:
            contato['nome'] = input("Novo nome: ")
            contato['telefone'] = input("Novo telefone: ")
            contato['tipo_telefone'] = input("Tipo de telefone (celular, fixo, residência ou trabalho): ")
            contato['aniversario'] = input("Data de aniversário (DD/MM/AAAA): ")
            contato['email'] = input("Email: ")
            return
    print("Contato não encontrado.")

def lista():
    for i, contato in enumerate(agenda):
        print(f"{i + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Tipo: {contato['tipo_telefone']}, Aniversário: {contato['aniversario']}, Email: {contato['email']}")

def le():
    global agenda
    try:
        with open("agenda.pkl", "rb") as f:
            agenda = pickle.load(f)
    except FileNotFoundError:
        agenda = []

def grava():
    with open("agenda.pkl", "wb") as f:
        pickle.dump(agenda, f)

def menu():
    print("\n1. Adicionar contato")
    print("2. Apagar contato")
    print("3. Alterar contato")
    print("4. Listar contatos")
    print("5. Exibir tamanho da agenda")
    print("6. Ordenar agenda por nome")
    print("7. Sair")

def tamanho_agenda():
    print(f"Tamanho da agenda: {len(agenda)} contatos.")

def ordena_por_nome():
    global agenda
    agenda.sort(key=lambda x: x['nome'])

def verifica_nome(nome):
    nomes = [contato['nome'] for contato in agenda]
    return nomes.count(nome) > 1

def main():
    le()
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            if verifica_nome(nome):
                print("Erro: Já existe um contato com esse nome na agenda.")
            else:
                telefone = input("Telefone: ")
                tipo_telefone = input("Tipo de telefone (celular, fixo, residência ou trabalho): ")
                aniversario = input("Data de aniversário (DD/MM/AAAA): ")
                email = input("Email: ")
                agenda.append({'nome': nome, 'telefone': telefone, 'tipo_telefone': tipo_telefone, 'aniversario': aniversario, 'email': email})
        elif opcao == '2':
            apaga()
        elif opcao == '3':
            altera()
        elif opcao == '4':
            lista()
        elif opcao == '5':
            tamanho_agenda()
        elif opcao == '6':
            ordena_por_nome()
        elif opcao == '7':
            grava()
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
