''' TCPClient.py
usage: python TCPClient.py HOSTNAMEorIP PORT
Reads text from user, sends to server, and prints answer
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((turing.uark.edu, 5555))

#hangman 
print 'Welcome to hangman!'
print 'The word is _ _ _ _ _'
while 1:
  
  # Connect to server using hostname/IP and port
  # Get sentence from user
  sentence = raw_input('Input guess: ')
  # Send it into socket to server
  if sentence == '':
      while sentence == '':
          sentence = raw_input('Try again please: ')
 

  clientSocket.send(sentence)

  # Receive response from server via socket
  modifiedSentence = clientSocket.recv(1024)

  print 'From Server: ', modifiedSentence
  #Win or Lose 
  if modifiedSentence == 'You won! :D The answer is "Arkansas".' or modifiedSentence == 'You lost :( The answer was "Arkansas"':
    break
  
clientSocket.close()
