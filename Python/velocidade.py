#Inicialização das variáveis
vo=int(0)
vf=int(0)
to=int(0)
tf=int(0)
delta_v=int(0)
delta_t=int(0)
af=int(0)
goto="Y"
#############################
print("CÁLCULO DE VELOCIDADE (FÍSICA)")

#Quebra de linha
print()

print("Velocidade = km/h")
print("Tempo = segundos")

#Quebra de linha
print()
print()

while goto == "Y":
    vo=int(input("Digite a velocidade inicial: "))
    vf=int(input("Digite a velocidade final: "))

    #Quebra de linha
    print()

    to=float(input("Digite o tempo inicial: "))
    tf=float(input("Digite o tempo final: "))
    #Calcula a variação da velocidade
    delta_v = vf-vo
    #Calcula a variação do tempo
    delta_t = tf-to
    #Retorna o resultado da divisão de delta_v por delta_t
    #e armazena na variável 'af' (aceleração final)
    af=delta_v/delta_t

    #Quebra de linha
    print()
    print("A aceleração é de %.2f m/s" %(af))
    #Quebra de linha
    print()
    goto=input("Calcular de novo? (Y/N): ")
        
else:
    print("Até mais!")

