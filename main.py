secret_message = "I Love Lucy!"
number = 101
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar_cipher(text: str, shift: int) -> str:
    
    result = ""

    for char in text: 
        if char in character_list:
          result += character_list[(character_list.index(char) + shift) % 62]
        else:
          result += char 

    return result 

def caeser_decipher(secret_message:str ) -> str:

  for shift in range(62): 
      result = ""
      for char in secret_message: 
          if char in character_list:
              result += character_list[(character_list.index(char) - shift) % 62]
          else:
              result += char

      print(f"shift {shift}: {result}")

hidden_message = caesar_cipher(secret_message, number)
print(secret_message)

caeser_decipher(hidden_message)