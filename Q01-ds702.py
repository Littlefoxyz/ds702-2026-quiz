def f(x):
    z = (x**2) + (2.5*x) - 5
    if z == 0 :
        return print(f"f({x}) is 0")
    else:
        return print(f"f({x}) is not 0")

f(float(input()))