# Client code --> Node B
from socket import *
from time import *
filename= 'junc_b.txt'
def readfile(filename):
    with open(filename, 'r') as file:
        data_read = file.read()
        return(data_read)    
client=socket()
client.connect(('localhost',12000))
print('connected to server ')    
recData=client.recv(1024).decode()
print('serever : ',recData)
data=readfile(filename)
client.send(bytes(data + '\n' + ctime(),'utf-8'))
client.close()