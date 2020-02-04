def fibon(n):
    f0 = 0
    f1 = 1
    sum=f0+f1
    for i in range(0, n - 1):
        n_val = f0 + f1
        f0 = f1
        f1 = n_val
        sum=sum+n_val
    return sum
print("sum of the 5th terms: ", fibon(5))
print("sum of the 10th terms: ", fibon(10))


