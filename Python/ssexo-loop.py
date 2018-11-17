sexo = input("Digite seu sexo [M/F]: ").strip().upper()[0]
while sexo not in "MmFf":
	sexo = input("Dado inválido, por favor, digite seu sexo [M/F]: ").strip().upper()[0]
print("Dado registrado com sucesso!")
	
