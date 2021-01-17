import socket
import getpass

with socket.socket() as s:
    ip,port='192.168.43.173',1234
    s.connect((ip,port))
 #   name = input('Whats your name: ')
#    s.send((f'{name} is connected..').encode())
    password = getpass.getpass('Enter Password: ')
    print()
    s.send(password.encode())
    login = (s.recv(1024)).decode()
    print(login)
    if login == 'password is wrong...Try again':
        print('bye')
    else:
        while True:
            data = input('root@localhost: ')
            print()
            if data=='exit':
                print('Ba Bye...')
                break
            s.send(data.encode())
            print((s.recv(100000)).decode())
            print()
