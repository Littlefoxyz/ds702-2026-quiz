# a % b =c
# b % c = d
# c % d

#n = 126 % 45
#m = 45 % n
#n = n % m
L=[]
def GCD(a,b):
    a = int(a)
    b = int(b)
    n = a % b
    while n > 0:
        n = b % n
        L.append(n)
    print(f"GCD of : {a} , {b} = {(L[-2])}")

GCD(input("max number : "),input("min number : "))
