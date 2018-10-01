import socket
import time

HOST = "misc.chal.csaw.io"
PORT = 9002

GOOD = "YAAAAAY keep going\n"

def expression(expr):

    flag = 0

    while expr[1] == '(':
        time.sleep(0.1)

        i = 0
        j = len(expr)

        test = expr
        print expr + '\n'

        while i < j:
    	    if expr[i] == '(':
		i += 1
	    else:
        	if expr[i] != 'X':
		    if expr[i+4] != 'X' and expr[i+5] != 'X':
		        ex = expr[i:].split(')')[0]
		        new = ex.split()
                        if 'X' not in new[0] and 'X' not in new[2]:
                            if new[1] == '+':
		                res = int(new[0]) + int(new[2])
		            if new[1] == '-':
		                res = int(new[0]) - int(new[2])
		            if new[1] == '*':
		                res = int(new[0]) * int(new[2])
		            if res < 0 and expr[i-3] == '-':
		                expr = expr[0:i-3] + '+ ' + str(-res) + expr[i+len(ex)+1:]    
		            else:
		                expr = expr[0:i-1] + str(res) + expr[i+len(ex)+1:]
		            if test != expr:
		                print expr + '\n'
                        else:
                            flag = 1
		while expr[i] != '(' and expr[i] != '=':
		     i += 1
		if expr[i] == '=':
		     j = 0
	if test == expr:
    	    break

    if flag == 0:
        i = expr.find('X')
        if expr[i+1] == ')':
            expr = expr[:i+1] + expr[i+2:]
            while expr[i] != '(':
                i -= 1
            expr = expr[:i] + expr[i+1:]
        print expr + '\n'

    i = expr.find('=')
    print i
    while expr[i-2] != ')' and expr[i-2] != 'X':
        data = expr.split()
	if data[-4] == '*':
            print "first if"
	    if data [-5][-1] != ')' and data[-5][-1] != 'X':
                if (data[-3][-2:] != '.0' or data[-5][-2:] != '.0') and ('.' in data[-3] or '.' in data[-5]):
                    res = float(data[-3]) * float(data[-5])
	            expr = ' '.join(data[:-5]) + ' ' + str(res) + ' ' + ' '.join(data[-2:])
                else:
                    res = int(float(data[-3])) * int(float(data[-5]))
                    expr = ' '.join(data[:-5]) + ' ' + str(res) + ' ' + ' '.join(data[-2:])
            else:
                try:
	            res = float(data[-1]) / float(data[-3])
                    expr = ' '.join(data[:-4]) + ' ' + ' '.join(data[-2]) + ' ' + str(res)
                except ZeroDivisionError:
                    return "X = 0"
	if data[-4] == '-':
            if (data[-1][-2:] != '.0' or data[-3][-2:] != '.0') and ('.' in data[-1] or '.' in data[-3]):
                res = float(data[-1]) + float(data[-3])
                expr = ' '.join(data[:-4]) + ' ' + ' '.join(data[-2]) + ' ' + str(res)
            else:
	        res = int(float(data[-1])) + int(float(data[-3]))
	        expr = ' '.join(data[:-4]) + ' ' + ' '.join(data[-2]) + ' ' + str(res)
	if data[-4] == '+':
            if (data[-1][-2:] != '.0' or data[-3][-2:] != '.0') and ('.' in data[-1] or '.' in data[-3]):
                res = float(data[-1]) - float(data[-3])
                expr = ' '.join(data[:-4]) + ' ' + ' '.join(data[-2]) + ' ' + str(res)
            else:
	        res = int(float(data[-1])) - int(float(data[-3]))
	        expr = ' '.join(data[:-4]) + ' ' + ' '.join(data[-2]) + ' ' + str(res)

	i = expr.find('=')
        if expr[i-2] == ')':
	    expr = expr[1:i-2] + expr[i-1:]
	print expr + '\n'
        time.sleep(0.1)
        if ')' in expr.split()[-3]:
            if expr.split()[1] == '+':
                if (expr.split()[-1][-2:] != '.0' or expr.split()[0][-2:] != '.0') and ('.' in expr.split()[-1] or '.' in expr.split()[0]):
                    res = float(expr.split()[-1]) - float(expr.split()[0])
                    expr = ' '.join(expr.split()[2:-1]) + ' ' + str(res)
                else:
                    res = int(float(expr.split()[-1])) - int(float(expr.split()[0]))
                    expr = ' '.join(expr.split()[2:-1]) + ' ' + str(res)
            elif expr.split()[1] == '-':
                if (expr.split()[-1][-2:] != '.0' or expr.split()[0][-2:] != '.0') and ('.' in expr.split()[-1] or '.' in expr.split()[0]):
                    res = float(expr.split()[0]) - float(expr.split()[-1])
                    expr = ' '.join(expr.split()[2:-1]) + ' ' + str(res)
                else:
                    res = int(float(expr.split()[0])) - int(float(expr.split()[-1]))
                    expr = ' '.join(expr.split()[2:-1]) + ' ' + str(res)
            elif expr.split()[1] == '*':
                try:
                    res = float(expr.split()[-1]) / float(expr.split()[0])
                    expr = ' '.join(expr.split()[2:-1]) + ' ' + str(res)
                except ZeroDivisionError:
                    return "X = 0"
            i = expr.find('=')
            if expr[i-2] == ')':
                expr = expr[1:i-2] + expr[i-1:]
            print expr + '\n'

    return expr
    
def init_connection():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

def parse_data():
    data = s.recv(2048).split('\n')[0]
    print data
    if len(data) > 100:
	data = expression(data)
    if data[:3] != 'X =':
        data = data.split()
        print data
        if data[0] == 'X':
            if data[1] == '*':
                res = float(data[4]) / float(data[2])
            elif data[1] == '+':
                res = float(data[4]) - float(data[2])
            elif data[1] == '-':
                res = float(data[4]) + float(data[2])
        else:
            if data[1] == '*':
                res = float(data[4]) / float(data[0])
            if data[1] == '+':
                res = float(data[4]) - float(data[0])
            if data[1] == '-':
                res = float(data[0]) - float(data[4])
    else:
        res = float(data.split()[-1])
    s.send(str(res) + "\n")
    print res
    print s.recv(len(GOOD))

def recv_banner():
    banner = s.recv(1024)
    print banner

init_connection()
recv_banner()
while True:
    parse_data()
