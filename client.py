"""
Client side operation, using Tkinter for the GUI
"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter 


def receiveMessage():
	while True:
		try:
			msg = client_socket.recv(BUFSIZ).decode("utf8")
			msgList.insert(tikinter.END, msg)
		except OSError:		#If the client leaves the chat
			break


def sendMessage(event = None):
	""" Event passed by Tkinter GUI"""
	msg = message.get()
	message.set("")
	client_socket.send(bytes(msg, "utf8"))
	if msg == "{QUIT}":
		client_socket.close()
		top.quit()


def closeWindow(event = None):
	""" Close the the GUI window"""
	message.set("{QUIT}")
	sendMessage()



top = tkinter.Tk()
top.title("Chatbot")


frame = tkinter.Frame(top)
message = tkinter.StringVar()
message.set("Type your message!")
scrollbar = tkinter.Scrollbar(frame)


msgList = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msgList.pack()

frame.pack()


#Create input field 
entry_field = tkinter.Entry(top, textvariable=message)
entry_field.bind("<Return>", sendMessage)
entry_field.pack(side=tkinter.LEFT, fill=tkinter.Y)
send_button = tkinter.Button(top, text="Send", command=sendMessage, width=8)
send_button.pack(side=tkinter.LEFT, fill=tkinter.X)

top.protocol("WM_DELETE_WINDOW", closeWindow)


HOST = "127.0.0.1"
PORT = 12346



BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


#begin the thread
receive_thread = Thread(target=receiveMessage)
receive_thread.start()
tkinter.mainloop()
