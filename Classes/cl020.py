def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 2, 1, 6]
dobra(valores)
print(valores)