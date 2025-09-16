def trans_int_char(tab):
    return (list(map(str, tab)))

def val_abs(tab): 
    return(list(map(abs, tab)))

t1 = [1, 2, 3, 4, 5]
print(trans_int_char(t1))

t2 = [-1, +2, -3]
print(val_abs(t2))