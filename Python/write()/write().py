# -*- coding: utf-8 -*-
nome = str(input("Digite o seu nome: "))
filehandle = open('nome-arquivo', 'w', encoding="utf-8")
filehandle.write(nome)
filehandle.close()