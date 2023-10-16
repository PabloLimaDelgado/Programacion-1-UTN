import random

#EJERCICIO 2
def delet_number(numeros):
    condition = False
    num = int(input("Ingrese un numero: "))
    for i in numeros:
        if (i == num):
            numeros.remove(i)
            condition = True
        else:
            condition = False
    if (condition == True):        
        print(f"Se elimino el numero {num} de la lista")
    else:
        print("No se encontro el numero en la lista") 

#EJERCICIO 3
def sum_numbers(numeros):
    sum = 0
    for i in numeros:
        sum += i
    return sum

#EJERCICIO 4
def num_minors(numeros):
    list_minors = []

    num = int(input("Ingrese un numero: "))

    for i in numeros:
        if (i < num):
            list_minors.append(i)

    return f"Los elemntos de la lista menores a {num} son: {list_minors}"

#EJERCICIO 5
def fill_list(list_len):

    list = []

    for i in range(list_len):
        list.append(random.randint(0, 10))

    return list

#EJERCICIO 6
def show_names(list_primary, list_secondary):
    list_aux_primary = []
    list_aux_secondary = []

    for name in list_primary:
        if name not in list_aux_primary:
            list_aux_primary.append(name)
    
    for name in list_secondary:
        if name not in list_aux_secondary:
            list_aux_secondary.append(name)

    print(f" Los nombres sin repetir de la primaria son: {list_aux_primary}")
    print(f" Los nombres sin repetir de la secundaria son: {list_aux_secondary}")

def show_names_repeted_list(list_primary, list_secondary):
    list_aux = []
    list_name_no_repeted = []

    for name in list_primary:
        for name in list_secondary:
            if name in list_primary and name in list_secondary:
                list_aux.append(name)

    for name in list_aux:
        if name not in list_name_no_repeted:
            list_name_no_repeted.append(name)

    print(f" Los nombres que se repiten en ambas listas son {list_name_no_repeted}")

def show_names_repeted_list_primary(list_primary, list_secondary):
    list_name_no_repeted = []

    for name in list_primary:
        if name not in list_secondary and name not in list_name_no_repeted:
            list_name_no_repeted.append(name)

    print(f"Los nombres en nivel primario que no se repiten en los de nivel secundario: {list_name_no_repeted}")

#EJERCICIO 8
def resultado_final(matrix):
    i = 0
    n = 0
    o = 0
    r = 0

    while (i < 4):
        goles_favor = 0
        goles_contra = 0

        ganados = 0
        perdidos = 0
        empatados = 0
        puntos = 0

        n = 0
        o = 0

        while (o < 4):
            if (matrix[i][n] > matrix[o][r]) and (i != n):
                ganados += 1
                goles_favor += matrix[i][n]
                goles_contra += matrix[o][r]
                puntos += 3

            elif (matrix[i][n] < matrix[o][r]) and (i != n):
                perdidos += 1
                goles_favor += matrix[i][n]
                goles_contra += matrix[o][r]
                puntos += 0

            elif (matrix[i][n] == matrix[o][r]) and (i != n):
                empatados+=1
                goles_favor+=matrix[i][n]
                goles_contra += matrix[o][r]
                puntos+=1

            o+=1
            n+=1

        if (i == 0):
            matriz_equipo1 = [[f"Ha ganado {ganados} partidos",f"Ha perdido {perdidos} partidos",f"Ha empatado {empatados}"],[f"Tiene una diferencia de goles de:{goles_favor-goles_contra} "],[puntos]]
        elif (i == 1):
            matriz_equipo2 = [[f"Ha ganado {ganados} partidos",f"Ha perdido {perdidos} partidos",f"Ha empatado {empatados}"],[f"Tiene una diferencia de goles de:{goles_favor-goles_contra} "],[puntos]]
        elif (i == 2):
            matriz_equipo3 = [[f"Ha ganado {ganados} partidos",f"Ha perdido {perdidos} partidos",f"Ha empatado {empatados}"],[f"Tiene una diferencia de goles de:{goles_favor-goles_contra} "],[puntos]]
        elif (i == 3):
            matriz_equipo4 = [[f"Ha ganado {ganados} partidos",f"Ha perdido {perdidos} partidos",f"Ha empatado {empatados}"],[f"Tiene una diferencia de goles de:{goles_favor-goles_contra} "],[puntos]]
        
        r+=1
        i+=1

    print(f"""Equipo 1: {matriz_equipo1}
            Equipo 2: {matriz_equipo2}
            Equipo 3: {matriz_equipo3}
            Equipo 4: {matriz_equipo4}""")
    
    tabla_posicion = {
        "Equipo 1": matriz_equipo1[2][0],"Equipo 2": matriz_equipo2[2][0],"Equipo 3": matriz_equipo3[2][0],"Equipo 4": matriz_equipo4[2][0]}

    for m,n in tabla_posicion.items():
        print (f"{m} Puntos: {n}", end= " ")
        print(" ")

def equipos_resultado():
    matriz_resultados = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    i = 0
    n = 0

    while (i < 4):
        n = 0

        while (n < 4):
            if (i+1 != n+1):
                matriz_resultados[i][n] = int(input(f"Cuantos goles hizo el equipo {i+1} contra el equipo {n+1} : "))
            n+=1
        i+=1
    return(matriz_resultados)

#EJERCICIO 9
def juego_memo(matriz_memo):
    matriz_encript = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matriz_aux1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    while (matriz_encript != matriz_memo):
            
        matriz_aux1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        fil_option = input("Ingrese el número de la fila que desea (1 al 4): ")
        colum_option = input("Ingrese el número de la columna que desea (1 al 4): ")
        
        while (fil_option != "1" and fil_option != "4" and fil_option != "2" and fil_option != "3" ) or (colum_option != "4" and colum_option != "1" and colum_option != "2" and colum_option != "3"):
            fil_option = input("Ingrese el número de la fila que sea correcto (0 al 3): ")
            colum_option = input("Ingrese el número de la columna que sea correcto (0 al 3): ")
    
            
        fil_option = int(fil_option) - 1
        colum_option = int(colum_option) - 1
        value_option1 = 0
            
        value_option1 = matriz_memo[fil_option][colum_option]
        
        matriz_aux1[fil_option][colum_option] = value_option1


        for i in matriz_aux1:
            for n in i:
                print(n, end= "     ")
            print(" ")
        
        fil_option2 = input("Ingrese el número de la fila que desea (1 al 4): ")
        colum_option2 = input("Ingrese el número de la columna que desea (1 al 4): ")
        
        while(fil_option2 != "4" and fil_option2 != "1" and fil_option2 != "2" and fil_option2 != "3" ) or (colum_option2 != "4" and colum_option2 != "1" and colum_option2 != "2" and colum_option2 != "3"):
        
            fil_option2 = input("Ingrese el número de la fila que sea correcto (0 al 3): ")
            colum_option2 = input("Ingrese el número de la columna que sea correcto (0 al 3): ")
    
        fil_option2 = int(fil_option2) -1
        colum_option2 = int(colum_option2) -1
        value_option2 = 0
        value_option2 = matriz_memo[fil_option2][colum_option2] 
        matriz_aux1[fil_option2][colum_option2] = value_option2
        for i in matriz_aux1:
            for n in i:
                print(n, end= "     ")
            print(" ")

        if value_option1 == value_option2:
            print("Conseguiste un par")
            matriz_encript[fil_option][colum_option] = value_option1
            matriz_encript[fil_option2][colum_option2] = value_option2
        elif value_option2 != value_option1:
            print("No coinciden las cartas")
        
        for i in matriz_encript:
            for n in i:
                print(n, end = "     ")
            print(" ")
    
    return "Felicidadeees, ganaste el juego!!!!!!" 
       
def concurrencia_memo(matriz, num):
    count1 = 0
    for i in matriz:
        for n in i:
            if n == num:
                count1+=1
    return count1

def make_memo():
    memo =[[],[],[],[]]
    while concurrencia_memo(memo,1) != 2:
        num_random=random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(1)
            
    while concurrencia_memo(memo,2) != 2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(2)
            
    while concurrencia_memo(memo,3)!=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(3)
            
    while concurrencia_memo(memo,4) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(4)
            
    while concurrencia_memo(memo,5) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(5)
            
    while concurrencia_memo(memo,6) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(6)
            
    while concurrencia_memo(memo,7) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(7)
            
    while concurrencia_memo(memo,8) !=2:
        num_random = random.randint(0,3)
        if len(memo[num_random]) < 4:  
            memo[num_random].append(8)
    return memo

#EJERCICIO 10
def matriz_inDiagonal(mat):
    colum = len(mat[0])
    fil = len(mat)
    n = 0
    diagonal_real = []
    diagonal = []
    list_aux = []
    d = 0
    v = len(mat[0])
    invert_diagonal = []
    invert_diagonal_real = []

    if (fil < colum): 
        return "La matriz ingresada no tiene la misma cantidad de filas y columnas"
    
    for i in mat:
        for l in i:
            list_aux.append(0)
        diagonal.append(list_aux)
        invert_diagonal.append(list_aux)
        list_aux = []
        
    for i in mat:
        diagonal_real.append(i[d])
        invert_diagonal_real.append(i[v-1])
        d+=1
        v-=1

    v = len(mat[0])-1
    for i in mat:
        for m in diagonal:
            if i[n] in diagonal_real:
                m[n] = i[n]      
            n+=1  
        n = 0
        
    for i in mat:
        for m in invert_diagonal:
            if i[v] in invert_diagonal_real:
                m[v] = i[v]      
            v-=1  
        v = len(mat[0])-1
        
    for r in diagonal:
        for element in r:
            print(element, end=" ")
        print(" ") 