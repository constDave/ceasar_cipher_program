
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_chars = [' ', '!', '.', '?', '1','2','3','4','5','6','7','8','9','0']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):

  message = ""
  if shift > 26:
    shift = shift % 26
  for letter in text:
    if letter in special_chars:
      message += letter
    else:
      position = alphabet.index(letter)
      encode_shift = position + shift
      decode_shift = position - shift
      new_position = encode_shift if direction == "encode" else decode_shift
      message += alphabet[new_position]
  print(f"The message is {message}")

caesar(text, shift, direction)

continue_game = input("Would you like to rerun the program? ").lower()

while continue_game == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  continue_game = input("Would you like to rerun the program? ").lower()
  if continue_game != "yes":
    print("Goodbye.")

  


