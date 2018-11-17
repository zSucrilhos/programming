################################################################################################################################################################
################################################################## LISTAS EM PYTHON ############################################################################
################################################################################################################################################################
fighter_jets = ["Dassault Mirage 2000-5", "Dassault Mirage 2000-10", "F-15 Eagle", "F-16 Fighting Falcon", "F-22 Raptor","Eurofighter 2000", "Sukhoi Su-27", "Sukhoi Su-30", "Sukhoi Su-34", "Sukhoi Su-35", "Sukhoi Su-37", "Mig-15", "Mig-21", "Mig-29"]

gpus = ["GTX 650", "GTX 670", "GTX 680", "GTX 750", "GTX 750 Ti", "GTX 760", "GTX 770", "GTX 780" "GTX 780 Ti", "GTX 950", "GTX 960", "GTX 970", "GTX 980", "GTX 1030", "GTX 1050", "GTX 1050 Ti", "GTX 1060 3GB", "GTX 1060 6GB", "GTX 1070", "GTX 1070 Ti", "GTX 1080", "GTX 1080 Ti"]

cpus = ["i5 3570", "i5 3570k", "i5 4440", "i5 4440k", "i7 2600", "FX 6300", "FX 8300", "FX 9500"]

nomes = ["erick", "bruno", "claudineia", "julio", "samuel", "pedro", "joão vitor", "marcelo"]

print("Meu caça preferido é o "+ fighter_jets[1])
print("Minha placa de vídeo atual é a " + gpus[14])
print("Meu processador atual é o " + cpus[5])
print()
print("Meu nome é %s" %(nomes[0].lower()))
print("Meu pai se chama " + nomes[3].upper())
print("Minha mãe se chama %s" %(nomes[2].title()))
print("Imprimindo os últimos itens de uma lista 1: " + gpus[-1])
print("Imprimindo os últimos itens de uma lista 2: " + gpus[-2])
print("Imprimindo os últimos itens de uma lista 3: " + gpus[-3])
print("Imprimindo os últimos itens de uma lista 4: " + gpus[-4].lower())
master_race = gpus[-1]

print(master_race)
print()
modify = input("Modificar o último item da lista 'fighter_jets'? O último item atualmente é %s ? (Y/N): "  %(fighter_jets[-1]))
modify = modify.upper()
if modify == "Y":
    entrada_modify = input("Digite o nome do novo item: ")
    fighter_jets[-1] = entrada_modify
    print(fighter_jets[-1] + ", item modificado com sucesso!")
    print(fighter_jets)
else:
    print("Tá bom, até mais!")
print()

lista_nova = ["01", "02", "03", "04", "05" ,"06" ,"07" ,"08", "09"]
print("Agora para remover elementos de uma lista.")
loop3 = "Y"
while loop3 == "Y":
        inserir = input("Deletar um item da lista? (Y/N) ")
        if inserir == "Y":
            print(lista_nova)
            pos_del_item = int(input("Digite a posição do item a remover (0-X): "))
            del lista_nova[pos_del_item]
            print("O item foi inserido com sucesso!!")
            print()
            print(lista_nova)
        else:
            print("ok")
print()
print(len(fighter_jets))
print(len(gpus))
print(len(cpus))
print(len(nomes))
