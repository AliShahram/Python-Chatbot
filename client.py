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
top.geometry("400x520")

filename = tkinter.PhotoImage(file = "/Users/shahram/Desktop/Programming/python_chatbot/network.png")
background_label = tkinter.Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(top)

message = tkinter.StringVar()
message.set("Type your message!")


scrollbar = tkinter.Scrollbar(frame, bg="#251f36")
msgList = tkinter.Listbox(frame, height=25, width=30, yscrollcommand=scrollbar.set, bg="#251f36", fg="white")

scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msgList.pack()

frame.pack(pady=20)


entry_field = tkinter.Entry(top, textvariable=message, bg="#251f36", fg="white")
entry_field.bind("<Return>", sendMessage)
send_button = tkinter.Button(top, text="Send", command=sendMessage, highlightbackground="#000000", width=8)
entry_field.pack(side=tkinter.LEFT, padx=(55,10))
entry_field.config(highlightbackground="black")
send_button.pack(side=tkinter.LEFT,fill=tkinter.X)







'''







#Create input field 

'''
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
