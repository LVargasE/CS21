x = 6
y = 4

def main(x, y):
  sumOfx, sumOfy = example(x, y)
  sumOfxx, sumOfyy = example2(x, y)
  xsum = sumOfx + sumOfxx
  ysum = sumOfy + sumOfyy
  sum = xsum + ysum

  example(x, y)

  example2(x, y)

  print(x)
  print(y)
  print(xsum)
  print(ysum)
  print(sum)

def example(x, y):
  print(x)
  print(x + y)
  x+=5
  y+=10
  print(x, y)

  return x, y

def example2(x, y):
  print(x)
  print(x + y)
  x+=10
  y+=15
  print(x, y)

  return x, y

main(x, y)
