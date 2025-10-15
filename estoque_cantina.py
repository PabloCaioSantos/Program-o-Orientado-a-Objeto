estoque_comida = {
    "sanduiche": 5,
    "bolo": 6,
    "coxinha": 8,
    "pastel": 4,
    "pao_queijo": 10,
    "torta": 3,
    "empada": 7,
    "pizza": 2,
    "cachorro_quente": 9,
    "esfirra": 6
}

estoque_bebida = {
    "refrigerante": 10,
    "suco": 8,
    "cafe": 15,
    "agua": 20,
    "cha": 12,
    "achocolatado": 7,
    "vitamina": 5,
    "suco_natural": 6,
    "agua_coco": 4,
    "refrigerante_zero": 8
}


def mostrar_estoque():
    global estoque_comida, estoque_bebida

    print("\n--- ESTOQUE ATUAL ---")
    print("\nComidas:")
    for produto, quantidade in estoque_comida.items():
        print(f"{produto}: {quantidade}")

    print("\nBebidas:")
    for produto, quantidade in estoque_bebida.items():
        print(f"{produto}: {quantidade}")


def adicionar_produto(nome, quantidade):
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        estoque_comida[nome] += quantidade
        print(f"Adicionado! Total de {nome}: {estoque_comida[nome]}")
    elif nome in estoque_bebida:
        estoque_bebida[nome] += quantidade
        print(f"Adicionado! Total de {nome}: {estoque_bebida[nome]}")
    else:
        tipo = input("Produto novo. É comida ou bebida? (c/b): ")
        if tipo == 'c':
            estoque_comida[nome] = quantidade
        else:
            estoque_bebida[nome] = quantidade
        print(f"{nome} adicionado com {quantidade} unidades")


def remover_produto(nome, quantidade):
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        if estoque_comida[nome] >= quantidade:
            estoque_comida[nome] -= quantidade
            print(f"Removido! Restam {estoque_comida[nome]} de {nome}")
        else:
            print(f"Quantidade insuficiente! Disponível: {estoque_comida[nome]}")
    elif nome in estoque_bebida:
        if estoque_bebida[nome] >= quantidade:
            estoque_bebida[nome] -= quantidade
            print(f"Removido! Restam {estoque_bebida[nome]} de {nome}")
        else:
            print(f"Quantidade insuficiente! Disponível: {estoque_bebida[nome]}")
    else:
        print("Produto não encontrado")


def consultar_produto(nome):
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        print(f"{nome}: {estoque_comida[nome]} unidades (comida)")
    elif nome in estoque_bebida:
        print(f"{nome}: {estoque_bebida[nome]} unidades (bebida)")
    else:
        print("Produto não encontrado")


def repor_automatico():
    global estoque_comida, estoque_bebida

    print("\nReposição automática:")

    for produto in estoque_comida:
        if estoque_comida[produto] < 3:
            estoque_comida[produto] += 5
            print(f"{produto} reposto")

    for produto in estoque_bebida:
        if estoque_bebida[produto] < 3:
            estoque_bebida[produto] += 5
            print(f"{produto} reposto")


def salvar_relatorio():
    global estoque_comida, estoque_bebida

    arquivo = open("estoque.txt", "w")

    arquivo.write("RELATORIO DE ESTOQUE\n\n")

    arquivo.write("Comidas:\n")
    for produto, quantidade in estoque_comida.items():
        arquivo.write(f"{produto}: {quantidade}\n")

    arquivo.write("\nBebidas:\n")
    for produto, quantidade in estoque_bebida.items():
        arquivo.write(f"{produto}: {quantidade}\n")

    arquivo.close()
    print("Relatório salvo em estoque.txt")


def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Mostrar estoque")
        print("2 - Adicionar produto")
        print("3 - Remover produto")
        print("4 - Consultar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, quantidade)
        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            remover_produto(nome, quantidade)
        elif opcao == "4":
            nome = input("Nome do produto: ")
            consultar_produto(nome)
        elif opcao == "5":
            salvar_relatorio()
            print("Saindo...")
            break
        else:
            print("Opção inválida")


menu()