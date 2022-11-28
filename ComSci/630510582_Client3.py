#lab_03
#tulakorn sawangmuang
#630510582
#client
import socket
import threading

Login_Username = "[ Login ] "
Connect = False

Socket_Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5679 # port connect to server

def Client_re(client):
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
        except:
            print("\n{ CLIENT } | Disconnect from [ Server ]")
            break
        if (not msg):
            break
        print(msg)

# login username to server
Username = input("\n{ CLIENT } | Username : ")
Login_Username += Username
if Username !="q":
    Socket_Client.connect((host,port))
    Socket_Client.send(Login_Username.encode("ascii"))
    Connect = True

Client_recv = threading.Thread(target=Client_re, args=(Socket_Client,))
Client_recv.start()
# when connecting
while Connect:
    User_ = input("{ CLIENT } | Chat to Username : ")
    if User_ == "q": # disconnect
        User_ = "[ QUIT ] | " + Username 
        print("/n{ CLIENT } | LOGOUT!!")
        Socket_Client.sendall(User_.encode("ascii"))
        break
    else: # send massage
        Message = input("\n{ CLIENT } | Message :")
        User_ = "[ SELECT ] | " + User_ + " | " + Message + " | " + Username
        Socket_Client.sendall(User_.encode("ascii"))
Socket_Client.close()


