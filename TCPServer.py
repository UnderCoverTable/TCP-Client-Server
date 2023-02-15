from socket import *

serverPort = 1200 # Port Number
serverSocket = socket(AF_INET, SOCK_STREAM) # For TCP
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while 1:
	connectionSocket, addr = serverSocket.accept() # ConnectionSocket is used to send and receive from client


	recvievedValue = connectionSocket.recv(1024).decode() # Server recicves input value from Client
 
	if recvievedValue == "-1": # Connection terminated if its -1
		print("\nClient terminated conenction")
		break

	print(f"Recieved value from client: {recvievedValue}") # Input value is printed

	askForConversionType = "\n1 => Binary to Decimal \n2 => Decimal to Binary \n3 => Binary to Octal\n4 => Octal to Binary\n5 => Binary to Hex\n6 => Hex to Binary"
	connectionSocket.send(askForConversionType.encode()) # List of conversions is sent to client

	recvievedConversionType = connectionSocket.recv(1024).decode() # Recieves clients response to type of conversion
	print(f"Conversion type: {recvievedConversionType}") # Conversion number is printed

	def checkIfBinary(num): # Function to see if a number is binary
		num = [i for i in str(num)]
		for n in num:
			if n != "1" and n !="0":
				return "end"

	value = recvievedValue
	flag = 1 # Flag setup to track an errors
	
	if(recvievedConversionType == "1"): #Binary to Decimal
		type = "Binary to Decimal"

		if checkIfBinary(value) == "end":
			flag = 2
		
		if flag == 1:
			value = int(value)
			value = bin(value)[2:]
	

	elif(recvievedConversionType == "2"):#Decimal to Binary
		type =" Decimal to Binary"
		for i in value:
			if i == '.':
				flag = 3
		
		if flag == 1:
			value = int(value)
			value = bin(value).replace("0b","")

	elif(recvievedConversionType == "3"): #Binary to Octal
		type = "Binary to Octal"
		
		if checkIfBinary(value) == "end":
			flag = 2

		if flag == 1:
			value = int(value)
			value = oct(value)

	elif(recvievedConversionType == "4"): #Octal to Binary
		type = "Octal to Binary"

		if value[0] != '0' or (value[1] != 'o' and value[1] != 'O'):
			flag = 4

		if flag == 1:
			value = int(value[2:],8)
			value = bin(value)[2:]


	elif(recvievedConversionType == "5"):#Binary to Hex
		type = "Binary to Hex"
		

		if checkIfBinary(value) == "end":
			flag = 2

		if flag == 1:
			value = int(value)
			value = hex(value)

	elif(recvievedConversionType == "6"):#Hex to Binary
		type = "Hex to Binary"
		print(value[0],value[1])
		if value[0] != '0' or (value[1] != 'x' and value[1] != 'X'):
			flag = 5

		if flag == 1:
			value = int(value[2:],16)
			value = bin(value)[2:]

	
	if flag == 1: # Indicates that covnersion was successful and value is sent to client
		connectionSocket.send(str(value).encode())
		connectionSocket.send(type.encode())

	# Following flags indicate conversion failed and error msg is sent to client
	if flag == 2:
		connectionSocket.send("Input value is not Binary".encode())
		connectionSocket.send(type.encode())

	if flag == 3:
		connectionSocket.send("Input value is not Decimal".encode())
		connectionSocket.send(type.encode())

	if flag == 4:
		connectionSocket.send("Input value is not Octa".encode())
		connectionSocket.send(type.encode())

	if flag == 5:
		connectionSocket.send("Input value is not Hex".encode())
		connectionSocket.send(type.encode())

	# Loop repeats until client wants to
	connectionSocket.close()
