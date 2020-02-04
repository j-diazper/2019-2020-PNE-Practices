
def fibon(n):
    f0 = 0
    f1 = 1
    for i in range(0,n-1):
        n_val= f0+f1
        f0=f1
        f1=n_val
    return f1
print("5th fibonacci element: ",fibon(5))
print("10th fibonacci element: ",fibon(10))
print("15th fibonacci element: ",fibon(15))

