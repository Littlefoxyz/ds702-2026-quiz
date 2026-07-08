
L=[]
for c in input("Please enter a string : "):
    num = ord(c) + 1
    L.append(chr(num))
print(f"The plus one cypher is " + "".join(L))