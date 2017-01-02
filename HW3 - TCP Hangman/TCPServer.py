''' TCPServer.py
usage: python TCPServer.py PORT
Reads in text, changes all letters to uppercase, and returns
the text to the client
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

#Alphabet to check against
answer = ['A', 'r', 'k', 'a', 'n', 's', 'a','s']
guess = [None, None, None, None, None, None, None, None]

def Guess(letter):
        out = ''
        if letter == 'a':
            guess[0] = 'A'
            guess[3] = 'a'
            guess[6] = 'a'
        elif letter == 'r':
            guess[1] = 'r'
        elif letter == 'k':
            guess[2] = 'k'
        elif letter == 'n':
            guess[4] = 'n'
        elif letter == 's':
            guess[5] = 's'
            guess[7] = 's'
        else:
            return '{0} is incorrect.'.format(letter) 
        #builds the output to send to the client    
        
        return None


def Make_String():
	out = ''
	for l in range(len(guess)):
	    if guess[l] != None:
                out += guess[l]
	    else:
	        out += '_'
        return out

# Set port number by converting argument string to integer
serverPort = 5555

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print "The server is ready to receive"

connectionSocket, addr = serverSocket.accept()

#Eight guesses
i = 7 
while True:
  # Wait for connection and create a new socket
  # It blocks here waiting for connection
#  connectionSocket, addr = serverSocket.accept()

  # Read bytes from socket
  letter = connectionSocket.recv(1024)
  letter = letter.lower()
  #Gives us the guess string

  out_letter = Guess(letter)
  i = i - 1  
  if Make_String() == 'Arkansas':
      connectionSocket.send('You won! :D The answer is "Arkansas".')
      break
  elif out_letter == None:
      connectionSocket.send('{0} Correct! You have {1} guesses left.'.format(Make_String(), i))
  elif i == 0:
      connectionSocket.send('You lost :( The answer was "Arkansas"')   
      break
  else:
      connectionSocket.send('{0} {1} You have {2} guesses left.'.format(Make_String(), out_letter, i))

# Close connection to client but do not close welcome socket
connectionSocket.close()
