def max_et_indice(tab):
    max = tab[0]
    for num in tab:
        if num > max:
            max = num
    index = tab.index(max)
    return (max, index)

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print (max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([-2]))
print(max_et_indice([1, 1, 1, 1]))