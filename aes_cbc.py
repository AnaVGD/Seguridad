
# Inicialización de la Caja S
caja_s = []
caja_s.append([0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76])
caja_s.append([0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0])
caja_s.append([0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15])
caja_s.append([0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75])
caja_s.append([0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84])
caja_s.append([0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf])
caja_s.append([0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8])
caja_s.append([0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2])
caja_s.append([0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73])
caja_s.append([0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb])
caja_s.append([0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79])
caja_s.append([0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08])
caja_s.append([0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a])
caja_s.append([0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e])
caja_s.append([0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf])
caja_s.append([0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16])

# Rcon
rc = []
rc.append([0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36])
rc.append([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
rc.append([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
rc.append([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Convierto un string en una matriz 4x4
def toMatrix(strin):
  strinVec = []
  for i in range(4):
    strinVec.append([])
    for j in range(4):
      pos = (i * 8) + (2 * j)
      strinVec[i].append(strin[pos:pos+2])
  
  # print(strinVec)
  finalVec = []
  for k in range(len(strinVec)):
    aux = []
    for l in range(len(strinVec)):
      # Los valores los pongo en hexadecimal
      aux.append('0x' + (hex(int(strinVec[l][k], 16)))[2:].zfill(2))
    finalVec.append(aux)
  # print(finalVec)
  return finalVec

# Iteración 0
# OR-EXCLUSIVA entre el bloque de entrada y la clave original de cifrado.
def addRoundKey(entradaMatrix, claveMatrix):
  for i in range(4):
    result =[]
    for j in range(4):
      result.append('0x' + (hex(int(entradaMatrix[i][j], 16) ^ int(claveMatrix[i][j], 16)))[2:].zfill(2))
    entradaMatrix[i] = result
  return entradaMatrix

# Transformación 1
# Usando la caja s, sustituyo los bytes por unos nuevos teniendo en cuenta la caja
def subBytes(estado1):
  for i in range(4):
    auxVec = []
    for j in range(4):
      # obtengo la posiciones para buscar en la caja a partir de los bytes del
      # estado intermedio 1, y los convierto en enteros para poder buscar en la caja-s
      pos = estado1[i][j][2:].zfill(2)
      auxVec.append(hex(caja_s[int(pos[0], 16)][int(pos[1], 16)]))
    estado1[i] = (auxVec)
  return estado1

# Realizo el algoritmo de subBytes pero solo para una columna
def subBytesColum(col):
  for i in range(4):
    pos = col[i][2:].zfill(2)
    col[i] = ('0x' + hex(caja_s[int(pos[0], 16)][int(pos[1], 16)])[2:].zfill(2))  
  return col

# Transformación 2.
# desplazo a la izquierda los bytes de las filas que conforman la matriz del 
# estado actual.
# Cada fila i=0,1,2,3 se desplaza un nº i de posiciones diferentes
def shiftRow(estado2):
  for i in range(4):
    auxVec = []
    k = i
    for j in range(4):
      auxVec.append(estado2[i][k % 4])
      k += 1
    estado2[i] = auxVec
  return(estado2)

# Transformación 3.
# Aplico el algoritmo dado:
# void gmix_column(unsigned char *r) {
#  unsigned char a[4];
#  unsigned char b[4];
#  unsigned char c;
#  unsigned char h;
#  /* The array 'a' is simply a copy of the input array 'r'
#  * The array 'b' is each element of the array 'a' multiplied by 2
#  * in Rijndael's Galois field
#  * a[n] ^ b[n] is element n multiplied by 3 in Rijndael's Galois field */
#  for(c=0;c<4;c++) {
#  a[c] = r[c];
#  h = r[c] & 0x80; /* hi bit */
#  b[c] = r[c] << 1;
#  if(h == 0x80)
#  b[c] ^= 0x1b; /* Rijndael's Galois field */
#  }
#  r[0] = b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]; /* 2 * a0 + a3 + a2 + 3 * a1 */
#  r[1] = b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]; /* 2 * a1 + a0 + a3 + 3 * a2 */
#  r[2] = b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]; /* 2 * a2 + a1 + a0 + 3 * a3 */
#  r[3] = b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]; /* 2 * a3 + a2 + a1 + 3 * a0 */
# } 
def mixColumn(r):
  # print(r)
  for i in range(4):
    a = []
    b = []
    for c in range(4):
      a.append(int(r[c][i], 16))
      h = int(r[c][i], 16) & 0x80
      b.append((int(r[c][i], 16) << 1) % 256)
      if (h == 0x80):
        b[c] = b[c] ^ 0x1b 
    r[0][i] = hex(b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]) 
    r[1][i] = hex(b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]) 
    r[2][i] = hex(b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]) 
    r[3][i] = hex(b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]) 
  return r

# EXPANSIÓN DE CLAVE
def expandirClave(clave):
  subclave = []  # Lista en la que se irán guardando las subclaves
  subclave.append(clave)  # Se añade la clave original como primera subclave
  # print(clave)
  # 10 subclaves
  for n in range(10):
    clave_aux = []
    columna_aux = []
    columna1 = []
    columna2 = []
    columna3 = []
    columna4 = []
    
    for i in range(4):
      columna_aux.append(subclave[n][i][3])
      
    #RotWord
    aux = columna_aux.pop(0)
    columna_aux.append(aux)
    
    #SubBytes
    subBytesColum(columna_aux)
    
    #XOR
    for i in range(4):
      columna1.append('0x' + hex(int(subclave[n][i][0], 16) ^ int(columna_aux[i], 16) ^ rc[i][n])[2:].zfill(2))
      columna2.append('0x' + hex(int(subclave[n][i][1], 16) ^ int(columna1[i], 16))[2:].zfill(2))
      columna3.append('0x' + hex(int(subclave[n][i][2], 16) ^ int(columna2[i], 16))[2:].zfill(2))
      columna4.append('0x' + hex(int(subclave[n][i][3], 16) ^ int(columna3[i], 16))[2:].zfill(2))
      
    # Añado las columnas a las filas
    for j in range(4):
      filas = []
      filas.append(columna1[j])
      filas.append(columna2[j])
      filas.append(columna3[j])
      filas.append(columna4[j])
      clave_aux.append(filas)
    # Se añade la subclave generada a la lista de claves
    subclave.append(clave_aux)  
  return subclave

# Se encarga de llamar a las funciones comentadas anteriormente teniendo en
# cuenta el orden correspondiente 
def rijndael(clave, entrada):
  # clave = input('Introduce la clave (16 bytes en hexadecimal): ')
  # while len(clave) != 32:
  #   clave = input("Introduzca la clave (16 bytes en hexadecimal): ")
    
  # entrada = input('Introduce el texto original (16 bytes en hexadecimal) : ')
  # while len(entrada) != 32:
  #   entrada = input("Introduzca el texto original (16 bytes en hexadecimal): ")
  # entrada ='3243f6a8885a308d313198a2e0370734'
  # clave = '2b7e151628aed2a6abf7158809cf4f3c'
  # entrada ='00112233445566778899aabbccddeeff'
  # clave = '000102030405060708090a0b0c0d0e0f'
  # print(type(entrada))
  entradaMatrix = toMatrix(str(entrada))
  subClave = []
  subClave = expandirClave(toMatrix(clave))
  addRoundKey(entradaMatrix, toMatrix(clave))

  # Inicia el bucle de 9 iteraciones (SubBytes, ShiftRow, MixColumn y AddRoundKey)
  for item in range(1, 10):
    subBytes(entradaMatrix)
    shiftRow(entradaMatrix)
    mixColumn(entradaMatrix)
    addRoundKey(entradaMatrix, subClave[item])

  # Etapa final
  subBytes(entradaMatrix)
  shiftRow(entradaMatrix)
  addRoundKey(entradaMatrix, subClave[10])
  var = ''
  for i in range(4):
    for j in range(4):
      var += entradaMatrix[j][i][2:].zfill(2)
  return var

