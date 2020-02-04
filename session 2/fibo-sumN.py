def fibon(n):
    f0 = 0
    f1 = 1
    for i in range(0, n - 1):
        n_val = f0 + f1
        f0 = f1
        f1 = n_val
    return n_val


print("sum of the 5th terms: ", fibon(5))
