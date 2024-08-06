class my_class(object):
    pass
# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]

# Adicionando um elemento � lista
minha_lista.append(6)

# Ordenando a lista (embora j� esteja ordenada neste caso)
minha_lista.sort()
print("Lista ordenada:", minha_lista)

# Criando uma nova lista para concatenar
outra_lista = [7, 8, 9]

# Concatenando as listas
lista_concatenada = minha_lista + outra_lista
print("Lista concatenada:", lista_concatenada)

# Fatiando a lista
fatia1 = lista_concatenada[0:3]  # Do in�cio at� o terceiro elemento (n�o inclusivo)
fatia2 = lista_concatenada[3:]   # Do quarto elemento at� o final
fatia3 = lista_concatenada[-3:]  # �ltimos tr�s elementos

print("Fatia 1 (primeiros tr�s elementos):", fatia1)
print("Fatia 2 (do quarto elemento at� o final):", fatia2)
print("Fatia 3 (�ltimos tr�s elementos):", fatia3)




