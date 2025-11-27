# Insertion Sort
items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # Comienza en el segundo elemento
    j = None

def step():
    global items, n,i, j 

    #Fin del algoritmo:
    if i>= n:
        return {"done": True}

    #Inicia el desplazamiento de items[i]:
    if j == None:
        j=i
        return {"a": j-1,"b": j,"swap": False,"done": False}
    
    #Mientras haya items que desplazar:
    if (j > 0) and (items[j-1]>items[j]):
        items[j-1],items[j]=items[j],items[j-1]
        j-=1
        return {"a": j,"b": j+1,"swap": True,"done": False}
    
    #Concluye el desplazamiento y avanzamos i:
    i+=1
    j=None
    return {"a": i-1,"b": i-1,"swap": False,"done": False}
