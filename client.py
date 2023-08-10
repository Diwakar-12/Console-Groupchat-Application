import socket

import threading

client_socket = socket.socket()
host = socket.gethostname()
port = 5050


name=input("Enter your name : ")

client_socket.connect((host, port))

client_socket.send(name.encode("utf-8"))

def sendmsg():
    print("Type 'bye' to exit the chat!")
    while True:
        
        ms=input()
        msg=f"{name} : {ms}"
        try:
            if(ms != "bye"):
                client_socket.send(msg.encode("utf-8"))
            else :
                k=1/0 
        except:
            print("You left")
            client_socket.close()
            break


def recmsg():
    while True:
        try:
            rec=client_socket.recv(1024).decode()
            print(rec)
        except:
            print("Connection lost to server")
            break


t1=threading.Thread(target=sendmsg)
t2=threading.Thread(target=recmsg)

t1.start()
t2.start()







