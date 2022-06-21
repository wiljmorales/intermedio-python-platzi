def run():
  super_list = [i for i in range(1, 100000) if i % 36 == 0]
  print(super_list)

if __name__ == "__main__":
  run()