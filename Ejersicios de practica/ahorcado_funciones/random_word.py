import random

word_list = ["COMPUTADORA", "AVION", "COMSOS", "MATEMATICA", "TELEVISOR", "TIROTEO", "GUERRERO", "SERENATA", "CAMALEON"]

def random_word():
    select_word = word_list[random.randint(0, len(word_list))]
    return select_word


