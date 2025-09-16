from functools import reduce

def addition(a, b):
    return(a+b)


t = [1, -3, 3, 4, -10]
print(f"addition = {reduce(addition, t)}")


def min(a, b):
    if a < b:
        return a
    else:
        return b

print(f"min = {reduce(min, t)}")