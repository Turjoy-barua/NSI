import random

my_list = random.sample(range(0, 1000), 800)
print(my_list)

def tri_fusion(T):
    if len(T) <= 1:
        return T
    
    milieu = len(T) // 2
    T1 = tri_fusion(T[:milieu])
    T2 = tri_fusion(T[milieu:])
    
    return fusion(T1, T2)
    
def fusion(T1, T2):
    if not T1:
        return T2
    elif not T2:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]] + fusion(T1[1:], T2)
    else:
        return [T2[0]] + fusion(T1, T2[1:])
    
#print(tri_fusion(my_list))
tri_fusion(my_list)