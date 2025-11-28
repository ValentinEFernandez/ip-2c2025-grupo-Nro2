# algorithms/sort_shell.py

items = []
n = 0

# Estado interno del Shell Sort
gap = 0
i = 0
j = 0
temp = 0
stage = "gap"
done = False


def init(vals):
    global items, n, gap, i, j, temp, stage, done

    items = list(vals)
    n = len(items)

    gap = n // 2
    i = 0
    j = 0
    temp = 0
    stage = "gap"
    done = False


def step():
    global items, n, gap, i, j, temp, stage, done

    if done:
        return {"done": True}

    # 1) Cambiar de gap
    if stage == "gap":
        if gap == 0:
            done = True
            return {"done": True}

        i = gap
        stage = "i_loop"
        return {"a": 0, "b": 0, "swap": False, "done": False}

    # 2) Loop de i
    if stage == "i_loop":
        if i >= n:
            gap //= 2
            stage = "gap"
            return {"a": 0, "b": 0, "swap": False, "done": False}

        temp = items[i]
        j = i
        stage = "shift"
        return {"a": j, "b": j - gap, "swap": False, "done": False}

    # 3) Corrimientos (shift)
    if stage == "shift":
        if j >= gap and items[j - gap] > temp:
            items[j] = items[j - gap]
            old_j = j
            j -= gap
            return {"a": old_j, "b": j, "swap": True, "done": False}
        else:
            stage = "insert"
            return {"a": j, "b": j - gap, "swap": False, "done": False}

    # 4) Insertar temp
    if stage == "insert":
        items[j] = temp
        i += 1
        stage = "i_loop"
        return {"a": j, "b": i, "swap": False, "done": False}

    # Seguridad
    return {"done": False}
