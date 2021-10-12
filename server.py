import socket
import threading


host = "127.0.0.1"
port = 5500

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host , port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)  
            '''
            if msg.decode("ascii").startswith("permission got and done"):
                
                print(message)
                broadcast(message)
            '''
            if "BYEBYE" in msg.decode("ascii"):
                kick = msg[7:]
                client.send("kicked".encode("ascii"))
                kick_user(kick)
                broadcast(f"{client} has left the chat")
            
            elif "permission request" in msg.decode("ascii"):
                client.send("permission granded".encode("ascii"))

            else:
                print("permission got and done")
                print(message)
                broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode("ascii"))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client , address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} has joined the chatroom".encode("ascii"))
        client.send("Connected to the server!".encode("ascii"))

        thread = threading.Thread(target = handle , args = (client ,))
        thread.start()

print("Server is listening...")


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        clients_to_kick = clients(name_index)
        clients.remove(clients_to_kick)
        clients_to_kick.send("Your connection terminated")
        nicknames.remove(name)
        broadcast(f"{name} has left the channel..." )


if __name__ == "__main__":
    receive()