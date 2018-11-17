from random import randint
pcchoice = int()
usrchoice = int()
pedra = int(1)
papel = int(2)
tesoura = int(3)
############################

print("PEDRA, PAPEL, TESOURA\n")
print("1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n")

usrchoice = int(input("\tEscolha: "))
#Decidindo aleatoriamente e imprimindo a escolha do pc
pcchoice = randint(1,3)
if pcchoice == 1:
    print("o pc escolheu pedra!")
elif pcchoice == 2:
    print("O pc escolheu papel!")
else:
    print("O pc escolheu tesoura!")

    if usrchoice == pcchoice:
        print("O jogo empatou!")
    elif usrchoice == 1 and pcchoice == 2:
        print("Não foi dessa vez, o pc ganhou :(")
    elif usrchoice == 1 and pcchoice == 3:
        print("parabéns você ganhou!")
    elif usrchoice == 2 and pcchoice == 1:
        print("Você ganhou!")
    elif usrchoice == 2 and pcchoice == 3:
        print("Não foi dessa vez, o pc ganhou :(")
    elif usrchoice == 3 and pcchoice == 1:
        print("Não foi dessa vez, o pc ganhou :(")
    else:
        print("Parabéns! você ganhou!")
