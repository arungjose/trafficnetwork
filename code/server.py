# Server code --> Node A
from socket import *
from time import *
filename= 'junc_a.txt'
def readfile(filename):
    with open(filename, 'r') as file:
        data_read = file.read()
        return(data_read)
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen()
print('Server listening at 12000')
connection, address = server.accept()
print('Connected to client')
data =readfile(filename)
connection.send(bytes(data + '\n' + ctime(), 'utf-8'))
recData = connection.recv(1024).decode()
print('Client:', recData)
connection.close()