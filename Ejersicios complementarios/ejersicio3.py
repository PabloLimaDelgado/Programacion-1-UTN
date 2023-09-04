import math

#EJERSICIO 1
'''abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
frase = []
frase_codificada = []
lista_aux = []
string_final = ""

corrimiento_lugares = int(input("Ingrese la cantidad de lugares que desea correr los mensajes a encriptar: "))

for i in range(5):
    frase_sola = input("Ingrese el mensaje desencriptado: ").upper()

    frase.append(frase_sola)
    frase_codificada.append("")

    for j in range(len(frase_sola)):
        aux = abecedario.index(frase_sola[j])

        lista_aux.append(frase_sola[j])

        if aux == 27:
            lista_aux[j] = abecedario[27]
        else:
            lista_aux[j] = abecedario[(aux + corrimiento_lugares)%27]
        
        string_final += lista_aux[j]
    
    frase_codificada[i] = string_final
    string_final = ""


for m in range(len(frase)):
    print(f"La frase {m} sin codificar es",frase[m], end=" ")
    print(f"La frase {m} codificada es",frase_codificada[m], end=" ")
    print("\n")'''

#EJERSICIO 2
'''contador_digitos_impares = 0
contador_digitos_pares= 0
num = int(input("Ingrese un número positivo: "))

while (num!=0):
    if(num == 0):
        break

    while num > 0:
        aux = num%10
        num = num // 10
        if (aux%2 == 0):
            contador_digitos_pares += 1
        else:
            contador_digitos_impares += 1
    
    num = int(input("Ingrese un número positivo: "))


print(f"La cantiad de digitos pares es: {contador_digitos_pares}")
print(f"La cantiad de digitos impares es: {contador_digitos_impares}")'''
    






