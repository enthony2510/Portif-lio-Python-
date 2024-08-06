class my_class(object):
    pass
# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]

# Adicionando um elemento à lista
minha_lista.append(6)

# Ordenando a lista (embora já esteja ordenada neste caso)
minha_lista.sort()
print("Lista ordenada:", minha_lista)

# Criando uma nova lista para concatenar
outra_lista = [7, 8, 9]

# Concatenando as listas
lista_concatenada = minha_lista + outra_lista
print("Lista concatenada:", lista_concatenada)

# Fatiando a lista
fatia1 = lista_concatenada[0:3]  # Do início até o terceiro elemento (não inclusivo)
fatia2 = lista_concatenada[3:]   # Do quarto elemento até o final
fatia3 = lista_concatenada[-3:]  # Últimos três elementos

print("Fatia 1 (primeiros três elementos):", fatia1)
print("Fatia 2 (do quarto elemento até o final):", fatia2)
print("Fatia 3 (últimos três elementos):", fatia3)




