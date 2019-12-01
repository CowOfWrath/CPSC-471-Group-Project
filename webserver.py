#import socket module
from socket import *
import sys #In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

serverPort = 12346 #port used
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #limit # of connections to 1

while True :
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try :
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        errorMessage = ('404 Not Found: ' + filename + "\r\n")
        connectionSocket.send(errorMessage.encode())
        connectionSocket.close()
        #Close client socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
