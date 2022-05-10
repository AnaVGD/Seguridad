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
  

# Paso el primer byte, el segundo byte y el bit A9 o 1B
# primero recorro el byte 2 y cuando sea igual a uno llamo a la función separar que me devolver un
# string con los bits separados y esto lo guardo en el vector separbits, luego recorro este vector pero 
# compruebo que las ultimas posiciones de los bits que están en el vector sea uno, si lo es en el vector resultado 
# guardo el bit tal cual, en caso contrario llamo a la función desplazamiento que calculara el desplazamiento del bit dependiendo
# del bit del algoritmo.
def doit(byte1, byte2, algort):
  separbits = []
  resultados = []
  for i in reversed(range(len(byte2))):
    if(byte2[i] == '1'): 
      separbits.append(separar(i))
  for i in range(len(separbits)):
    if separbits[i][7] == "1": # 00000001
      resultados.append(byte1)
    else:
      print('\nPasos de la operacion', byte1, 'x', separbits[i])
      resultados.append(desplazamiento(byte1, separbits[i], algort))
      
      
  print("\nOperacion")
  for i in range(len(resultados) -1):
    print(resultados[i] + ' + ', end='')
  print(resultados[len(resultados) - 1])
  result = 0
  for i in range(len(resultados)):
    result ^= int(resultados[i], 2)
  
  print('\nPrimer byte: ' + byte1)
  print('Segundo byte: ' + byte2)
  print('Byte Algoritmo: ' + algort)
  print("Multiplicación = " + bin(result)[2:].zfill(8))

# Separa los bits si es 100010 devuelve 000010
# se le pasa la posición donde se encuentra el uno
def separar(one):
  stringByte = ''
  for i in range(8):
    if (i != one):
      stringByte += '0'
    else:
      stringByte += '1'
  return stringByte

# Calcula el desplazamiento, comprueba la posición del 1, luego calcula el desplazamiento
# comprueba si la primera posición es 1 en ese caso se le suma el bit del algorito en caso contrario se desplaza
# lo que le corresponde.
def desplazamiento(byte1, byte2, algort):
  # print(byte2)
  desplazamiento = 0
  for i in range(len(byte2)):
    if (byte2[i] == "1"):
      desplazamiento = i
      break

  desplazamiento = 7 - desplazamiento
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
