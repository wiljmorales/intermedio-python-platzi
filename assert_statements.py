def divisors(num):
  divisor = [i for i in range(1, num + 1) if num % i == 0]
  return divisor

def run():
  num = input('Ingrese un numero positivo: ')
  assert num.isnumeric(), "Debes ingresar un numero"
  print(divisors(int(num)))
  print('Termino el programa')


if __name__ == "__main__":
  run()