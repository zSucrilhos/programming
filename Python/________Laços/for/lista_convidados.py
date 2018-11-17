#////////////////////// Listas em Python //////////////////////
#//////// Escrito por Erick César, 08/07/2018, 23:45 PM ///////

convidados_festa = ["João", "Carla", "Maria", "Gabriel", "Vitor", "Bruno", "Erick", "Samuel", "marcelo", "Pedro", "Augusto", "Camila" "Isabela", "Beatriz", "Emilly", "José", "Júnior", "Jéssica", "Ashley", "Gabriele"]
print("Os convidados são: ")
print(convidados_festa)
print()

nao_comparecera_if = input("Alguém não poderá comparecer? (Y/N): ")
nao_comparecera_if = nao_comparecera_if.upper()
if nao_comparecera_if == "Y":
    nao_comparecera_num = int(input("Quantas pessoas não comparecerão? (Por favor digite somente números): "))
    if nao_comparecera_num > len(convidados_festa):
        print("\tPor favor, digite um número válido entre 1 e %s." %(len(convidados_festa)))
    else:
        for nao_comp in range(0, nao_comparecera_num):
            nao_comparecera_nome = input("Quem não poderá comparecer? ")
            nao_comparecera_nome = nao_comparecera_nome.title()
            convidados_festa.remove(nao_comparecera_nome)
            print("\tO convidado %s foi removido da lista de convidados com sucesso!" %(nao_comparecera_nome))
            print()
            print("\tEntão são %i convidados ao todo para a festa.\n" %(len(convidados_festa)))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    acrescentar_convidado = input("Alguém mais irá comparecer? (Y/N): ")
    acrescentar_convidado = acrescentar_convidado.upper()
    if acrescentar_convidado == "Y":
        novo_convidado_insert = input("Digite o nome do novo convidado: ")
        novo_convidado_insert = novo_convidado_insert.title()
        convidados_festa.insert(0, novo_convidado_insert)
        print("Novo convidado adicionado com sucesso à lista!")
        print()
        print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
        print()
    elif acrescentar_convidado == "N":
        print("Boa festa!")
    else:
        print("ERRO: Comando não reconhecido.")
elif nao_comparecera_if == "N":
    acrescentar_convidado = input("Alguém mais irá comparecer? (Y/N): ")
    if acrescentar_convidado == "Y":
        novo_convidado_insert = input("Digite o nome do novo convidado: ")
        novo_convidado_insert = novo_convidado_insert.title()
        convidados_festa.insert(0, novo_convidado_insert)
        print("Novo convidado adicionado com sucesso à lista! (método .insert())")
        print()
        print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
        print()
    elif acrescentar_convidado == "N":
        print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
    else:
        print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
else:
    print("ERRO: Comando não reconhecido.")
print()
