############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 08/03/2022
# Práctica: Cifrado de RC4
############################################################

def menu():
  seed = input("Introduce la semilla de la clave: ")
  word = str(input("Introduce la palabra: "))
  # Quito los espacios en blanco 
  seed = seed.replace(" ", "")
  word = word.replace(" ", "")
  seedVec = []
  vec = []
  # Separo los números de la semilla en un vector
  seedVec = seed.split(',')
  vec = word.split(',')
  
  # Llamo a la función PRGA pasándole la función KSA y la semilla
  PRGA(KSA(seedVec), seedVec, vec)

# Aplico el algoritmo KSA
def KSA(seed):
  s = [];
  k = [];
  for i in range(256):
    # la asigno al vector S los números de 0 al 255  
    s.append(i) 
    # relleno k con la clave hasta 255
    k.append(seed[i % len(seed)])
  print("S =", s, end="\n\n")
  print("K =", k, end="\n\n")
  j = 0
  for i in range(256):
    j = (j + int(s[i]) + int(k[i])) % 256
    print(f'S[{i}] = {s[i]} K[{i}] = {k[i]} produce f = {j}', end="")
    s[i], s[j] = s[j], s[i]
    print(f' y S[{i}] = {s[i]} S[{j}] = {s[j]}')
  print("\nS =", s)
  return s

# Aplico el algoritmo PRGA
def PRGA(s, seed, vec):
  i = 0
  j = 0
  k = 0
  while(k < len(vec)):
    size  = len(seed)
    for item in range(size):
      i = (i + 1) % 256
      j = (j + s[i]) % 256
      s[i], s[j] = s[j], s[i]
      t = (s[i] + s[j]) % 256
      result = s[t]
      cifrar(item, t, result, vec[k])
      k = k + 1

# Se encarga de cifrar
def cifrar(item, t, result, vec):
  num = vec
  # Paso a binario S[t]
  # if (type(result) == int):
  binary = format(result, "08b")
  print(f"\nByte {item + 1} de secuencia cifrante: s[{t}] = {result}: {binary}")
  print(f"Introduce el byte {item + 1} de texto original: {num}")
  # print(num)
  # Paso a binario el primer bit introducido. 
  binaryInput = format(int(num), "08b")
  print(f"M[{item + 1}] = {num}:", binaryInput)
  # Hago la operación XOR entre el numero introducido y el numero de S[t]
  xor = int(binary, 2) ^ int(binaryInput, 2)
  print(f'Byte {item + 1} de texto cifrante: C[{item + 1}] = {xor}: {format(xor, "08b")}')
  # else:
  #   binary = ''.join(format(ord(i), '08b') for i in result)
  #   print(f"Byte {item + 1} de secuencia cifrante: s[{t}] = {result}: {binary}")
  
  

menu()
