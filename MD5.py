from hashlib import md5


#my_begin = str(input("Enter the beginnning of the message: "))
my_begin = b'\x42\x66\x37'

def double_md5(message, x, begin):
  print(message, x, begin)
  return md5(md5(begin + message).digest()).digest()[:x]

def double_md5_II(message, x, begin):
  # print(message, x, begin)
  return md5(md5(begin + message).digest()).hexdigest()[:x*2]

def floyd(x, initial):

  x0 = initial
  m0 = None
  m1 = None


  turtle = double_md5(x0, x, my_begin)
  hare = double_md5(turtle, x, my_begin)

  while turtle != hare:
    turtle = double_md5(turtle, x, my_begin)
    hare   = double_md5(double_md5(hare, x, my_begin), x, my_begin)

  turtle = x0
  
  while turtle != hare:
    m0 = turtle
    turtle = double_md5(turtle, x, my_begin)
    hare = double_md5(hare, x, my_begin)


  hare = double_md5(turtle, x, my_begin)

  while turtle != hare:
    m1 = hare
    hare = double_md5(hare, x, my_begin)

  print_results(m0, m1, double_md5_II(m0, x, my_begin))
  print_results_hex(m0, m1, double_md5_II(m0, x, my_begin))


#wynik w  bajtach

def print_results(m0, m1, hash):
  print('___________________________________')
  print('Bytes results: ')
  print('First message:', my_begin + m0)
  print('Second message:', my_begin + m1)
  print('Hash of both:', hash)


#wynik w hexach

def print_results_hex(m0, m1, hash):
  print('___________________________________')
  print('Hex results: ')
  print('First message:', (my_begin + m0).hex())
  print('Second message:', (my_begin + m1).hex())
  print('Hash of both:', hash)

x = int(input('How many collisions bytes you need?: '))
floyd(x, b'123456789xyz')


