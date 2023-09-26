def summation(number):
    add_number_count = 0

    while (number > 0):
        aux = number%10
        number = number // 10
        add_number_count = add_number_count + aux
    
    return add_number_count
