'''Importing'''
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
import DBMS_Project
import tkinter

class Authentication:

    def __init__(self,root):

        self.root = root
        self.root.title('Blockchain Management System')
        self.root.resizable(True, True)
        self.cnt =1

        '''Make Window 10X10'''

        rows = 0
        while rows<10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows+=1

        '''Username and Password'''

        frame = LabelFrame(self.root, text='Login',font='Times 13', padx=10, pady=10,fg='Dark blue')
        frame.grid(row = 1, column = 2, columnspan=7,rowspan=8)

        Label(frame, text = ' Username ',font='Times 13').grid(row = 2, column = 1, sticky = NSEW)
        self.username = Entry(frame)
        self.username.grid(row = 2,column = 2, sticky = W)

        Label(frame, text = ' Password' ,font='Times 13').grid(row = 6, column = 1, sticky = NSEW)
        self.password = Entry(frame, show='*')
        self.password.grid(row = 6, column = 2, sticky = W)

        # Button

        ttk.Button(frame, text = 'LOGIN',command = self.login_user).grid(row=7,column=1)
        ttk.Button(frame, text = 'REGISTRATION',command = self.register_user).grid(row=7,column=2)

        '''Message Display'''
        self.message = Label(text = '',fg = 'Red')
        self.message.grid(row=9,column=6)

    def login_user(self):
        with open('users.txt', 'r') as usersFile:
            # Reads the content in the text file
            content = usersFile.readlines()
            for line in content:
                # Goes through each line in content
                # Removes '\n' from every line and splits the line up whenever there is a ','
                editedLines = line.strip('\n').split(',')
                temp_username = self.username.get()
                temp_password = self.password.get()
                    
                if temp_username == editedLines[0] and temp_password == editedLines[1]:
                    tkinter.messagebox.showinfo("LOGIN", "Your ID has been confirmed. Welcome.")
                    # Destroy current window
                    self.root.destroy()
                    # Open new window
                    newroot = Tk()
                    application = DBMS_Project.Blockchain_Portal(newroot)
                    newroot.mainloop()
                
            if self.cnt <5 :
                self.message['text'] = 'Login Failure {} times.'.format(self.cnt)+'\n'+'You have {} chances left.'.format(5-self.cnt)
                self.cnt += 1
        
            else:
                tkinter.messagebox.showinfo("Login Failure","The System will be closed for the security."+"\n"+"          Please Restart the system")
                self.root.destroy()
            
                usersFile.close()

    
    def register_user(self):
        global newroot2
        self.newroot2 = Tk()
        #newroot2 = Toplevel(root)
        self.newroot2.iconbitmap("login.ico")
        self.newroot2.title("Registration")
        self.newroot2.geometry("380x200")
        self.newroot2.resizable(True, True)

        # Make Register window 10 x 10
        
        rows = 0
        while rows<10:
            self.newroot2.rowconfigure(rows, weight=1)
            self.newroot2.columnconfigure(rows, weight=1)
            rows+=1
            
        # Design_Register
        
        frame2 = LabelFrame(self.newroot2, text='Registration',font='Times 13', padx=10, pady=10,fg='Dark blue')
        frame2.grid(row = 1, column = 1, columnspan=7,rowspan=8)

        Label(frame2, text = ' Username ',font='Times 13').grid(row = 2, column = 1, sticky = NSEW)
        self.username2 = Entry(frame2)
        self.username2.grid(row = 2,column = 2, sticky = W)

        Label(frame2, text = ' Password' ,font='Times 13').grid(row = 6, column = 1, sticky = NSEW)
        self.password2 = Entry(frame2, show='*')
        self.password2.grid(row = 6, column = 2, sticky = W)

        Label(frame2, text = ' Password Verification' ,font='Times 13').grid(row = 7, column = 1, sticky = NSEW)
        self.passwordver = Entry(frame2, show='*')
        self.passwordver.grid(row = 7, column = 2, sticky = W)
        
        self.message = Label(frame2, text = 'Please enter the details below.',fg = 'Blue')
        self.message.grid(row=1,column=2)
        

        # Button

        ttk.Button(frame2, text = 'REGISTER',command = self.register_ver_user).grid(row=8,column=2)
    
    def register_ver_user(self):
        if self.password2.get() == self.passwordver.get():
        
            temp = self.username2.get() +','+ self.password2.get() + '\n'

            with open('users.txt', 'a+t') as usersFile:
                usersFile.writelines(temp)
                usersFile.close()
                
            tkinter.messagebox.showinfo("Register", "Your ID has been registered.")
            self.newroot2.destroy()
        else:
            tkinter.messagebox.showinfo("Warning","The password you entered does not match the password verification." +'\n'+'                Please check your password agian.')
            
                     
if __name__ == '__main__':
        
    root = tkinter.Tk()
    root.iconbitmap("login.ico") #import an icon to app
    root.geometry('425x185+600+400')
    application = Authentication(root)

    root.mainloop()


