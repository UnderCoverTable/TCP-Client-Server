from socket import *

serverName = '192.168.100.53'# 'servername'
serverPort = 1200 # Port number

while(1):

	clientSocket = socket(AF_INET, SOCK_STREAM) # For TCP
	clientSocket.connect((serverName, serverPort)) # ClientSocket it used to communicate with server
	#print(clientSocket.getsockname())

	sentValue = input('\nEnter a number to be converted by server (-1 to quit): ') 
	clientSocket.send(sentValue.encode()) # Client enters number and its sent to server

	if sentValue == "-1": # If it is -1, connection is terminated
		print("\nClient terminated conenction")
		break


	print(clientSocket.recv(1024).decode()) # Recieves list of conversion types from server
	replyConversionType = input("Enter type: ") 
	clientSocket.send(replyConversionType.encode()) # Client enters type of conversion and its sent to server

	convertedReply = clientSocket.recv(1024).decode() # Client recieves converted answer or error
	conversionType = clientSocket.recv(1024).decode() # Type of conversion is also returned

	if convertedReply[0] == 'I': # I, indicates that an error msg was returned instead of a value, so error is displayed instead
		print(f"\n{conversionType} failed --> {convertedReply}")

	else:
		print(f"\n({conversionType}) -/- {sentValue} --> {convertedReply}") # Otherwise, the converted value is printed

	# Loop restarts and client can keep sending values until they want
	clientSocket.close()
