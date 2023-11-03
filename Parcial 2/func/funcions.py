#FUNCION QUE LLENA Y VERIFICA LAS CADENAS DE LOS GENES
def fill_matrix(adn):
    num_aux = 0

    while(num_aux <= 5): #BUCLE QUE ITERA HASTA CREAR LA 'MATRIZ' 6x6 DEL ADN
        adn_string = input("Ingrese la cadena de genes: ").upper() #CADENA DE GENES Y LO CONVERTIMOS A MAYUS
        valid = True

        #IF PARA VERIFICAR QUE LA CADENA TENGA 6 CARACTERES Y LOS GENES SEAN LOS CORRECTOS
        if(len(adn_string) == 6):
            for adn_aux in adn_string:
                if (not(adn_aux == "A" or adn_aux == "T" or adn_aux == "C" or adn_aux == "G")):
                    valid = False
                    print("Cadena de caracteres incorrecta")
                    break

            if (valid):
                adn.append(adn_string)
                num_aux += 1
            else:
                continue
        else:
            print("Cadena de caracteres incorrecta, la cadena debe ser de 6 caracteres: ")
            continue

#FUNCION QUE TRANSPONE LA MATRIZ DE GENES
def gene_transposed_matrix(adn):
    transpoded_adn = [] 

    #VA ITERANDO LA MATRIZ TRANSPUESTA CON LOS VALORES DE LA MATRIZ ORIGINAL PERO REEMPLAZANDO LAS FILAS POR COLUMNAS
    for i in range(len(adn)):
        adn_string = ""
        for j in range(len(adn[0])):
            adn_string += adn[j][i]
        
        transpoded_adn.append(adn_string)

    #RETORNA LA MATRIZ TRANSPUESTA
    return transpoded_adn

#FUNCION QUE VERIFICA QUE NO HAYAN GENES REPETIDOS HORIZONTALES
def horizontal_gene_verification(adn):

    counter_genes = 0
    for adn_aux in adn:
        counter = 0 

        for i in range(len(adn_aux) - 1): #ITERA LA MATRIZ POR FILAS Y REVISA CADA STRING
            current_gene = adn_aux[i]
            next_gene = adn_aux[i + 1]

            if (current_gene == next_gene):
                counter += 1
                if (counter >= 3):  # VERIFICA SI HAY 4 GENES CONSECUTIVOS
                    counter_genes += 1
            else:
                counter = 0

    return counter_genes

#FUNCION QUE VERIFICA QUE NO HAYAN GENES REPETIDOS VERTICALES
def vertical_gene_verification(adn):

    #PRIMERO OBTENGO LA MATRIZ TRANSPUESTA Y DESPUES VERIFICO SI LAS FILAS DE ESA MATRIZ SE REPITE 4 VECES ALGUN GEN
    adn_aux = gene_transposed_matrix(adn)
    value = horizontal_gene_verification(adn_aux)
    
    return value

#FUNCION QUE VERIFICA TODAS LAS DIAGONALES DE LA MATRIZ DE GENES
def diagonals_gene_verification(adn):

    main_diagonal = diagonal_gene_verification(adn, 0, 0)
    up_main_diagonal_long = diagonal_gene_verification(adn, 0, 1)
    up_main_diagonal_short = diagonal_gene_verification(adn, 0, 2)
    down_main_diagonal_long = diagonal_gene_verification(adn, 1, 0)
    down_main_diagonal_short = diagonal_gene_verification(adn, 2, 0)

    #DEVUELVE LA CANTIDAD DE DIAGONALES MUTANTE
    return main_diagonal + up_main_diagonal_long + up_main_diagonal_short + down_main_diagonal_long + down_main_diagonal_short

#FUNCION QUE COPIA EN ESPEJO LA MATRIZ ASI LAS DIAGONALES CONTRARIAS QUEDAN COMO LAS ORIGINALES
def opposite_gene_diagonals_verification(adn):
   return diagonals_gene_verification(adn[::-1]) #::-1 REFLEJA CADA FILA

#FUNCION QUE VERIRICA SOLO UNA DIAGONAL DE LA MATRIZ DE GENES
def diagonal_gene_verification(adn, row, col):
    rows = len(adn)
    cols = len(adn[0])

    #ITERA LAS FILAS Y COLUMNAS SEGUN DESDE DONDE EMPIEZE LA DIAGONAL
    while((row < rows - 3) and (col < cols - 3)):

        #SI SE REPITE 4 VECECS ALGUN GEN DEVUELVE 1
        if((adn[row][col] == adn[row+1][col+1]) and (adn[row][col] == adn[row+2][col+2]) and (adn[row][col] == adn[row+3][col+3])):
            return 1
        
        row += 1
        col += 1
    
    return 0

#FUNCION QUE VERIFICA TODAS LAS POSIBILIDADES DE QUE SEA UN ADN MUTANTE O NO
def all_gene_verification(adn):
    adn_horizontal = horizontal_gene_verification(adn)
    adn_vertical = vertical_gene_verification(adn)
    adn_diagonals_gene_verification = diagonals_gene_verification(adn)
    adn_opposite_diagonals_gene_verification = opposite_gene_diagonals_verification(adn)

    if((adn_horizontal + adn_vertical + adn_diagonals_gene_verification + adn_opposite_diagonals_gene_verification) >= 2):
        return True
    else:
        return False
#FUNCION QUE MUESTRA LA MATRIZ
def show_matrix(adn):

    for i in range(len(adn)):
        for j in range(len(adn[0])):
            print(adn[i][j], end= " ")
        print(" ")
