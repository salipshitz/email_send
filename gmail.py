from tkinter import *
from smtplib import *
class Window(Frame):
	def __init__(this, master=None):
		Super(Window, this).__init__()
		this.master = master
		this.pack(fill=BOTH, expand=1)
		try:
			this.server = SMTP_SSL('smtp.gmail.com', port=465)
			this.server.ehlo()
			assert this.server != None
			this.screen_login()
		except:
			Label(self, text="ERROR: Mail server failed to initialize").pack()
	
	def pw(this, width):
		return Entry(this, show="*", width=width)
	
	def en(this, width):
		return Entry(this, width=width)
	
	def screen_login(this):
		this.pass = this.pw(15)
		this.pass.place(relx=0.5, rely=0.75, anchor=CENTER)
		this.user = this.en(15)
		this.user.place(relx=0.5, rely=0.25, anchor=CENTER)
		btn = Button(self, text="Enter", command=self.login)
		btn.place(relx=0.5, rely = 1.0, anchor=S)
		
	def login(this):
		this.password = this.pass.get()
		this.fromAddr = this.user.get()
		
		try:
			this.server.login(fromAddr, password)
			this.screen_msg
		except:
			Label(this, text="Error: Login failed").pack()
	
	def screen_msg(this):
		for widget in this.winfo_children():
			widget.destroy()
		
		mes_label = Label(self, text="Enter your message. End lines with \\n")
		mes_label.pack()
		this.mes = this.en(100)
		this.mes.place(relx=0.5, rely=0.5, anchor=CENTER)
		btn = Button(self, text="Enter", command=this.msg_set)
		btn.place(relx=0.5, rely=1.0, anchor=S)
	
	def msg_set(this):
		this.msg = this.mes.get()
		this.screen_send()
		
	def screen_send(this):
		for widget in this.winfo_children:
			widget.destroy()
		
		this.to = this.en(15)
		this.to.place(relx=0.5, rely=0.5, anchor=CENTER)
		btn = Button(this, text="Send", command=this.email_send)
		btn.place(relx=0.5, rely=1.0, anchor=S)
	
	def email_send(this):
		for widget in this.winfo_children:
			widget.destroy
		
		this.toAddrs = this.to.get().split(", ")	
		try:
			this.server.sendmail(this.fromAddr, this.toAddrs, this.msg)
			Label(this, text="Email succesfully sent").pack()
		except:
			Label(this, text="Email failed to send").pack()
		finally:
			this.server.close()
			del this.server
			try:
				assert this.server == None
			except:
				Label(self, text="Mail server not succesfully deleted").pack()
