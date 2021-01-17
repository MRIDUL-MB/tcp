import socket
import threading
import subprocess

def socketFunction(con,add):
    print(add)
#    con.send(b'hello i am server')
    password = (con.recv(1024)).decode()
    if password == '<your password>':  #your password
        con.send(b'successfully login...')
        while True:
            data = (con.recv(1024)).decode()
            if data == 'exit':
                break
            output = subprocess.getoutput(data)
            con.send(output.encode())
    else:
        con.send(b'password is wrong...Try again')
        con.close()
        

with  socket.socket() as s:  #By default it is tcp
    ip,port = '',1234
    s.bind((ip,port))
    s.listen()
    while True:
        con,add = s.accept()
        t = threading.Thread(target=socketFunction,args=(con,add)).start()
