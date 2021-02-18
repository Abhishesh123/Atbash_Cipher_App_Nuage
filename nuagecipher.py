import string
import threading
import sys
import time

num = string.digits
punct = string.punctuation

Cipher_data = {

		'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'

      } 

def EncrypFunct(message):
	print(message)
	output = ''
	for i in message:
		if (i != ' ' and i not in punct and i not in num):
			output += Cipher_data[i.upper()]
		elif (i in punct):
			output += i
		elif (i in num):
			output += i
		else:
			output += ' '
	return output

read_data = ''

def FileOpenRead():
	global read_data
	with open("input_data.txt", "r") as f:
		read_data = EncrypFunct(f.read().rstrip("\n"))

t1 = threading.Thread(target = FileOpenRead())
t2 = threading.Thread(target = EncrypFunct, args=(Cipher_data,) ,daemon=True)
t1.start()
t2.start()
t1.join()
t2.join()	
try:
	output = read_data[0].upper() + read_data[1:]
	encrypted_data = []
	for i in output.split(' '):
		if (i.startswith('w')):
			encrypted_data.append(i[0].upper() + i[1:])
		elif not (i.startswith('w')):
			encrypted_data.append(i)
			with open("output_data.txt", "w") as f:
				f.write(' '.join(encrypted_data))
except:
  print("Exception:Index out of range")
