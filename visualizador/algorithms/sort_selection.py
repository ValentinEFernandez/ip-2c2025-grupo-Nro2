# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():

    global items, n, i, j, min_idx, fase
    
    #Si i es menor mayor que n significa que el recorrido terminó, por lo tanto retorna "done:true"
    if i >= n:  
        return{"done":True}

    if fase == "buscar":  
        if j < n :
            j_actual = j
            #Compara dos valores de la lista items con indices distintos para saber cual es menor
            if items[j] < items[min_idx]:   
                #si items[j] es menor que items[min_idx], j pasa a ser el nuevo indice donde se encuentra el elemento de menor valor
                min_idx = j  
            j +=1
            return{"a": min_idx, "b": j_actual, "swap": False, "done": False}
        else:
                fase="swap"
    if fase == "swap":
        i_original = i
        min_idx_original = min_idx
        swap_hecho = False
        if min_idx != i:  #verifica que min_idx sea distinto de i, sino el elemento está en la posición correcta
            temp = items[i]
            items[i] = items[min_idx]
            items[min_idx] = temp
            swap_hecho = True   
        i+=1    #i aumenta uno para comparar el proximo valor
        min_idx = i #reinicia el valor de min_idx en el valor de la cabeza de la parte no ordenada
        j = i+1 #pone el valor de j en el siguiente valor de i para compararlos entre si
        fase = "buscar" #reiniciamos la fase en "buscar" para que se reinicie la busqueda
        return{"a":i_original, "b":min_idx_original, "swap":swap_hecho, "done":False}
