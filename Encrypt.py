def encryption(Encrypt_Word, shift):
  Alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
  ]
  new_word = ""
  position = 0
  new_position = 0
  div=0
  for letters in Encrypt_Word:
    if letters in Alphabets:
      position = Alphabets.index(letters)
      # if position == 26 or position == 27 or position == 28:
      #   new_word += Alphabets[position]
      if position <= (25-shift):
        new_position = position + shift
        new_word = new_word + Alphabets[new_position]
        new_position = 0
      elif position > (25-shift):
        new_position = position + shift-1
        new_position-=25
        new_word = new_word + Alphabets[new_position]
        new_position = 0
    else:
      new_word += letters
  print(f"The encrypted word is : {new_word}")
