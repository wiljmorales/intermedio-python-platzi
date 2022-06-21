from unicodedata import name


def run():
  my_list = [1, "hello", True, 4.5]
  my_dict = {"firstname": "John", "lastname": "Doe"}

  super_list = [
    {"firstname": "John", "lastname": "Doe"},
    {"firstname": "Jane", "lastname": "Doe"},
    {"firstname": "Jack", "lastname": "Doe"},
  ]

  super_dict = {
    "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "integer_nums": [-4, -3, -2, -1, 0, 1, 2, 3, 4],
    "float_nums": [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
  }

  for key, value in super_dict.items():
    print(f"{key}: {value}")

if __name__ == '__main__':
  run()