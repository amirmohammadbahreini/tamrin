x = 2**1444

print(x)

x2 = str(x)
print(type(x2))
print(len(x2))

del x, x2

x = 8+ 3j

print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())

y = 2**14
print(y)
print(round(y,-4))


del x, y

x = 10_000_000_000_000_000
print(x)

t = 125
T = str(t)
print(T[0], T[1], T[2])
x =float(x)
print(isinstance(x,float))

################################################################

wazn = int(input('wazn'))
ghad = int(input('ghad'))

BMI = wazn/pow(ghad, 2)
print(BMI)

################################################################

list = '     amir mohammad bahreini'

print(list.upper())

print(list.count(' '))
print(list.endswith(''))
print(list.rfind(''))


