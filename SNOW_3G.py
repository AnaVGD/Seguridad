############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 29/03/2022
# Práctica: Multiplicacion Snow 3G y AES
############################################################


from numpy import byte
import sys

def inicio():
  byte1 = input('Primer byte: ')
  byte2 = input('Segundo  byte: ')
  # byte1 = bin(int('10111101', 2))[2:].zfill(8)
  # byte2 = bin(int('00100101', 2))[2:].zfill(8)
  byte1 = '57'
  byte2 = '83'
  # print(byte1, byte2)
  byte1 = (bin(int(byte1, 16))[2:]).zfill(8)
  byte2 = (bin(int(byte2, 16))[2:]).zfill(8)
  correct = False
  algoritmo = int(input("\nSeleccione el algoritmo a usar Snow3G (0) | AES (1) "))
  while(correct == False):
    if algoritmo == 0:
      print("Se utilizará el byte A9 (10101001)")
      altg = "10101001"
      correct = True
    elif algoritmo == 1:
      print("Se utilizará el byte 1B (00011011)")
      altg = "00011011"
      correct = True
    else:
      print("Elección erronea")

  doit(byte1, byte2, altg)
  
  
def doit(byte1, byte2, algort):
  separbits = []
  resultados = []
  # print(byte2)
  for i in reversed(range(len(byte2))):
    if(byte2[i] == '1'): 
      # print('hi')
      # print(separar(i))
      separbits.append(separar(i))
  # print(separbits)
  # print(byte1, byte2)
  for i in range(len(separbits)):
    if separbits[i][7] == "1": # 00000001
      resultados.append(byte1)
    else:
      print('\nPasos de la operacion', byte1, 'x', separbits[i])
      resultados.append(desplazamiento(byte1, separbits[i], algort))

  print("\nOperacion", resultados)
    
  result = 0
  for i in range(len(resultados)):
    result ^= int(resultados[i], 2)
  
  print('\nPrimer byte: ' + byte1)
  print('Segundo byte: ' + byte2)
  print('Byte Algoritmo: ' + algort)
  print("Multiplicación = " + bin(result)[2:].zfill(8))
      
def separar(one):
  # print('hi')
  stringByte = ''
  for i in range(8):
    if (i != one):
      stringByte += '0'
    else:
      stringByte += '1'
  return stringByte

def desplazamiento(byte1, byte2, algort):
  # print(byte2)
  desplazamiento = 0
  for i in range(len(byte2)):
    if (byte2[i] == "1"):
      desplazamiento = i
      break

  # print(desplazamiento)
  desplazamiento = 7 - desplazamiento
  # print(desplazamiento)
  valor = byte1
  iteracion = 0
  
  print("%d --> " % iteracion, valor)
  for i in range(desplazamiento):
      if valor[0] == "1": # Desplazamos y sumamos byte Snow3G | AES
          valor = valor[1:]
          valor = valor + "0"
          valor = int(valor, 2) ^ int(algort, 2)
          valor = (str(bin(valor)[2:])).zfill(8)
      else: # Desplazamos
          valor = valor[1:]
          valor = valor + "0"
      iteracion = iteracion + 1
      print("%d --> " % iteracion, valor)

  return valor
  
inicio()
# doit()