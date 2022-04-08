class Pair():
    p = 0
    q = 0

    def Pair(thep, theq):
        p = thep
        q = theq

class Leftside():
    state = 0
    symbol = ''

    def Leftside(st, sym):
        state = st
        symbol = sym

# Input values
Nstates = int(input("Количество состояний: "))
symstr = list(input("Вершины: ").split(' '))
flist = list(input("Список допускающих состояний: ").split(' '))
startingState = int(input("Cтартовое состояние: "))

# Init some values
symbols = list()

for i in range(0, len(symstr)) :
    symbols.append(symstr[i])

favorable = [False for i in range(1, Nstates + 1)]
for items in flist:
    favorable[int(items)] = True


print(symbols)
print(flist)
print(Nstates)