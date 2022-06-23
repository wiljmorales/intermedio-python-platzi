def divisors(num):
  divisor = [i for i in range(1, num + 1) if num % i == 0]
  return divisor

def run():
  try:
    num = int(input('Ingrese un numero: '))
    print(divisors(num))
    print('Termino el programa')
  except ValueError:
    print("Debes ingresar un numero")

if __name__ == "__main__":
  run()