import json

ARQUIVO = "medicamentos.json"


def carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)


def buscar(lista, nome):
    return [med for med in lista if nome.lower() in med["nome"].lower()]


medicamentos = carregar()

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        med = {
            "nome": input("Nome: "),
            "principio_ativo": input("Princípio ativo: "),
            "laboratorio": input("Laboratório: "),
            "quantidade": input("Quantidade: ")
        }
        medicamentos.append(med)
        print("Cadastrado!")

    elif opcao == "2":
        for med in medicamentos:
            print(med)

    elif opcao == "3":
        nome = input("Digite o nome: ")
        resultado = buscar(medicamentos, nome)
        print(resultado if resultado else "Não encontrado.")

    elif opcao == "4":
        salvar(medicamentos)
        print("Dados salvos. Programa encerrado!")
        break

    else:
        print("Opção inválida!")
