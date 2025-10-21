import socket
import threading
import time
import sys

class SimpleUDP:
    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.running = False
        
    def clear_screen(self):
        """Clear the console screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        """Display program banner"""
        print("=" * 50)
        print("       SIMPLE UDP CHAT PROGRAM")
        print("=" * 50)
        print("Commands:")
        print("  /quit - Exit program")
        print("  /clear - Clear screen")
        print("  /help - Show this help")
        print("=" * 50)
    
    def start_receiver(self):
        """Start UDP receiver in a separate thread"""
        self.running = True
        receiver_thread = threading.Thread(target=self._receiver)
        receiver_thread.daemon = True
        receiver_thread.start()
        print("✅ Receiver started on port 12345")
        return receiver_thread
    
    def _receiver(self):
        """UDP receiver function"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.bind((self.host, self.port))
            sock.settimeout(1.0)  # 1 second timeout
            
            while self.running:
                try:
                    data, addr = sock.recvfrom(1024)
                    message = data.decode('utf-8')
                    timestamp = time.strftime("%H:%M:%S")
                    print(f"\n📩 [{timestamp}] FROM {addr[0]}:{addr[1]}: {message}")
                    print("You: ", end="", flush=True)  # Keep input prompt visible
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:  # Only print errors if we're supposed to be running
                        print(f"\nReceiver error: {e}")
                        
        finally:
            sock.close()
    
    def start_sender(self):
        """Start UDP sender"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        target_host = input("Enter target IP (localhost for same machine): ").strip()
        target_host = target_host if target_host else 'localhost'
        
        print(f"📤 Ready to send messages to {target_host}:12345")
        print("Type your messages below:")
        
        try:
            while True:
                try:
                    message = input("You: ").strip()
                    
                    # Handle commands
                    if message == '/quit':
                        break
                    elif message == '/clear':
                        self.clear_screen()
                        self.show_banner()
                        continue
                    elif message == '/help':
                        self.show_banner()
                        continue
                    elif not message:
                        continue
                    
                    # Send message
                    sock.sendto(message.encode('utf-8'), (target_host, self.port))
                    
                except KeyboardInterrupt:
                    print("\n\nExiting...")
                    break
                except Exception as e:
                    print(f"Error sending message: {e}")
                    
        finally:
            self.running = False
            sock.close()
    
    def run_chat(self):
        """Run the complete chat application"""
        self.clear_screen()
        self.show_banner()
        
        print("\nChoose mode:")
        print("1. Receive only (wait for messages)")
        print("2. Send only (send messages to others)")
        print("3. Both (send and receive on this machine)")
        
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == '1':
            print("\n🎯 RECEIVE MODE - Waiting for incoming messages...")
            receiver_thread = self.start_receiver()
            input("Press Enter to stop receiving...\n")
            self.running = False
            receiver_thread.join(timeout=2)
            
        elif choice == '2':
            print("\n🎯 SEND MODE - Ready to send messages")
            self.start_sender()
            
        elif choice == '3':
            print("\n🎯 DUAL MODE - Both sending and receiving")
            receiver_thread = self.start_receiver()
            time.sleep(1)  # Give receiver time to start
            self.start_sender()
            self.running = False
            receiver_thread.join(timeout=2)
            
        else:
            print("Invalid choice!")

def main():
    """Main function"""
    chat = SimpleUDP()
    
    try:
        chat.run_chat()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Thanks for using UDP Chat!")

if __name__ == "__main__":
    main()