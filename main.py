import art



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

restart = True

while restart == True:

  direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n").lower()
  if direction == "encode" or direction == "decode":

    text = input("Type your message: \n").lower()
    shift = int(input("type the shift number: \n"))
    shift = shift % 26

    #single function for both encryption and decryption.
    def caesar(text_msg, shift_num, caesar_direction):
      message = ""
      for char in text_msg:
        if char in alphabets:
          
          position = alphabets.index(char)

          if caesar_direction == "encode":
            new_position = position + shift_num
          else:
            new_position = position - shift_num
          
          new_char = alphabets[new_position]
          message += new_char
        else:
          message += char
      print(f"the {caesar_direction}d message will be {message}\n\n")

    caesar(text_msg = text, shift_num = shift, caesar_direction = direction)
  
  else:
    print("Invalid input. Only 'encode' and 'decode' allowed.\n")

  restartInput = input("Do you want to restart? Y or N ?\n")
  
  if restartInput == "Y" or restartInput == "N":
    if restartInput == "Y":
      restart = True
    else:
      restart = False
      print("Thank you!")
  else:
    restart = False
    print("give the valid input - Y or N")


      

