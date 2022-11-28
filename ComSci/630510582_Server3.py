#lab_03
#tulakorn sawangmuang
#630510582
#server
import socket
import threading

Online_list = []
Client_list = []

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#create server and wait for connect
host = socket.gethostname()
port = 5679 #port for connection
Server_Socket.bind((host,port))
Server_Socket.listen(5)
print("{____SERVER_____} | Runing")


#Function for create threading
def Server_Onlinee():
    Count_Thread = 0
    print("{ SERVER | THREAD  }  | Online")
    while True:
        clientsocket,addr = Server_Socket.accept()
        Server_Message_Online = threading.Thread(target=Server_Message,args=[clientsocket,addr])
        Count_Thread += 1
        Server_Message_Online.start()
        print("{ SERVER | THREAD  }  | Start thread message client : ",Count_Thread)
        Client_list.append(clientsocket)


def Server_Message(client,addr):
    text_online = "\n { CLIENT  | ONLINE }  "

    while True:
        try:
            msg_client = client.recv(1024).decode("ascii")
        except:
            break
        
        if "[ Login ]" in msg_client:
            Online_list.append(list(addr))
            Online_list[-1].append(msg_client.replace("[ Login ] ",""))
            Online_list[-1].append(client)
            for Users in Online_list:
                text_online += "\n | "+ Users[2] + " | "
            for i in Client_list:
                i.send(text_online.encode("ascii"))
            print("{ SERVER | LOGIN   }  |",msg_client," to server.")
        elif "[ SELECT ]" in msg_client:
            C_Mes = msg_client.split('|')
            for Select_User_to_Send in Online_list:
                if (Select_User_to_Send[2] in msg_client) and (Select_User_to_Send[2] in C_Mes[1]):
                    Send_Text = "\n Message from " + C_Mes[3] + " : " + C_Mes[2]
                    Select_User_to_Send[3].send(Send_Text.encode("ascii"))
                    print("{ SERVER | MESSAGE }    | "+ C_Mes[3] +" Send message to :",Select_User_to_Send[2])
                    
        elif "[ QUIT ]" in msg_client:
            print("{ SERVER : LOGOUT  }   |" + msg_client + " from server. ")
            for Quit_ in Online_list:
                if Quit_[2] in msg_client:
                    Quit_[3].close()
                    Client_list.remove(Quit_[3])
                    Online_list.remove(Quit_)

                    
            for Users_Q in Client_list:
                Send_Q = "{ ONLINE }  | \n |"
                for use in Online_list:
                    Send_Q += use[2] + " | "
                Users_Q.send(Send_Q.encode("ascii"))
            break
        
Server_Online = threading.Thread(target=Server_Onlinee)
Server_Online.start()