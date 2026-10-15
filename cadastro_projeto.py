
print("=== Cadastro de Projeto ===")

while True:
    nome = input("Digite o nome do projeto: ").strip()
    responsavel = input("Digite o responsável: ").strip()
    objetivo = input("Digite o objetivo do projeto: ").strip()


    if not nome:
        print("\nErro: o campo 'nome' é obrigatório.")
    elif not responsavel:
        print("\nErro: o campo 'responsável' é obrigatório.")
    elif not objetivo:
        print("\nErro: o campo 'objetivo' é obrigatório.")
    else:
        print("\n=== Dados Cadastrados ===")
        print(f"Projeto: {nome}")
        print(f"Responsável: {responsavel}")
        print(f"Objetivo: {objetivo}")
        break

    print("Tente cadastrar novamente.\n")




