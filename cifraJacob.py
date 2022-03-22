from operator import xor

def home():
  print ("Bienvenido al programa")
  semilla = input ("Escriba la semilla de clave: ") # Pido la semilla por pantalla
  texto = input ("Introduzca el texto original: ") # Pido el texto por pantalla
  vectorMensaje = texto.split(",") # Paso el mensaje introducido a un vector
  vectorSemilla = semilla.split(",") # Paso la clave a un vecotr
  PRGA(KSA(vectorSemilla),vectorSemilla, vectorMensaje) # Invoco a PRGA y llamo s KSA que devuelve la S y le paso el vector con la semilla y el vector con el texto

# Creo el KSA  
def KSA (vectorSemilla): # Le paso el vector de la semilla
  s = [] # Creo vector S
  k = [] #Creo vector k
  for i in range(256): # Bucle for que recorre las 256 posiciones
    s.append(i) # Rellenos el vector del 0 hasta el 255 
    k.append(vectorSemilla[i % len(vectorSemilla)]) # Relleno la k con la semilla y la voy repitiendo hasta llegar a 255
  print ("\nS =", s) # Muestro la S
  print ("\nK =", k, end="\n") # Muestro la k
  j = 0
  for i in range(256):
    print ("S[" + str(i) + "]=" + str(s[i]) + ", K[" + str(i) + "]=" + str(k[i]) + " produce ", end="")
    j = (j + int(s[i]) + int(k[i])) % 256
    s[i], s[j] = s[j], s[i] #Intercambio valores
    print ("f=" + str(j) + ", S[" + str(i) + "]=" + str(s[i]) + ", S[" + str(j) + "]=" + str(s[j])) 
  print ("\nS =", s)
  return s

def PRGA (s, vectorSemilla, vectorMensaje): # le paso la S (resultado de KSA), el vector de la semilla y el vector del mensaje
  i = 0 # inicalizo la i
  j = 0 # inicializo la j
  l = 0 # Creo el iterador
  vectorSecuencia = [] # Creo el vector de la secuencia iniciada
  vectorOperator = [] # Creo el vector que va a operar
  for l in range(len(vectorSemilla)): # bucle for que recorre el tamaño del vector semilla
    i = (i + 1) % 256 
    j = (j + s[i]) % 256 
    s[i], s[j] = s[j], s[i] #intercmabio los valores
    t = (s[i] + s[j]) % 256
    vectorSecuencia.append(s[t]) # Agrego el cifrado al vector secuencia 
    vectorOperator.append(xor(int(vectorMensaje[l]), int(s[t]))) # Hago el xor entre el mensaje original y el resultado
    print("Byte " + str(l+1) + " de secuencia cifrante: Salida: S[" + str(t) + "] = " + str(s[t]) + ":\t" + bin(s[t])[2:].zfill(8))
    print("Byte " + str(l+1) + " de texto original: Entrada: M[" + str(l+1) + "] = " + str(vectorMensaje[l]) + ":\t\t" + bin(int(vectorMensaje[l]))[2:].zfill(8)) # bin lo convierto a binario, sin el 8b gracias al 2: y de 8 bites por el zfill
    print("Byte " + str(l+1) + " de texto cifrado: Salida: C[" + str(l+1) + "] = " + str(vectorOperator[l]) + ":\t\t" + bin(int(vectorOperator[l]))[2:].zfill(8)) 

home()