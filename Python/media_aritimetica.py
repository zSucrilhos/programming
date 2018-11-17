print("CALCULADOR DE MÉDIA ARITIMÉTICA")
print("O programa calcula com base de 4 notas.")
print()
###################################################
materia = str(input("Digite a matéria: "))
materia = str(materia.upper())
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
notas = nota1 + nota2 + nota3 + nota4
media_final = float((nota1 + nota2 + nota3 + nota4)/4)
if media_final < 100:
	falta = int(notas - media_final)
	print("Atualmente você tem %s pontos no total e precisa de %i pontos para passar." %(notas, falta))
print()
print("%s\n\t%s\n\t%s\n\t%s\n\t%s" %(materia, nota1, nota2, nota3, nota4))
print("---------------------")
print("A MÉDIA FINAL É: %.1f" %(media_final))
		