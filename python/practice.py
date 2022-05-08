import random as r
name = input('give me the name: ')
num  = int(input('now give me the num: '))
v=r.randint(0,10)
num+=v
print('hello ' + name + ' the type of ur name is: ' + str(type(name))+ 'and ur new num is: ' + str(num))

print("#"*30)

print(bin(10),oct(10),hex(10))
print(format(10,'b'),format(10,'o'),format(10,'x'))
print(int("1010",2),int('0o12',8),int('0xa',16))

print("#"*30)

if name == "mahmoud":
    print('hello dear ')
elif name == "anas":
    print("hello bro")
else:
    print("hello anyway")

print("#"*30)

mylst=[]
while v<num:
    g=input('give me a name man: ')
    mylst.append(g)
    v+=1

print("#"*30)

for j in mylst:
    print(j)

print("#"*30)

# ===================== RANGE/alpha =========================
for i in range(ord('a'),ord('z')+1):
    print(chr(i))

print("#"*30)

# ====================== SLICING ===========================
print(name[::1]) #start end step

# ========================= CENTER ==========================
print(name.center(10,"#"))

#   =======================FORMATTING====================
print('my name is: %s and my num is: %d '%(name,num)) # %.3f .... %.5s

print( 'my name is {} and my num is {:,d}' .format(name,10000000)) #////
print( 'my num is {1:d} and my name is {0}' .format(name,num)) #////

print(f"my name is : {name} and my num is: {num}")