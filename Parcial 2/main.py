'''Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
Te ha contratado a ti para que desarrolles un programa que detecte si un humano es mutante basándose 
en su secuencia de ADN. Para eso te ha pedido crear un programa con un método o función booleana, 
llamada is_mutant(dna), que recibe como parámetro un arreglo de Strings que representan cada 
fila de una matriz 6x6 con la secuencia de ADN. Las letras de los Strings solo pueden ser: A,T,C,G; 
las cuales representan cada base nitrogenada del ADN. Sabrás si un humano es mutante, si encuentras 
más de una secuencia de cuatro letras iguales, estas pueden aparecer de forma oblicua, horizontal o 
vertical.'''

import func.funcions
adn = [] #LISTA DE GENES

#example_adn_mutant = ["TGAAGT", "ACAAGC", "AATTAC", "GTTACA", "CTCTTA", "ACCCCT"]
#example_adn_human = ["AAAAGA", "AAGTGC", "ATATTT", "GGACGG", "GCGTCA", "TCACTG"]

func.funcions.fill_matrix(adn)
func.funcions.show_matrix(adn)
print(func.funcions.all_gene_verification(adn))

#print(func.funcions.all_gene_verification(example_adn_mutant))
#print(func.funcions.all_gene_verification(example_adn_human))