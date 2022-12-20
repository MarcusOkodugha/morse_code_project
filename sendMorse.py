import winsound
import time
import tkinter as tk

def string_to_morse(input_string):
  # Create a dictionary with the Morse code translations
  morse_code = {
    '0': '11111',
    '1': '01111',
    '2': '00111',
    '3': '00011',
    '4': '00001',
    '5': '00000',
    '6': '10000',
    '7': '11000',
    '8': '11100',
    '9': '11110',
    'a': '01',
    'b': '1000',
    'c': '1010',
    'd': '100',
    'e': '0',
    'f': '0010',
    'g': '110',
    'h': '0000',
    'i': '00',
    'j': '0111',
    'k': '101',
    'l': '0100',
    'm': '11',
    'n': '10',
    'o': '111',
    'p': '0110',
    'q': '1101',
    'r': '010',
    's': '000',
    't': '1',
    'u': '001',
    'v': '0001',
    'w': '011',
    'x': '1001',
    'y': '1011',
    'z': '1100'
  }

  # Initialize an empty result string
  result = ''

  # Loop through each character in the input string
  for char in input_string:
    # If the character is a space, add a space to the result string
    if char == ' ':
      result += ' '
    # Otherwise, look up the Morse code translation and add it to the result string
    else:
      result += morse_code[char.lower()] + ' '

  # Return the result
  return result

def play_morse(morse_string):
  # Loop through each character in the Morse code string
  for char in morse_string:
    # If the character is a 1, play a long beep
    if char == '1':
      winsound.PlaySound('longBeep_1.wav', winsound.SND_FILENAME)
      #winsound.Beep(700, 300)
      #time.sleep(0.200)
    # If the character is a 0, play a short beep
    elif char == '0':
      winsound.PlaySound('shortBeep_0.wav', winsound.SND_FILENAME)
      #winsound.Beep(700, 50)
      #time.sleep(0.025)
    # If the character is a space, pause for a short time
    elif char == ' ':
      time.sleep(0.0125)
    # If the character is a double space, pause for a longer time
    elif char == '  ':
      time.sleep(0.025)


def get_input():
    input_string = input_box.get("1.0", "end-1c")
    # You can now use the input string for whatever purpose you desire
    # For example, you could pass it to a function or print it to the console
    print(input_string)
    input_string = string_to_morse(input_string)
    print(input_string)
    play_morse(input_string)

root = tk.Tk()

# Create a text box
input_box = tk.Text(root)
input_box.pack()

# Create a button to retrieve the input from the text box
button = tk.Button(root, text="Send Morse", command=get_input)
button.pack()
root.mainloop()