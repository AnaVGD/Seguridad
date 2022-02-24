############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 22/02/2022
# Práctica: Cifrado de Vernam
############################################################

# Pruebas
# M.O = ana
# C = 001111110010011000100101

# M.C = CAI?
# C = 00101011001011100010010101011110

from pickle import FALSE
import sys

# Imprimo el menu para que se seleccione si se quiere cifrar o descifra 
def menu():
  sel = False
  while sel == False:
    selec = input("Selecciona [d]escifrar o [c]ifrar un mensaje: ")
    if selec == 'd':
      vernam("descifrar")
      sel = True
    elif selec == 'c':
      vernam("cifrar")
      sel = True
    else:
      sel = False
      print("La selección no es correcta")

# Función encargada de cifrar o descifrar
def vernam(action):
  message = input("Introduce el mensaje a " + action + ": ")
  print(" ")
  
  # Convierte el mensaje introducido a binario y se guarda en binary
  # La format()función simplemente formatea la entrada. 
  # formatea la salida para que quepa en un ancho de 8 caracteres, con 0 relleno; 
  # Con el join uno todos los bits en una única cadena
  # con ord() te indica el código ascii
  binary = ''.join(format(ord(i), '08b') for i in message)
  
  # Contiene el numero de caracteres del string
  sizeBinary = len(binary)
  
  print("Mensaje original en binario: " , binary)
  print("Longitud del mensaje binario: ", sizeBinary)
  print(" ")
  
  # Compruebo que la clave se del mismo tamaño que el mesaje introducido en binario y sea una cadena binaria
  # El proceso no termina hasta que se introduzca una clave correcta
  sameSize = False
  isBinary = False
  
  while sameSize == False and isBinary == False:
    clave = input("Introduce la clave aleatoria de tamaño " + str(sizeBinary) + ": ")
    for i in clave:
      # Comprueba que la cadena sea binaria
      if i == "0" or i == "1": 
        isBinary = True
    
    # En el caso de que no sea del mismo tamaño se indica
    if isBinary == False:
      print("La clave introducida no es binaria")
    
    # Comprueba que la cadena sea del mismo tamaño a la introducida en binario
    if len(clave) == sizeBinary:
      sameSize = True
    else:
      sameSize = False
      print("El tamaño de la clave no es " + str(sizeBinary))
      print(" ")
    
  if (sameSize == True and isBinary == True):
    if (action == "descifrar"):
      act = "original"
    elif (action == "cifrar"):
      act = "cifrado"
    
    # Convierte las cadenas binarias a una base entera 2, luego XOR, luego bin()y luego omita los dos primeros caracteres, 0b de ahí el bin(y0)[2:].
    # Después de eso, solo zfill hasta la longitud tam, para este caso.
    # omite los dos primeros caracteres 0b de ahí el bin(c)[2:].
    c = int(binary,2) ^ int(clave,2)
    resultXor = bin(c)[2:].zfill(sizeBinary)
    
    print(' ')
    print("Mensaje " + act + " en binario: ", resultXor)
    
    resultXorInt = int(resultXor, 2)

    # Convierto el mensaje cifrado en original o el mensaje original en cifrado
    # Toma cada bloque de ocho caracteres (un byte), convertirlo en un número entero y luego convertirlo en un carácter con chr()
    print("Mensaje " + act + ": ", ''.join(chr(int(resultXor[i*8:i*8+8],2)) for i in range(len(resultXor)//8)))
    
# Llamo al menu
menu()
