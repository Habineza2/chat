import socket

def main():
    host = "127.0.0.1"  # localhost
    port = 55556

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Request user's name
    name = input("Enter your name: ")
    client_socket.send(name.encode())

    print("Connected to the server. Type 'quit' to exit.")

    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        client_socket.send(message.encode())

        # Receive the echoed message from the server
        response = client_socket.recv(1024).decode()
        print("Server:", response)

    client_socket.close()

if __name__ == "__main__":
    main()
