import socket
import threading

# SIMPLE UDP RECEIVER
def start_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 12345))
    print("🔊 Listening for messages on port 12345...")
    
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"FROM {addr}: {data.decode('utf-8')}")

# SIMPLE UDP SENDER  
def start_sender():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("📤 Type messages to send (Ctrl+C to quit):")
    
    while True:
        message = input()
        sock.sendto(message.encode('utf-8'), ('localhost', 12345))

# QUICK START
if __name__ == "__main__":
    print("UDP Chat - Choose:")
    print("1. Start RECEIVER (listen for messages)")
    print("2. Start SENDER (send messages)")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        start_receiver()
    elif choice == '2':
        start_sender()
    else:
        print("Invalid choice! Run again.")