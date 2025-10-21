# UDP Chat - Simple Messaging Tool

A dead-simple way to send messages between computers using Python. No setup, no installs, just run and chat!

## 🚀 Quick Start

### On One Computer (Testing)

1. **Save the code** as `udp_chat.py`

2. **Open two terminals**

3. **In first terminal - listen for messages:**
   ```bash
   python udp_chat.py
   ```
   Choose `1` for RECEIVE mode

4. **In second terminal - send messages:**
   ```bash
   python udp_chat.py
   ```
   Choose `2` for SEND mode

5. **Start chatting!** Type in sender, see messages in receiver.

### On Different Computers

**Computer A (Receiver):**
- Run `python udp_chat.py`
- Choose `1`
- Note your IP address

**Computer B (Sender):**
- Run `python udp_chat.py` 
- Choose `2`
- Enter Computer A's IP when asked

## 🎮 How to Use

**When running, you can:**
- Just type messages to send
- `/quit` - exit program
- `/clear` - clean the screen
- `/help` - show commands
- `Ctrl+C` - emergency quit

## 💡 What You'll See

**Receiver sees:**
```
📩 [14:30:25] FROM 192.168.1.5: Hello there!
```

**Sender types:**
```
You: Hello there!
```


#DEMO
<img width="866" height="746" alt="image" src="https://github.com/user-attachments/assets/ae9647d6-5ff6-41d0-a3c9-fdcabfd99180" />
<img width="1525" height="673" alt="image" src="https://github.com/user-attachments/assets/03b61109-0c20-44de-896c-62dcd7a9775e" />
