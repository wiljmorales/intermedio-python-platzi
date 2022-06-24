import random
def get_word():
  words = []
  with open('./files/hangman_words.txt', 'r', encoding="utf-8") as f:
    for word in f:
      words.append(word)
  return words[random.randint(0, len(words) - 1)]

def run():
  word = get_word().rstrip()

  # for letter in word:
  #   hiden_word += '_ '
  hiden_word = ''.join(["_ " for letter in word])
  print("adivina la palabra")
  print(hiden_word + "\n")


  user_input = input("elige una letra: ")
  while hiden_word.replace(" ", "") != word:
    if user_input in word:
      for i in range(len(word)):
        if word[i] == user_input:
          hiden_word = hiden_word.split(" ")
          hiden_word[i] = user_input
          hiden_word = " ".join(hiden_word)

    print(hiden_word + "\n")
    if hiden_word.replace(" ", "") == word:
      print("Ganaste")
    else:
      user_input = input("elige una letra: ")

if __name__ == '__main__':
  run()