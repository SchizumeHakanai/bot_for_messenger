## 🤖 Messenger Bot (fbchat_muqit)

A simple Facebook Messenger bot written in Python using the **`fbchat_muqit`** library.  
The bot listens for messages starting with the **`!`** prefix and executes simple text commands.

---

### ⚙️ Commands
- **`!test`** — replies with a test message.  
- **`!losuj`** — generates a random number between 1 and 90 and sends it as a reply.  

---

### 🧩 Structure
```python
COOKIES_FILE = "cookies.json"  # File containing Facebook session data
PREFIX = "!"                   # Command prefix
````

The bot listens for messages and responds only to those starting with the defined prefix (`!`).

---

### 🚀 Setup & Run

#### 1. Install the required packages:

```bash
pip install fbchat-muqit asyncio
```

#### 2. Create a `cookies.json` file

This file should contain your Facebook session data (obtained using the C3C FBState Utility).

#### 3. Run the bot:

```bash
python main.py
```

After a successful login, the console will display:

```
Online: account_name
```

---

### ⚠️ Disclaimer

* Using automation bots on Messenger may violate Meta’s Terms of Service — use responsibly.
* This project is intended **for educational and testing purposes only.**

---

### 📄 License

This project is released under the **MIT License** — feel free to modify and improve it.

```
