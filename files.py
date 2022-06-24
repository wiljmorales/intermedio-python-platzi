def read():
  numbers = []
  with open("./files/text.txt", "r", encoding="utf-8") as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def write():
  pass

def run():
  read()


if __name__ == "__main__":
  run()
