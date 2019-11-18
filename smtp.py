# Ryan Chen - 893219394
# CSPC 471
# This program sends an email

from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Optional Exercise 1 - Start
clientSocket.send('STARTTLS\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Wrap client socket with SSL
sslClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

# Initate authentication
authLogin = 'AUTH LOGIN\r\n'
sslClientSocket.send(authLogin.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)

# Send username - Username removed
username = 'ENTER USERNAME HERE'
sslClientSocket.send(base64.b64encode(username.encode()) + '\r\n'.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)

# Send Password - Password removed
password = 'ENTER PASSWORD HERE'
sslClientSocket.send(base64.b64encode(password.encode()) + '\r\n'.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)
# Optional Exercise 1 - end

# Send MAIL FROM command and print server response. - Email address removed
mailFrom = 'MAIL FROM: <ENTER SENDER HERE>\r\n'
sslClientSocket.send(mailFrom.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. - Email address removed
rcptTo = 'RCPT TO: <ENTER RECIPIENT HERE>\r\n'
sslClientSocket.send(rcptTo.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
sslClientSocket.send(msg.encode())

# Message ends with a single period.
sslClientSocket.send(endmsg.encode())
recv1 = sslClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quit = 'QUIT\r\n'
sslClientSocket.send(quit.encode())
sslClientSocket.close()