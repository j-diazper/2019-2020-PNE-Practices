# Session 02- Exercise 01 Fibonacci first 11 terms
f0=0
f1=1
for i in range(0,11):
    print(f0,end=" ")
    n_val= f0+f1
    f0=f1
    f1=n_val


