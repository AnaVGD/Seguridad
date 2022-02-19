############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 22/02/2022
# Práctica: Cifrado de Vernam
############################################################

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
      print("La seleccion no es correcta")


# Funcion encargada de cifrar o descifrar
def vernam(action):
  message = input("Introduce el mensaje a " + action + ": ")
  print(" ")
  # Convierte el mensaje introducido a binario y se guarda en binary
  binary = ''.join(format(ord(i), '08b') for i in message)
  # Contiene el numero de caracteres del string
  sizeBinary = len(binary)
  print("Mensaje original en binario: " , binary)
  print("Longitud del mensaje binario: ", sizeBinary)
  print(" ")
  
  sameSize = False
  isBinary = False
  
  # Comprueba que la clave se del mismo tamaño que el mesaje introducido en binario y sea una cadena binaria
  # El proceso no termina hasta que se introduzca una clave correcta
  while sameSize == False and isBinary == False:
    clave = input("Introduce la clave aleatoria de tamaño " + str(sizeBinary) + ": ")
    for i in binary:
      # Comprueba que la cadena sea binaria
      if i == "0" or i == "1": 
        isBinary = True
    # Comprueba que la cadena sea del mismo tamaño a la introducida en binario
    if len(clave) == sizeBinary:
      sameSize = True
    else:
      print("El tamaño de la clave no es " + sizeBinary)
    
    # En el caso de que no sea del mismo tamaño se indica
    if isBinary == False:
      print("La clave introducida no es binaria")
    print(" ")
    
  if (action == "descifrar"):
    act = "original"
  elif (action == "cifrar"):
    act = "cifrado"
  
  # Convierta las cadenas binarias a una base entera 2, luego XOR, luego bin()y luego omita los dos primeros caracteres, 0bde ahí el bin(y0)[2:].
  # Después de eso, solo zfill hasta la longitud tam, para este caso.
  c = int(binary,2) ^ int(clave,2)
  print("Mensaje " + act + " en binario: ", bin(c)[2:].zfill(sizeBinary))
  
  s = bin(c)[2:].zfill(sizeBinary)
  
  # Convierto el mensaje cifrado en original o el mensaje original en cifrado
  # se encarga de convertir el string binario en un cadena de carcateres ASCII
  print("Mensaje " + act + ": ", ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8)))
  
    
# Llamo al menu
menu()