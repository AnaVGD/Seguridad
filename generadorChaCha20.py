############################################################
# Ana Virginia Giambona Díaz
# Alu0101322650@ull.edu.es
# Seguridad en sistemas Informáticos 
# 15/03/2022
# Práctica: ChaCha20
############################################################

from binhex import hexbin
from contextlib import redirect_stdout
from curses import noecho
from ntpath import join
from numpy import vectorize

def menu():
  clave = input('Clave de 256 bits en forma de 8 palabras en hexadecimal = ')
  contador = input('Contador de 32 bits en forma de 1 palabra en hexadecimal = ')
  nonce = input('Nonce aleatorio de 96 bits en forma de 3 palabras en hexadecimal = ')
  # clave = '00:01:02:03: 04:05:06:07: 08:09:0a:0b: 0c:0d:0e:0f: 10:11:12:13: 14:15:16:17: 18:19:1a:1b: 1c:1d:1e:1f'
  # contador = '01:00:00:00'
  # nonce = '00:00:00:09: 00:00:00:4a: 00:00:00:00'
  # clave = '0e:99:a3:97: 3c:53:eb:1b: e2:42:6b:ad: 2f:31:2d:24: d9:c2:76:2b: 53:5e:f4:d7: 8e:17:75:a9: 45:3a:68:a5'
  # contador = '01:00:00:00'
  # nonce = 'b6:9e:de:ac: 73:ee:44:05: d3:fa:9a:8e'
  
  
  # Divido le asigna un apsosicion de un vector a cada numero hexadecimal de la
  # clave
  veClave = clave.split(' ')
  for i in range(len(veClave)):
    veClave[i] = (veClave[i].split(':'))[::-1]
    veClave[i] = ''.join(list(filter(None, veClave[i])))
  
  # Quito los : del string
  contador = ''.join(contador.split(':')[::-1])
  veNonce = nonce.split(' ')
  
  # Divido le asigna un apsosicion de un vector a cada numero hexadecimal del
  # nonce
  for i in range(len(veNonce)):
    veNonce[i] = (veNonce[i].split(':'))[::-1]
    veNonce[i] = ''.join(list(filter(None, veNonce[i])))
  chacha_block(veClave, contador, veNonce)
  

def ROTL(a,b):
  return (((a) << (b)) & 0xffffffff | ((a) >> (32 - (b))))
  
# Uso 0xffffffff para evitar desbordamientos
def QR(x, a, b, c, d):
  x[a] = (x[a] + x[b]) & 0xffffffff
  x[d] = ROTL(x[d] ^ x[a], 16)
  x[c] = (x[c] + x[d]) & 0xffffffff
  x[b] = ROTL(x[b] ^ x[c], 12)
  x[a] = (x[a] + x[b]) & 0xffffffff
  x[d] = ROTL(x[d] ^ x[a], 8)
  x[c] = (x[c] + x[d]) & 0xffffffff
  x[b] = ROTL(x[b] ^ x[c], 7)
  
def chacha_block(clave, contador, nonce):
  S = [None] * 16
  # Asigno los valores fijos en el vector
  S[0] = hex(int('61707865', 16))
  S[1] = hex(int('3320646e', 16))
  S[2] = hex(int('79622d32', 16))
  S[3] = hex(int('6b206574', 16))
  # Incerto la clave
  for i in range(len(clave)):
    S[i + 4] = hex(int(clave[i], 16))
  S[12] = hex(int(contador, 16))
  for i in range(len(nonce)):
    S[i + 13] = hex(int(nonce[i], 16))
  
  # Imprimo El estado inicial
  auxVe = [0] * 16
  for i in range(len(S)):
    auxVe[i] = S[i][2:].zfill(8)
    
  print('Estado inicial=', end='')
  for i in range(len(auxVe)):
    if(i%4 == 0):
      print()
    print(auxVe[i], end=' ')
  print()
  
  x = [None] * 16
  for i in range(len(x)):
    num = int(S[i], 16)
    S[i] = num
    x[i] = S[i]

  for i in range(10):
    QR(x, 0, 4,  8, 12)
    QR(x, 1, 5,  9, 13)
    QR(x, 2, 6, 10, 14)
    QR(x, 3, 7, 11, 15)
    QR(x, 0, 5, 10, 15)
    QR(x, 1, 6, 11, 12)
    QR(x, 2, 7,  8, 13)
    QR(x, 3, 4,  9, 14)
  
  for i in range(len(x)):
    auxVe[i] = hex(x[i])[2:]
  print('\nEstado final tras las 20 iteraciones=', end='')
  for i in range(len(auxVe)):
    if(i%4 == 0):
      print()
    print(auxVe[i], end=' ')
  print()
  
  # print(x)
  out = [None] * 16
  for i in range(16):
    out[i] = x[i] + S[i]
    
    
  # Imprimo el estado se salida generado
  for i in range(len(out)):
    auxVe[i] = hex(out[i])[2:].zfill(8)
  # print('Estado de salida del generador=\n' + str(auxVe))
  
  print('\nEstado de salida del generador=', end='')
  for i in range(len(auxVe)):
    if(i%4 == 0):
      print()
    print(auxVe[i], end=' ')
  print()
  

menu()
