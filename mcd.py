import timeit


#Cuantficador Universal Para Todo. tema de Matematicas Discretas
def paraTodo(P, L):
    if L == []:
        return True
    elif P(L[0]):
        return paraTodo(P, L[1:])
    else:
        return False

#Cuantficador Universal Existe Un. tema de Matematicas Discretas
def existeUn(P,L):
    if L == []:
        return False
    elif P(L[0]):
        return True
    else:
        return existeUn(P, L[1:])
 
#metodo recursivo para calcular el MCD 
#MCD_B recibe una lista L, un numero n y una lista res (primos divisibles)        
def MCD_B(L,n,res):
   # print(L,n,res)
    if paraTodo(lambda x: x%n == 0, L):
        return MCD_B(list(map(lambda x: x/n, L)), n, res+[n])
    elif n == L[0] or n > L[0]:
        resultado = 1
        for elemento in res:
            resultado *= elemento
        return resultado   
    elif n == 2:
        n += 1
        return MCD_B(L, n, res) 
    elif n > 2:
        n += 2
        return MCD_B(L, n, res)
            
#=======MEJORA======
def es_primo(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n,divisor+1)

#MCD_C recibe una lista L, un numero n
def MCD_C(L,n,mult=1):
    ##print(mult)
    if paraTodo(lambda x: x==L[0], L[1:]):
        return L[0]
    if existeUn(es_primo, L) or existeUn(lambda x: n >= x,L):        
        return mult
    elif paraTodo(lambda x: x%n == 0, L):        
        return MCD_C(list(map(lambda x: x//n, L)), n, mult * n)      
    elif n == 2:              
        return MCD_C(L, n + 1, mult) 
    else:
        return MCD_C(L, n + 2, mult)
    
#MCD Auclides
def MCD_euclides(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

#MCD recibe una lista de numeros            
def MCD_V1(L):
    return MCD_B(L,2,[])

#MCD Mejorado recibe una lista de numeros
def MCD_V2(L):
    #L.sort()
    return MCD_C(L,2)
    
def MCD_Stein(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if a % 2 == 0 and b % 2 == 0:
        return 2 * MCD_Stein(a // 2, b // 2)
    elif a % 2 == 0:
        return MCD_Stein(a // 2, b)
    elif b % 2 == 0:
        return MCD_Stein(a, b // 2)
    else:
        if a > b:
            return MCD_Stein((a - b) // 2, b)
        else:
            return MCD_Stein((b - a) // 2, a)


q = 9997
w = 999
itera = 10
tiempo_promedio = timeit.timeit(lambda: MCD_euclides(q,w), number=itera)
print("Tiempo promedio ecuclides:", tiempo_promedio, "segundos")
tiempo_promedio = timeit.timeit(lambda: MCD_V2([q,w]), number=itera)
print("Tiempo promedio de mi algoritmo:", tiempo_promedio, "segundos")
tiempo_promedio = timeit.timeit(lambda: MCD_Stein(q,w), number=itera)
print("Tiempo promedio de algoritmo Stein:", tiempo_promedio, "segundos")

