import sys
import math
from random import shuffle


def inicio():
  # p = int(input('número primo p: '))
  # a = int(input('a: '))
  # b = int(input('b: '))
  # G = int(input('punto base G: '))
  # db = int(input('Db: '))
  # da = int(input('Da: '))
  # mensaje = input('Mensaje original: ')
  # p = 11
  # a = 1
  # b = 1
  # G = [3, 8]
  # db = 2
  # da = 3
  # mensaje = 3
  p = 13
  a = 5
  b = 3
  G = [9, 6]
  db = 2
  da = 4
  mensaje = 2
  
  if (testLP(p) and p > 3):
    if (comprobacion(a, b, p)):
      puntos = cacularPunto(p, a, b)
      print(str(puntos))
      # print('print', db, G)
      dbG = multPunto(db, G, p, a)
      print('Clave pública de B: punto dBG= ' + str(db) + '*' + str(G) + '=' + str(dbG))
      
      # print('print', da, G)
      daG = multPunto(da, G, p, a)
      print('Clave pública de A: punto dAG= ' + str(da) + '*' + str(G) + '=' + str(daG))
      
      # print('print', da, dbG)
      claveA = multPunto(da, dbG, p, a)
      print('Clave secreta compartida calculada por A: dA*(dBG)= ' + str(da) + '*' + str(dbG) + '=' + str(claveA))
      
      # print('print', db, daG)
      claveB = multPunto(db, daG, p, a)
      print('Clave secreta compartida calculada por B: dB*(dAG)= ' + str(db) + '*' + str(daG) + '=' + str(claveB))
      
      M = calcularM(mensaje)
      print('M =', M)
      
      h = p // M
      print('h =', h, '<', p, '/', M)
      
      mensajeOriginal = codificar(M, p, mensaje, puntos)
      print('Mensaje original codificado como punto Qm = ' + str(mensajeOriginal))
      
      cifrado = sumaPunto(mensajeOriginal, claveA, p, a)
      print('Mensaje cifrado y clave pública enviados de A a B: {' + str(cifrado) + ', ' + str(daG) + '}')
    else:
      print('ERROR: No es una curva elíptica')
  else:
    print('ERROR: P no es un número primo')
  
  
  
  
def expRapida(base, exponente, modulo):
  x = 1
  y = base % modulo
  b = exponente
  while (b > 0):
    # Si b par
    if ((b % 2) == 0):
      y = (y * y) % modulo
      b = b / 2
    # Si b es impar
    else:
      x = (x * y) % modulo
      b = b - 1
  return x


def testLP(p):
  if (p == 2 or p == 3 or p == 5 or p == 7 or p == 11):
    return True
  else:
    if (p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0):
      return False
    else:
      a = list(range(2, p))  # Lista de enteros de 1 a 'p-1'
      shuffle(a)  # desordena la lista
      resultA = []

      for i in range(len(a)):
        resultA.append(expRapida(a[i], ((p - 1) // 2 ), p))
        
      primo = True
      todo1 = True
      i = 0;
      while(primo and i < len(resultA)):
        if (resultA[i] != 1):
          todo1 = False
          if (resultA[i] != (p-1)):
            primo = False
        i += 1

      if (primo == True and todo1 == False):
        return True
      else: 
        False

def inverso(dividendo, divisor):
  # Declaro dos vectores uno para los valores de x y otro para los de z
  x = [dividendo, divisor]
  z = [0,1]
  
  # Aplico el algoritmo, empiezo a recorre el array desde el final
  i = (len(x) - 1)
  while(x[i] > 1):
    if (x[i] > 0):
      x.append(x[i-1] % x[i])
      z.append((-(x[i-1] // x[i]) * z[i]+z[i-1]) % dividendo)
    i += 1
  return  z[len(z)-1]


def cacularPunto(p, a, b):
  x = []
  y = []
  for i in range(p):
    x.append(((i**3 )+ (a * i) + b) % p)
    y.append((i**2 ) % p)
  aux = []
  iter = 0
  for i in range(len(x)):
    for j in range(len(y)):
      if (x[i] == y[j]):
        aux.append([i, j])
        iter += 1
  return aux

def sumaPunto(punto1, punto2, p, a):
  lan = 0
  if ((punto1[0] == punto2[0]) and (punto2[1] == -punto1[1])):
    return [0, 0]
  else:
    if (punto1 != punto2):
      lanUp = punto2[1] - punto1[1]
      lanDown = punto2[0] - punto1[0]
      # print(lanUp, lanDown, 'lanUp, lanDown')
      while (lanUp < 0):
        lanUp += p
        
      while (lanDown < 0):
        lanDown += p
      
      if (lanUp % lanDown == 0):
        lan = lanUp // lanDown
      else:
        # print(inverso(p, lanDown), 'inverso')
        lan = lanUp * inverso(p, lanDown)
    else:
      lanUp = 3*punto1[0]**2 + a
      lanDown = 2*punto1[1]
      if (lanUp % lanDown == 0):
        lan = lanUp // lanDown
      else:
        # print(inverso(p, lanDown), 'inverso')
        lan = lanUp * inverso(p, lanDown)

  x3 = (lan**2 - punto1[0] - punto2[0]) % p
  y3 = (lan * (punto1[0] - x3) - punto1[1]) % p
  return [x3, y3]

def comprobacion(a, b ,p):
  if ((4*a**3 + 27*b**2) % p == 0):
    return False
  else :
    return True
  
def multPuntoOther(mul, punto1, p, a):
  punto2 = punto1
  # result = [0, 0]
  for i in range(mul - 1):
    # print(i)
    # print('result', punto1, punto2)
    punto2 = sumaPunto(punto1, punto2, p, a)
  return punto2

def multPunto(mul, punto1, p, a):
  vec = [punto1] * mul
  div = mul // 2
  auxVec = [[0, 0]] * div
  # print(vec)
  # print(auxVec)
  
  if (div % 2 == 0):
    while (div > 0):
      for i in range(len(auxVec)):
        auxVec[i] = sumaPunto(vec[i], vec[i+div], p, a)
      # print(auxVec)
      vec = auxVec
      div = div // 2
      auxVec = [[0, 0]] * div
    return vec[0]
  else:
      return multPuntoOther(mul, punto1, p, a)

def calcularM(m):
  M = 0
  if (m >= 0):
    while(m >= M):
      # print(M)
      M += 2
    return M
  else:
    print('El mensaje debe ser mayor que 0')
    return None
  
def codificar(M, p, m, listaP):
  h = p // M
  
  for j in range(h):
    x = m * h + j
    for punto in listaP:
      if (x == punto[0]):
        return punto
  return None
  
inicio()
# print(multPunto(3, [6, 6], 11, 1))
# print(cacularPunto(11, 1, 6))
# list = cacularPunto(11, 1, 6)
# print(len(list))
# print(inverso(11, 8))
# print(sumaPunto([2, 4], [2, 4], 11, 1))
# print(calcularM(2))
# for i in range(len(list)):
#   print(list[i])
# print(codificar(4, 13, 2, cacularPunto(13, 5, 3)))
# result = codificar(2, 11, 0, cacularPunto(11, 1, 6))
# print('result', result)
# DbG = multPunto(2, [9, 6], 13, 5)
# print(sumaPunto([10, 2], [5, 2], 11, 1))
# print('DbG', DbG)
# Da = multPunto(3, DbG, 11, 1)
# print('Da', Da)
# cifrad = sumaPunto(result, Da, 11, 1)
# print('cifrado', cifrad)
# daG = multPunto(4, [5, 2], 11, 1)
# print('daG', daG)
# result = codificar(4, 13, 2, cacularPunto(13, 5, 3))
# print('result', result)
# DbG = multPunto(2, [9, 6], 13, 5)
# print('DbG', DbG)
# Da = multPunto(4, DbG, 13, 5)
# print('Da', Da)
# cifrad = sumaPunto(result, Da, 13, 5)
# print('cifrado', cifrad)