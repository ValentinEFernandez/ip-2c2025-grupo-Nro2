 # Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    global items, n,i, j  # TODO:
    if i>= n:         # - Si i >= n: devolver {"done": True}.
        return {"done": True}

    if j == None:   # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
        j=i
        return {"a": j-1,"b": j,"swap": False,"done": False}

    if (j > 0) and (items[j-1]>items[j]):     # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
        items[j-1],items[j]=items[j],items[j-1]
        j-=1
        return {"a": j,"b": j+1,"swap": True,"done": False}

    i=i+1                         # - Si ya no hay que desplazar: avanzar i y setear j=None.
    j=None
    return {"a": i-1,"b": i-1,"swap": False,"done": False}
