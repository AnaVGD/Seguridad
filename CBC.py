############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 19/04/2022
# Práctica: CBC
############################################################

import string
import sys
from numpy import block
import aes_cbc
from aes_cbc import *

def CBC():
  # clave ='00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F'.replace(' ', '')
  # iv = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'.replace(' ', '')
  # b1 = '00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF'
  # b2 = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'

  vecText = []
  # Se introduce la clave y el vector de inicializacion
  clave = input('Introduce la clave: ').replace(' ', '')
  iv = input('Introduce el IV: ').replace(' ', '')
  # Pido el numero de bloques de texto original
  count = int(input('Introduce el número de bloques de texto original: '))
  print()
  for i in range(count):
    block = input('Introduce el texto original ' + str(i + 1) + ': ').replace(' ', '')
    vecText.append(block)

  # vecText = [b1, b2]
  vecResult = []
  # Realizo el cifrado
  for i in range(len(vecText)):
    vecText[i] = vecText[i].replace(' ', '')
    # XOR entre el bloque de texto original y el vector de inicializacion
    vecResult.append(hex(int(vecText[i], 16) ^ int(iv, 16))[2:].zfill(32))
    # Aplico el cifrado AES y lo guardo en el vector de resultado
    vecResult[i] =  rijndael(clave, str(vecResult[i]))
    # El resultado se guarda en el vector de inicializacion
    iv = vecResult[i]

  print()
  print('Salida:')
  # Recorrondo el vector de resultados
  for i in range(len(vecResult)):
    result = ''
    for j in range(len(vecResult[i])):
      # Agrego espacio entre cada numero hexadecimal
      if (j % 2 == 0 and j != 0):
        result +=  ' ' + vecResult[i][j]
      else:
        result += vecResult[i][j]
    vecResult[i] = result
    # Imprimo el resultado por pantalla
    print('Bloque', i+1, 'de Texto Cifrado:', vecResult[i].upper())

# llamo a la funcion CBC
CBC()