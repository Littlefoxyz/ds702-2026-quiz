# a % b =c
# b % c = d
# c % d

#n = 126 % 45
#m = 45 % n
#n = n % m

L=[]
max = input("max number : ")
min = input("min number : ")

def GCD(a, b):
    a = int(a)
    b = int(b)

    while b > 0:
        L.append(b)
        n = a % b
        a = b
        b = n
    return print(f"GCD of : {max} , {min} = {(L[-1])}")

GCD(max,min)