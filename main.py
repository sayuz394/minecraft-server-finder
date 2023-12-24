from mcstatus import JavaServer


server_address = input("Your Ip Adress : ")
server_port = 25562
amount = int(input("Amount : "))
i = 0
while i <= amount:    
    server_port += 1
    i += 1
    try: 
        server = JavaServer(server_address, server_port)
        status = server.status()      
        print(f"Server {server_address}:{server_port} is online")
        print(f"Version: {status.version.name}")
        print(f"Players: {status.players.online}/{status.players.max}")
        print(f"Description: {status.description['text']}")
    except:
        print("Not Found")
