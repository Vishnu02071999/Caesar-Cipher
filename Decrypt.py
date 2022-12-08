def decryption(Encrypted_Word, shift):
  Alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
  ]
  new_word = ""
  position = 0
  new_position = 0
  for letters in Encrypted_Word:
    if letters in Alphabets:
      position = Alphabets.index(letters)
      new_position = position - shift
      if new_position >= (25-shift):
        new_word = new_word + Alphabets[new_position]
      elif new_position < (25-shift):
        new_word = new_word + Alphabets[new_position]
    else:
      new_word += letters
  print(f"The decrypted word is : {new_word}")
