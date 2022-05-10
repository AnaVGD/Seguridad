#########################################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 02/05/2022
# Práctica: PRÁCTICA: CIFRADO RSA
#########################################################################

  # p = 2347
  # q = 347
  # d = 5
  # mensaje = 'MANDA DINEROS'
  # mensaje = mensaje.replace(' ', '').upper()
  # abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # p = 421
  # q = 7
  # d = 1619
    # q = int(input('Introduce q'))
  # d = int(input('Introduce d'))
  # mensaje = 'AMIGO MIO'

from email import message
import math
import sys
from random import shuffle

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

      if (primo and todo1 == False):
        return True
      else: 
        False
  
def euclides(dividendo, divisor):
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
  return x[len(z)-1], z[len(z)-1]


def init():
  mensaje = input('Introduce el mensaje: ')
  mensaje = mensaje.replace(' ', '').upper()

  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  # Compruebo que p y q sean primos
  primos = False
  while(primos == False):
    p = int(input('Introduce p: '))
    if (testLP(p)):
      print('p es primo\n')
      primos = True
    else:
      print('p no es primo\n')
      primos = False

  primos = False
  while(primos == False):
    q = int(input('Introduce q: '))
    if (testLP(q)):
      print('q es primo\n')
      primos = True
    else:
      print('q no es primo\n')
      primos = False

  # Calculo o(n)
  # print(p, q)
  primos = False
  while(primos == False):
    d = int(input('Introduce d: '))
    o = (p - 1) * (q - 1)
    aux, e = euclides(o, d)
    if (aux == 1):
      print('d es primo\n')
      primos = True
    else:
      print('d no es primo\n')
      primos = False
  
  print('Se calcula phi =', o, '\n')
  print('Se calcula e =', e, '\n')
  
  # Calculo n
  n = p * q
  
  # Se calcula el tamaño de bloque en el que se dividirá el mensaje original
  j = math.trunc(math.log(n, 26)) + 1
  print('Se calcula n =', n, 'se divide el texto en bloques de', j - 1, 'caracteres\n')

  if ((j - 1) % 2 == 0):
    if (len(mensaje) % 2 != 0):
      mensaje += 'X'
  else:
    if (len(mensaje) % 2 == 0):
      mensaje += 'X'
  #Division del mensaje en bloques de j-1 de tamaño
  mensajeVec = []
  i = 0
  while(i < len(mensaje)):
    mensajeVec.append(mensaje[i:i + j - 1])
    i = i + j - 1
  print(mensajeVec)
  
  # Paso a decimal el mensaje
  mnsjDecimal = [] 
  for i in mensajeVec:
    aux = 0  # Suma de los caracteres en decimal
    pos = j - 2  # Posición del caracter en el bloque para la ponderación
    k = 0
    while (k < len(i)):
      aux = aux + abc.find(i[k]) * (26 ** pos)  # Se suma la ponderación del caracter correspondiente
      # print(abc.find(i[k]), 'abc')
      k = k + 1
      pos = pos - 1
    mnsjDecimal.append(aux)  # Se añade a la lista el bloque en decimal generado
    
  print('Se pasa cada bloque a decimal para poder cifrar, obteniendo', ", ".join([str(_) for _ in mnsjDecimal]), '\n')
  
  # cifrado
  # m' := me (mod n)
  mnsjCifrado = []
  for item in mnsjDecimal:
    mnsjCifrado.append(expRapida(item, e, n))
  print('Se calcula en decimal el texto cifrado:', ", ".join([str(_) for _ in mnsjCifrado]))
  

init()