#import socket module
from socket import *
import sys #In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverName = 'hostname'
serverPort = 12330
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True :
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try :
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html \n\n'.encode())
        connectionSocket.send(outputdata.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        errorMessage = ('404 Not Found: ' + filename + "\r\n")
        connectionSocket.send(errorMessage.encode())
        connectionSocket.close()
        #Fill in end
        #Close client socket
        #connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
