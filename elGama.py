#########################################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 26/04/2022
# Práctica: INTERCAMBIO DE CLAVES DE DIFFIE-HELLMAN Y CIFRADO DE ELGAMAL
#########################################################################

from numpy import append
import sys

# Paso los valores de (p, a, k, x, m) por lineas de comando
try:
    p = int(sys.argv[1])
    a = int(sys.argv[2])
    k = int(sys.argv[3])
    x = int(sys.argv[4])
    mArgv = int(sys.argv[5])

# Informa de un error en caso de que no se inserten todos los valores
except IndexError:
    print('Tiene que introducir los 5 datos correspondientes (p, a, k, x, m)')
    sys.exit(1)

# Función elGamal() encargado de realizar el cifrado elGamal
def elGamal():
  m = mArgv
  # Imprimo los valores introducidos 
  print(f'p = {p}, a = {a}, k = {k}, x = {x}, m = {m}')
  
  # Calculo valor publico de A Ya = a^k (mod p)
  Ya = (a**k)%p
  # Calculo el valor publico de B Yb = a^x (mod p)
  Yb = (a**x)%p
  # Calculo K, la clave compartida
  K = (Ya**x)%p
  # Obtengo el mensaje cifrado
  c = K * m % p
  # Calculo el inverso de la clave compartida llamando a la función inverso 
  Kinverso = inverso(p, K)
  # Descifro el mensaje cifrado.
  m = (Kinverso * c) % p
  # Imprimo los resultados de los calculos
  print(f'ya = {Ya}, yb = {Yb}, K = {K}, C = {c}, K-1 = {Kinverso}, M = {m}')
  
# Funcion encargada de aplicar el algoritmo de Euclides Extendido
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
  return z[len(z)-1]

elGamal()
