

 🕵️ Basic Network Sniffer

A simple Network packet sniffer built using Python, Scapy, Flask, and Tailwind CSS.
This project captures live network traffic, analyzes packet details, and displays them in a clean web-based dashboard.

 🚀 Features

* Capture live network packets in real-time
* Extract useful details:

  * Source IP
  * Destination IP
  * Protocol
  * Payload (Preview)
* Web-based UI with **Flask + Tailwind CSS
* Auto-refreshing packet table every few seconds
* Works on **Windows & Linux** (requires WinPcap/Npcap on Windows)

---

📂 Project Structure

Basic-Network-Sniffer/
│── app.py           # Flask backend
│── sniffer.py       # Packet sniffing logic using scapy
│── templates/
│   ├── head.html    # Common head with Tailwind setup
│   ├── index.html   # Main UI
│── static/          # (Optional) custom JS/CSS
│── requirements.txt # Dependencies

 ⚙️ Requirements

* Python 3.x
* Flask
* Scapy
* Tailwind (via CDN, already included in templates)
* **Npcap/WinPcap** (for Windows packet sniffing)

Install dependencies:

bash
pip install -r requirements.txt


---

## ▶️ Usage

1. Start the Flask app:

   ```bash
   python app.py
   ```
2. Open browser and go to:

  
   http://127.0.0.1:5000
 


 🔒 Disclaimer

⚠️ This project is for educational purposes only.
Use responsibly and only on networks you own or have permission to monitor.

