print("PROGRAMA PARA DE CRIAÇÃO DE LISTAS")
print()
loop = input("Criar nova lista? (Y/N): ")
loop = loop.lower()
if loop == "y":
    lista_1 = []
    novo_item = input("Digite um item para acrescentar à lista: ")
    lista_1.append(novo_item)
    print("Novo item adicionado à lista:")
    print()
    print("\tOrganizar de que maneira:\n1 - Ordem alfabética\n2 - Ordem alfabética inversa\n3 - Ordem inversa")
    organizar = int(input("?: "))
    if organizar == 1:
        print("Organizar por ordem alfabética:")
        print(sorted(lista_1))
        print("---FIM DO PROGRAMA---")
    elif organizar == 2:
        print("Organizar por ordem alfabética inversa:")
        lista_1.sort(reverse=True)
        print(lista_1)
        lista_1.sort(reverse=True)
        print("---FIM DO PROGRAMA---")
    elif organizar == 3:
        print("Organizar por ordem inversa:")
        lista_1.sort(reverse=True)
        print(lista_1)
        lista_1.sort(reverse=True)
        print("---FIM DO PROGRAMA---")
    else:
        print("Por favor escolha uma das opções listadas acima.")
elif loop == "n":
    prompt1 = input("Você tem certeza de que deseja cancelar? (Y/N): ")
    prompt1 = prompt1.lower()
    if prompt1 == "y":
        prompt2 = input("Certeza ABSOLUTA? (Y/N): ")
        prompt2 = prompt2.lower()
        if prompt2 == "y":
            prompt3 = input("A.B.S.O.L.U.T.A????????? (Y/N): ")
            prompt3 = prompt3.lower()
            if prompt3 == "y":
                print("Tá bom então, tudo bem... ")
            else:
                print("TAVA TE ZUANDO CARA KAKAKAKAK")
        else:
            print("TAVA TE ZUANDO CARA KAKAKAKAK")
    else:
        print("TAVA TE ZUANDO CARA KAKAKAKAK")
else:
    print("Por favor, digite uma opção válida.")
