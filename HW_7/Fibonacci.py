#Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію (25 балів)
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 5
# check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# else:
print(recur_fibo(nterms))

print("Fibonacci sequence:")
for i in range(nterms):
   print("i={0}, fibo={1}".format(i, recur_fibo(i)))

