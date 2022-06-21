import math
def run():
  # my_dict = {}
  # for i in range(1,11):
  #   if i % 3 != 0:
  #     my_dict[i] = i ** 3

  my_dict = {i: i ** 3 for i in range(1,11) if i % 3 != 0}
  
  print(my_dict)
  
  roots = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}
  print(roots)
if __name__ == "__main__":
  run()