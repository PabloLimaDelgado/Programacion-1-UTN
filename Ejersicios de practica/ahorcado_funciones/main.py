import random_word, find_word

selected_word = random_word.random_word()
number_of_errors = 0
aux_word = "_" * len(selected_word)
chosen_word_aux = selected_word

print(f"La palabra secreta es: {aux_word}")

while(number_of_errors < 6):
    new_word = ""
    if(selected_word == ""):
        print(f"Felicitaciones encontro la palabra {chosen_word_aux}")
        break

    letter = input("Ingrese una letra: ").upper()

    while(len(letter) != 1):
        letter = input("Incorrecto solo ingrese una letra: ").upper()

    error = find_word.letter_correct(letter, selected_word)

    if(error == 1):
        number_of_errors += 1
        print(f"Intento incorrecto le quedan {6 - number_of_errors} intentos")
        print(aux_word) 
    else:
        for index, char in enumerate(selected_word):
            if char != letter:
                new_word += char

        for index, char in enumerate(chosen_word_aux):
            if char == letter:
                aux_word = aux_word[:index] + char + aux_word[index + 1:]

        print(aux_word)
        selected_word = new_word 

if(number_of_errors == 6):
    print(f"Lo lamento ha perdido, la palabra correcta era {chosen_word_aux}")
