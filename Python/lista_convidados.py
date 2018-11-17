#////////////////////// Listas em Python //////////////////////
#//////// Escrito por Erick César, 08/07/2018, 23:45 PM ///////

convidados_festa = ["Convidado 01" ,"Convidado 02", "Convidado 03", "Convidado 04", "Convidado 05", "Convidado 06", "Convidado 07", "Convidado 08", "Convidado 09", "Convidado 10", "Convidado 11", "Convidado 12", "Convidado 13", "Convidado 14", "Convidado 15"]
print("Os convidados são: ")
print(convidados_festa)
print()

nao_comparecera_if = input("Alguém não poderá comparecer? (Y/N): ")
nao_comparecera_if = nao_comparecera_if.upper()
if nao_comparecera_if == "Y":
    nao_comparecera_nome = input("Quem não poderá comparecer? ")
    nao_comparecera_nome = nao_comparecera_nome.title()
    convidados_festa.remove(nao_comparecera_nome)
    print("O convidado %s foi removido da lista de convidados com sucesso!" %(nao_comparecera_nome))
    print()
    print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
    print()
    acrescentar_convidado = input("Alguém mais irá comparecer? (Y/N): ")
    acrescentar_convidado = acrescentar_convidado.upper()
    if acrescentar_convidado == "Y":
        novo_convidado_insert = input("Digite o nome do novo convidado: ")
        novo_convidado_insert = novo_convidado_insert.title()
        convidados_festa.insert(0, novo_convidado_insert)
        print("Novo convidado adicionado com sucesso à lista! (método .insert())")
        print()
        print("Então são %i convidados ao todo para a festa." %(len(convidados_festa)))
        print()
    elif acrescentar_convidado == "N":
        print("Boa festa!")
    else:
        print("masoq")
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
    print("Desculpe, não compreendi.")
print()
