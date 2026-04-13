<<<<<<< HEAD
(base) ➜  NSI git:(main) ✗ cd test
(base) ➜  test git:(main) ✗ python3 test.py 
(base) ➜  test git:(main) ✗ python3 test.py
(base) ➜  test git:(main) ✗ 

=======
from random import randint
def echange(lst, i1, i2):
    lst[i2] = lst[i1]
    lst[i1] = lst[i2] 
    return(lst)
def melange(lst, ind):
    print(lst)
    if ind > 0:
        j = randint(0, ind)
        echange(lst, ind, j)
        melange(lst, ind-1) 
print(echange([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 0, 1))
>>>>>>> 2c7816adbbd542bd4591dd4582199901a52cf9b0
