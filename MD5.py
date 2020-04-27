import hashlib


my_begin = str(input("Enter the beginnning of the message: "))

def double_md5(message, x, begin):
  print(message, x, begin)
  return hashlib.md5(hashlib.md5(begin + message).digest()).hexdigest()[:x]

def floyd(x, initial):

  x0 = initial
  m0 = None
  m1 = None


  slow = double_md5(x0, x, my_begin)
  fast = double_md5(slow, x, my_begin)

  while slow != fast:
    slow = double_md5(slow, x, my_begin)
    fast   = double_md5(double_md5(fast, x, my_begin), x, my_begin)

  slow = x0
  
  while slow != fast:
    m0 = slow
    slow = double_md5(slow, x, my_begin)
    fast = double_md5(fast, x, my_begin)


  fast = double_md5(slow, x, my_begin)

  while slow != fast:
    m1 = fast
    fast = double_md5(fast, x, my_begin)



  print_results(m0, m1, double_md5(m0, x, my_begin))


def print_results(m0, m1, hash):
  print "First message:", my_begin + m0
  print "Second message:", my_begin + m1
  print "Hash of both:", hash

x = input("How many collisions bytes you need?: ")
floyd(x, "123456789xyz")
