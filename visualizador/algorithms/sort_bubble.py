items = []
n = 0
i = 0
j = 0


def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0


def step():
    global items, n, i, j

    if i >= n:
        return {"done": True}

    if j < n - 1 - i:
        a = j
        b = j + 1
        swap = False

        if items[a] > items[b]:
            temp = items[a]
            items[a] = items[b]
            items[b] = temp
            swap = True

        j += 1
        return {"a": a, "b": b, "swap": swap, "done": False}

    else:
        j = 0
        i += 1
        return {"a": -1, "b": -1, "swap": False, "done": False}
