# Program 9
# This program can manipulate strings based on what the user tells it to do, and then returns the transformed string back to them.

# Sai Gottemukkula
# Date Completed: 12/21/2020 

X = 0
S = 0
L = 0
P = 0


def LS_X(word):
  loop_number = 0
  while loop_number <= X:  
    word = word[1:] + '#'
    loop_number = loop_number + 1
  print(word)
  return(word)

def RS_X(word):
  loop_number = 0
  while loop_number <= X:
    word = '#' + word[:-1]
    loop_number = loop_number + 1
  print(word)
  return(word)

def LC_X(word):
  loop_number = 0
  while loop_number <= X:
    character = word[0]
    word = word[1:] + character
    loop_number = loop_number + 1
  print(word)
  return(word)
    

def RC_X(word):
  loop_number = 0
  while loop_number <= X:
    character = word[-1]
    word = character + word[:-1]
    loop_number = loop_number + 1
  print(word)
  return(word)

def REV_SL(word):
  loop_number = 0
  while loop_number <= X:
    count = len(word) - 1
    new_word = ''
    while count >= 0:
      new_word = new_word + word[count]
      count = count - 1
      loop_number = loop_number + 1
  print(new_word)
  return(new_word)

def SWAP_SLP(word):
  loop_number = 0
  pass  


def main():
  #This is where you will write the main components of your program, the looping, user input and calling of functions

  #The program should loop four times receiving a line of input each time and call the correct functions as needed
  # Delete the word pass and write your code there, then delete this comment
  print('Welcome to the String Manipulator')
  line = str(input('\nPlease enter a line to manipulate and manipulators: '))
  if line[0:3] == 'LS-':
    line[3:]
    X = int(line[3])
    print(X)
    for item in range(len(line)):
      if item == ''

LS_X('Abcxyzmno')
RS_X('Abcxyzmno')
LC_X('computer')
RC_X('computer')
REV_SL('computer')

main()