def recu_fibo(n):
   if n <= 1:
       return n
   else:
       print(f"n = {n}")
       return(recu_fibo(n-1) + recu_fibo(n-2))
   
   
   
print(recu_fibo(30))