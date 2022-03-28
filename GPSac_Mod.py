from ast import Str
from re import L

# Lista de los satélites
# def satelite(n):
#   sats = [(2, 6), (3, 7), (4, 8), (5, 9), (1, 9), (2, 10), (1, 8), (2, 9), 
#           (3, 10), (2, 3), (3, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), 
#           (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (1, 3), (4, 6),
#           (5, 7), (6, 8), (7, 9), (8, 10), (1, 6), (2, 7), (3, 8), (4, 9)]
#   return sats[n-1]


def inicio():
  # id = int(input('Introduce la ID del satélite: '))
  longitud = int(input('Introduce la longitud de la secuencia de salida: '))
  print()
  # sat = satelite(id)
  # print(sat[0])
  vecLDSR1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  resulLDSR1 = 0
  vecLDSR2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  resulLDSR2 = 0
  print('--------------------------------------------------------------------------------------------------------------------------')
  print("{:<30} | {:<15} | {:<30} | {:<15} | {:<10}".format('LDSR1','Realimentacion','LDSR2','Realimentacion', 'Secuencia C/A PRN1'))
  print('--------------------------------------------------------------------------------------------------------------------------')
  
  for i in range(longitud):
    aux1 = [str(i) for i in vecLDSR1]
    rest1 = ('  '.join(aux1))
    aux2 = [str(i) for i in vecLDSR2]
    rest2 = ('  '.join(aux2))
    
    print("{:<30} | {:<15} | {:<30} | {:<15} | {:<10}".format(rest1, resulLDSR1, rest2, resulLDSR2, sec(vecLDSR1, vecLDSR2)))
    x = LDSR1(vecLDSR1, resulLDSR1)
    vecLDSR1 = x[0]
    resulLDSR1 = x[1]
    # print(x, end='')
    x = LDSR2(vecLDSR2, resulLDSR2)
    vecLDSR2 = x[0]
    resulLDSR2 = x[1]


def LDSR1(vec, result):
  resul = vec[2] ^ vec[7]
  vec = [resul] + vec
  vec.pop()
  return vec, resul

def LDSR2(vec, result):
  resul = vec[1] ^ vec[2] ^ vec[5] ^ vec[7] ^ vec[8] ^ vec[9]
  vec = [resul] + vec
  vec.pop()
  return vec, resul



def sec(vec1, vec2):
  return(vec2[9] ^ vec1[9])

inicio()