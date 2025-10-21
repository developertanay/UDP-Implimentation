# 💬 UDP Chat — Simple Peer-to-Peer Messaging Tool

A lightweight, no-dependency chat program built with **Python and UDP sockets**.  
Run it on a single computer for testing or across multiple devices on the same network to chat instantly — no servers required!

---

## 🚀 Quick Start

### 🧩 Prerequisites
- Python 3.8 or later installed
- Both computers connected to the same network (for multi-device chatting)

---

### 🖥️ Run Locally (Single Computer Test)

Open **two terminal windows** in the same folder.

**In the first terminal (Receiver):**
```bash
python udp_chat.py

Choose **1** for RECEIVE mode.

**In the second terminal (Sender):**

```bash
python udp_chat.py
```

Choose **2** for SEND mode.

Type a message in the sender window — it will appear in the receiver window instantly.

---

### 🌐 Chat Between Two Computers

**On Computer A (Receiver):**

```bash
python udp_chat.py
```

Choose **1** for RECEIVE mode
Note your **IP address** (e.g., `192.168.1.5`).

**On Computer B (Sender):**

```bash
python udp_chat.py
```

Choose **2** for SEND mode
When asked, enter **Computer A’s IP address**.

Start chatting across your local network!

---

## 🎮 Commands

| Command    | Description          |
| ---------- | -------------------- |
| `/quit`    | Exit the chat        |
| `/clear`   | Clear the screen     |
| `/help`    | Show all commands    |
| `Ctrl + C` | Force quit instantly |

---

## 💡 Example

**Receiver:**

```
📩 [14:30:25] FROM 192.168.1.5: Hello there!
```

**Sender:**

```
You: Hello there!
```

---

## 🧠 Notes

* Works only on LAN (Local Network)
* UDP is **connectionless**, meaning messages might be missed if the receiver isn’t listening
* Great for learning basic **network programming** and **socket communication**
