# CodeAlpha_Basic_Network_Sniffer

A lightweight Python-based network packet sniffer developed during my Cybersecurity Internship at CodeAlpha. This tool captures network traffic in real-time, extracts essential header data, and provides a clear breakdown of network flows.

## 🚀 Features
* **Real-Time Capture:** Continuously intercepts incoming and outgoing network packets.
* **IP Layer Parsing:** Extracts and displays Source and Destination IP addresses.
* **Protocol Identification:** Detects and classifies packet protocols (TCP, UDP, and ICMP).
* **Payload Preview:** Formats and prints a safe raw preview of the data payload inside the packets.

## 🛠️ Prerequisites & Installation

### 1. Requirements
* Python 3.x
* Administrative/Root privileges (required to open raw sockets for packet sniffing)

### 2. Dependencies
Install the required `scapy` library via pip:
```bash
pip install scapy
```

## 💻 Usage

Run the script with administrator privileges to allow packet capture:

* **Windows (Command Prompt as Admin):**
  ```cmd
  python sniffer.py
  ```

* **Linux / macOS:**
  ```bash
  sudo python3 sniffer.py
  ```

## 📋 Sample Output

```text
--- Starting Basic Network Sniffer ---
Listening for network traffic... Press Ctrl+C to stop.

[+] New Packet Captured:
    Source IP      : 192.168.1.15
    Destination IP : 142.250.190.46
    Protocol       : TCP (6)
    Payload Summary: b'GET / HTTP/1.1\r\(\nHost:\) google.com\r\n...'
```

## 🛑 Disclaimer
This project is developed strictly for educational and cybersecurity training purposes under the CodeAlpha Internship program. Unauthorized network sniffing on infrastructure you do not own or have explicit permission to test is strictly prohibited and illegal.
