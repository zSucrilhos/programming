lugares_visitar = ["Canadá", "Alemanha", "Japão", "Rússia", "Suíça", "Itália", "Grécia", "França"]
print("Lista original:")
print(lugares_visitar)
print()
print("Ordem alfabética(sorted()):")
print(sorted(lugares_visitar)) #sorted = muda temporariamente para ordem alfabética
print()
print("Ordem original(print()):")
print(lugares_visitar)
print()
print("Ordem reversa(.reverse()):")
lugares_visitar.reverse() #inverte a ordem da lista
print(lugares_visitar)
print()
print("Ordem original(.reverse()):")
lugares_visitar.reverse() #inverte a ordem da lista
print(lugares_visitar) #imprime a lista
print()
print("Ordem alfabética(.sort):")
lugares_visitar.sort() #sort = muda permanentemente para ordem alfabética
print(lugares_visitar)
print()
print("Ordem alfabética inversa(.sort(reverse=True))")
lugares_visitar.sort(reverse=True) #sort = muda permanentemente para ordem alfabética e inverte a ordem da lista
print(lugares_visitar)
