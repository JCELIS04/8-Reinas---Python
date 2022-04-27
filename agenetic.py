import random
import matplotlib.pyplot

# Población de generación inicial, la capacidad de población es 4, para mejorar la eficiencia de iteración, los 8 códigos de la población inicial son diferentes
def Initiate(a):
    while len(a)<8:
        b=random.randint(1,8)
        if not(b in a):
            a.append(b)
    return a

# Cálculo del estado físico, es decir, grado sin ataque. Si una reina no ataca a las otras reinas, el grado de no ataque es 8-1 = 7. La condición de terminación es que la suma del grado de no ataque de las 8 reinas es 8 * 7/2 (considerando cálculos repetidos)
def FitnessFunction(list):
    FitnessIndex=[28,28,28,28]
    for i in range(0, 4):
        for j in range(0, 7):
            for k in range(j+1, 8):
                if list[i][j]==list[i][k]:
                    FitnessIndex[i] -= 1
                if list[i][j]-list[i][k] == j-k or list[i][j]-list[i][k] == k-j:
                    FitnessIndex[i] -= 1
    fitness = {'a': FitnessIndex[0], 'b': FitnessIndex[1], 'c': FitnessIndex[2], 'd': FitnessIndex[3]}
    return fitness

# Seleccione el operador principal, use la selección competitiva aquí
def ChooseParents(a,b,c,d):
    stack=[]
    stack.append(a)
    stack.append(b)
    stack.append(c)
    stack.append(d)
    fitness = FitnessFunction(stack)
    sort=sorted(fitness.items(), key=lambda e : e[1], reverse=True)
    if sort[0][0] == 'a':
        firstfather = a
    elif sort[0][0] == 'b':
        firstfather = b
    elif sort[0][0] == 'c':
        firstfather = c
    else:
        firstfather = d
    if sort[1][0] == 'a':
        firstmother = a
    elif sort[1][0] == 'b':
        firstmother = b
    elif sort[1][0] == 'c':
        firstmother = c
    else:
        firstmother = d
    parents=[]
    parents.append(firstfather)
    parents.append(firstmother)
    parents.append(firstfather)
    if sort[0][0] == 'a':
        secmother = a
    elif sort[0][0] == 'b':
        secmother = b
    elif sort[0][0] == 'c':
        secmother = c
    else:
        secmother = d
    parents.append(secmother)
    return parents

Operador #Cross, este programa usa cross secuencial
def cross(parents):
    children = []
    crosspoint=random.randint(1,7)
    firstfather,firstmother,secfather,secmother=parents[0],parents[1],parents[2],parents[3]
    ch1 = firstfather[0:crosspoint]
    ch1.extend(firstmother[crosspoint:])
    ch2 = firstmother[0:crosspoint]
    ch2.extend(firstfather[crosspoint:])
    ch3 = secfather[0:crosspoint]
    ch3.extend(secmother[crosspoint:])
    ch4 = secmother[0:crosspoint]
    ch4.extend(secfather[crosspoint:])
    children.append(ch1)
    children.append(ch2)
    children.append(ch3)
    children.append(ch4)
    return children

# Mutación, la mutación de intercambio se usa aquí
def mutation(children):
    muchildren=[]
    mtpoint1=random.randint(0,7)
    mtpoint2=random.randint(0,7)
    ch1, ch2, ch3, ch4 = children[0], children[1], children[2], children[3]
    ch1[mtpoint1], ch1[mtpoint2] = ch1[mtpoint2], ch1[mtpoint1]
    mtpoint1=random.randint(0,7)
    mtpoint2=random.randint(0,7)
    ch2[mtpoint1], ch2[mtpoint2] = ch2[mtpoint2], ch2[mtpoint1]
    mtpoint1=random.randint(0,7)
    mtpoint2=random.randint(0,7)
    ch3[mtpoint1], ch3[mtpoint2] = ch3[mtpoint2], ch3[mtpoint1]
    mtpoint1=random.randint(0,7)
    mtpoint2=random.randint(0,7)
    ch4[mtpoint1], ch4[mtpoint2] = ch4[mtpoint2], ch4[mtpoint1]
    muchildren.append(ch1)
    muchildren.append(ch2)
    muchildren.append(ch3)
    muchildren.append(ch4)
    return muchildren


a,b,c,d=[],[],[],[]
Initiate(a)
Initiate(b)
Initiate(c)
Initiate(d)
parents=ChooseParents(a,b,c,d)
# Para evitar que el programa caiga en un bucle infinito, establezca el número máximo de reproducciones
maxGenerations=100000
generations=0
for i in range(maxGenerations):
    cparents=cross(parents)
    mparents=mutation(cparents)
    generations+=1
    fitness = FitnessFunction(mparents)
    if fitness['a'] == 28 or fitness['b'] == 28 or fitness['c'] == 28 or fitness['d'] == 28:
        answer = []
        if fitness['a'] == 28:
            answer.append(mparents[0])
        if fitness['b'] == 28:
            answer.append(mparents[1])
        if fitness['c'] == 28:
            answer.append(mparents[2])
        if fitness['d'] == 28:
            answer.append(mparents[3])
        print("This answer is {0}".format(answer))
        print("Find if after {0} times".format(generations))
        # Visualización de soluciones factibles
        for i in answer:
            y=[i.index(1)+0.5, i.index(2)+0.5, i.index(3)+0.5, i.index(4)+0.5, i.index(5)+0.5, i.index(6)+0.5, i.index(7)+0.5, i.index(8)+0.5]
        x=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
        matplotlib.pyplot.title("Using Genetic Algorithm to Solve 8-Queens' Problem")
        matplotlib.pyplot.axis([0,8,0,8])
        matplotlib.pyplot.grid()
        matplotlib.pyplot.plot(x, y, '*')
        matplotlib.pyplot.show()
        break
    else:
        parents=mparents
if maxGenerations==generations and answer==[]:
    print("Cannot find the answer")
