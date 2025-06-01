import sys
number = int(sys.argv[1])

print("a")

def divide(number):
  for i in range(1, number+1):
    if number % i == 0:
      print(i, end="a ")

  return 3
