def power(x, n):
    if x == 0:
        return 1
    else:
        return x * pow(x, n - 1)

print(power(4, 2))
