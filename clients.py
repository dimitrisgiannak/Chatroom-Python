import socket
import threading

nickname = input("Please choose a nickname: ")

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(("127.0.0.1" , 5500))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))

            elif message == "permission granded":
                if "BYEBYE" not in message1 :
                   print(message)
                
                client.send(message1.encode("ascii"))
               
            elif message == "kicked":
                client.close() 
                break
                
            else:
                print(message)
              
        except:
            print("An error occurred!")
            client.close()
            break

def write():
   
    while True:
        global message1
        permission = False
        message1 = f"{nickname} : {input('')}"
        
        if permission == False:
            client.send("permission request".encode("ascii"))
          




receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
