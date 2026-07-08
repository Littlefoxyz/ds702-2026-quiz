def sum_num(a):
    a = int(a)
    n = 0
    for i in range(1,a):
        n = i + n
    print (n)
    return print(f"summation of {a} = {n}")

sum_num(input())