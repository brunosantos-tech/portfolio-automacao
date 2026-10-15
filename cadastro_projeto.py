
print("=== Cadastro de Projeto ===")

while True:
    nome = input("Digite o nome do projeto: ").strip()
    responsavel = input("Digite o responsável: ").strip()
    objetivo = input("Digite o objetivo do projeto: ").strip()

    if nome and responsavel and objetivo:
        print("\n=== Dados Cadastrados ===")
        print(f"Projeto: {nome}")
        print(f"Responsável: {responsavel}")
        print(f"Objetivo: {objetivo}")
        break
    else:
        print("\nErro: todos os campos são obrigatórios.")
        print("Tente cadastrar novamente.\n")



