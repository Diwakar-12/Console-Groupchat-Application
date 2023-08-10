# importing required modules
import socket	
import datetime

import threading



clientlist={}
# initializing socket
server_socket = socket.socket()	
host = socket.gethostname()
port = 5050

# binding port and host
server_socket.bind((host, port))
# print(s)
# print()

# waiting for a client to connect
server_socket.listen()

def rec(client):
    c=clientlist[client]
    while True:
        try:
            msg=client.recv(1024)
            for clients in clientlist:
                if(client!=clients):
                    clients.send(msg)
        except:
            msg=f'{c} has left the chat'.encode("utf-8")
            for clients in clientlist:
                if(client!=clients):
                    clients.send(msg)
            
            del clientlist[clients]
            client.close()
            break
    



	
while True:
# accept connection & create a dedicated port for client and server
    client_socket, addr = server_socket.accept()

    name=client_socket.recv(1024).decode() 


    clientlist[client_socket]=name

    for clients in clientlist:
        if(clients!=client_socket):
            clients.send(f'{name} has joined the chat'.encode("utf-8"))
    
    thread1=threading.Thread(target=rec,args=(client_socket,))
    thread1.start()

    
    # date = datetime.datetime.now()
    # d = str(date)

    # sending data type should be string and encode before sending
    # c.send(f'{name} you are connected now \n'.encode())	
    






