# -*- coding: utf-8 -*-
print("\t\t\t\t\t\t\t\t\tCALCULADOR DE MÉDIA ARITIMÉTICA")
print("Calculador de nota média, baseada em 04 notas. Você também pode omitir as notas digitando '0' quando solicitado e o programa vai calcular quanto resta para você alcançar a pontuação final.")
print()
pont_final_ano = int(input("Digite a pontuação necessária para passar(anual): "))
materia = input("Digite a matéria: ")
materia = materia.title()
print("A matéria selecionada é: %s" %(materia))
print()
nota1 =  int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
pont_total = int((nota1 + nota2 + nota3 + nota4))
falta_pont_final_ano = (pont_total - pont_final_ano)

if pont_total < pont_final_ano:
	print("Infelizmente você não atingiu a pontuação necessária para passar(anual). Ainda te faltam %s pontos." %(falta_pont_final_ano))
elif pont_total == pont_final_ano:
	print("Parabéns! Você atingiu a pontuação necessária para passar.")
else:
	print("Parabéns! Você ultrapassou a pontuação necessária.")

