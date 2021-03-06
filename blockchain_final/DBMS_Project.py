''' IMPORTING NECCESARY PACKAGES'''

from tkinter import *
from tkinter import ttk
import Login_Authentication
import datetime
import time
import tkinter.messagebox
import sqlite3
import chainTest_mix
import chainTest_comp
import excelToBlock
import DBdata
import tkinter

''' IMPORTING SUCCESSFUL'''

''' CREATING CLASS'''

# Scroll bar Class

class Scrollbar:
 def __init__(self,text):
  self.frame = text.master
  self.text = text
  self.text.configure(wrap='none')
  self.for_x_view()
  self.for_y_view()

 def for_x_view(self):
  # scroll Bar x For width
  scroll_x=tkinter.Scrollbar(self.frame, orient='horizontal',command=self.text.xview)
  scroll_x.config(command=self.text.xview)
  self.text.configure(xscrollcommand=scroll_x.set)
  scroll_x.pack(side='bottom', fill='x', anchor='w')
  return

 def for_y_view(self):
  # Scroll Bar y For Height
  scroll_y = tkinter.Scrollbar(self.frame)
  scroll_y.config(command=self.text.yview)
  self.text.configure(yscrollcommand=scroll_y.set)
  scroll_y.pack(side='right', fill='y')  
  return

# Blockchain System

class Blockchain_Portal:
    user = '1'
    passw = '1'
    db_name = 'comp.db'
    db_mix = 'mix.db'
    
    # Bloch Chain
    s_mix = chainTest_mix.Blockchain_mix()
    s_comp = chainTest_comp.Blockchain_comp()

    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x1000+600+200')
        self.root.resizable(True, True)
        self.root.title('Blockchain Data')

        # Excel data to Block Chain
        excelToBlock.excelToBlock(self.s_mix, self.s_comp)
        
        # Block Chain to DB file
        DBdata.makeDB(self.s_mix, self.s_comp)

        # Logo and Title
      
        self.label4 = Label(text='')
        self.label4.grid(row=0, column=0, sticky=E)
        
        self.photo = PhotoImage(file='icon.png')
        self.label = Label(image=self.photo)
        self.label.grid(row=1, column=0)
        
        self.label5 = Label(text='')
        self.label5.grid(row=2, column=0, sticky=E)

        self.label1 = Label(font=('arial', 23, 'bold'), text='Blockchain Management System', fg='dark blue')
        self.label1.grid(row=7, column=0)

        # Time and Date

        def tick():
            d = datetime.datetime.now()
            today = '{:%B %d, %Y}'.format(d)

            mytime = time.strftime('%I :%M :%S %p')
            self.lblInfo.config(text=(mytime + '     ' + today))
            self.lblInfo.after(200, tick)
            
        frame = LabelFrame(self.root, text ='Time and Date',font=('arial', 11, 'bold'), fg='dark blue',
                           padx=10, pady=10)
        frame.grid(row=7, column=1, sticky=W)
        
        self.lblInfo = Label(frame, font=('arial', 14), fg='black')
        self.lblInfo.grid(row=7, column=1, columnspan=2)
        tick()
        
        # Label: Search the Block
        
        frame = LabelFrame(self.root, text ='Searching The Block',font=('arial', 11, 'bold'), fg='dark blue',
                           padx=10, pady=10)
        frame.grid(row=1, column=1, sticky=W)

        Label(frame, text='Block Index: ').grid(row=2, column=1, sticky=EW)
        self.searchIndex = Entry(frame)
        self.searchIndex.grid(row=2, column=2, sticky=EW)

        # Search Button
        
        ttk.Button(frame, text = 'Search the Block',command=self.search).grid(row=7, column=2, sticky=NSEW)

        # Data Manipulation Button

        ttk.Button(frame, text = 'Manipulate Product', command = self.fakeComp).grid(row=8, column=2)
        ttk.Button(frame, text = 'Manipulate Mixture', command = self.fakeMix).grid(row=9, column=2)
 
        # Message Display
        
        self.message = Label(text='', fg='Red')
        self.message.grid(row=8, column=1)

        # Label: Complete Product Display Message
        
        self.label2 = Label(text='')
        self.label2.grid(row=9, column=0, sticky=E)
        
        self.label3 = Label(font=('arial', 14, 'bold'), text='Complete Product',
                            fg='dark Red', relief='ridge',padx=10,pady=10)
        self.label3.grid(row=10, column=0, columnspan=2, ipadx= 189, ipady=1)
        
        self.label2 = Label(text='')
        self.label2.grid(row=11, column=0, sticky=E)

        # Display 1: Complete Product Table display box (tree)
        
        self.tree = ttk.Treeview(height=4, column=['', '', '', '', '', '', '', '', ''
                                                    , '', '', '', '', '', '', '', ''
                                                   , '', '', '', ''])
        self.tree.grid(row=12, column=0, columnspan=2)
        self.tree.heading('#0', text='Index')
        self.tree.column('#0', width=50)
        self.tree.heading('#1', text='Company')
        self.tree.column('#1', width=100)
        self.tree.heading('#2', text='Date')
        self.tree.column('#2', width=100)
        self.tree.heading('#3', text='Time')
        self.tree.column('#3', width=90)
        self.tree.heading('#4', text='Amount')
        self.tree.column('#4', width=50)
        self.tree.heading('#5', text='Recipe')
        self.tree.column('#5', width=120)
        self.tree.heading('#6', text='Car')
        self.tree.column('#6', width=50)
        self.tree.heading('#7', text='Material1')
        self.tree.column('#7', width=70)
        self.tree.heading('#8', text='Ideal1')
        self.tree.column('#8', width=50)
        self.tree.heading('#9', text='Real1')
        self.tree.column('#9', width=50)
        self.tree.heading('#10', text='Material2')
        self.tree.column('#10', width=70)
        self.tree.heading('#11', text='Ideal2')
        self.tree.column('#11', width=50)
        self.tree.heading('#12', text='Real2')
        self.tree.column('#12', width=50)
        self.tree.heading('#13', text='Material3')
        self.tree.column('#13', width=70)
        self.tree.heading('#14', text='Ideal3')
        self.tree.column('#14', width=50)
        self.tree.heading('#15', text='Real3')
        self.tree.column('#15', width=50)
        self.tree.heading('#16', text='Material4')
        self.tree.column('#16', width=70)
        self.tree.heading('#17', text='Ideal4')
        self.tree.column('#17', width=50)
        self.tree.heading('#18', text='Real4')
        self.tree.column('#18', width=50)
        self.tree.heading('#19', text='Material5')
        self.tree.column('#19', width=70)
        self.tree.heading('#20', text='Ideal5')
        self.tree.column('#20', width=50)
        self.tree.heading('#21', text='Real5')
        self.tree.column('#21', width=50)

        # Label: Complete Product Display Message
        
        self.label2 = Label(text='')
        self.label2.grid(row=13, column=0, sticky=EW)
        
        self.label3 = Label(font=('arial', 14, 'bold'), text='Mixture Product',
                            fg='dark green', relief='ridge',padx=10,pady=10)
        self.label3.grid(row=14, column=0, columnspan=2, ipadx= 200, ipady=1)
        
        self.label2 = Label(text='')
        self.label2.grid(row=15, column=0, sticky=EW)
        
        # Display 2: Mixture Product Table display box       
        self.treeM = ttk.Treeview(height=4, column=['', '', '', '', ''])
        self.treeM.grid(row=16, column=0, rowspan=1, columnspan=1)
        self.treeM.heading('#0', text='Index')
        self.treeM.column('#0', width=150)
        self.treeM.heading('#1', text='Code')
        self.treeM.column('#1', width=150)
        self.treeM.heading('#2', text='Date')
        self.treeM.column('#2', width=150)
        self.treeM.heading('#3', text='Amount')
        self.treeM.column('#3', width=150)
        self.treeM.heading('#4', text='Traits A')
        self.treeM.column('#4', width=150)
        self.treeM.heading('#5', text='Traits B')
        self.treeM.column('#5', width=150)

        # Pass or Fail  
        self.passchk = ttk.Treeview(height=4, column=1)
        self.passchk.grid(row=16, column=1, columnspan=1)
        self.passchk.heading('#0', text='Index')
        self.passchk.column('#0', width=80)
        self.passchk.heading('#1', text='Pass')
        self.passchk.column('#1', width=80)


        ''' Menu Bar '''
        Chooser = Menu()
        itemone = Menu()

        #itemone.add_command(label='Add Record', command=self.add)
        #itemone.add_command(label='Edit Record', command=self.edit)
        #itemone.add_command(label='Delete Record', command=self.delet)
        itemone.add_separator()
        itemone.add_command(label='Exit', command=self.ex)

        #Chooser.add_cascade(label='File', menu=itemone)
        #Chooser.add_command(label='Add', command=self.add)
        #Chooser.add_command(label='Edit', command=self.edit)
        #Chooser.add_command(label='Delete', command=self.delet)
        Chooser.add_command(label='Exit', command=self.ex)

        root.config(menu=Chooser)
        self.veiwing_records()

    ''' View Database Table'''

    def run_query(self, query):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            return cursor.execute(query)

    ''' View ALL Records of Products (Default) '''
    
    def veiwing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        query = 'SELECT * FROM product'
        db_table = self.run_query(query)
        for data in db_table:
            self.tree.insert('', 1000, text=data[0], values=data[1:])

    ''' Search product and Show corresponding data '''
    
    def search_product(self, idx) :
        # clear the display of product
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Integrity check
        if self.integrityCheck(self.s_comp) :
            tkinter.messagebox.showinfo("Integrity Check", "Integrity verification failed. (comp)")
            return False
        
        # select and show corresponding data
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            db_table = cursor.execute('SELECT * FROM product WHERE "index"=?', (idx,))
            matList = []
            for data in db_table :
                self.tree.insert('', 'end', text=data[0], values=data[1:])
                # collect the mixture info
                try :
                    matList.append([int(data[7][3:]), float(data[8])])
                    matList.append([int(data[10][3:]), float(data[11])])
                    matList.append([int(data[13][3:]), float(data[14])])
                    matList.append([int(data[16][3:]), float(data[17])])
                    matList.append([int(data[19][3:]), float(data[20])])
                except TypeError : # out of range in column (None)
                    break
            if matList is None : # out of range (data in row)
                return 0
            else :
                return matList
        
    ''' Veiw ALL records of corresponding mixtures of the product '''
    
    def search_mat(self, matList) :
        # clear the display of mixture
        records = self.treeM.get_children()
        for element in records:
            self.treeM.delete(element)

        # clear the display of recipe checking
        records = self.passchk.get_children()
        for element in records:
            self.passchk.delete(element)

        # Integrity check
        if self.integrityCheck(self.s_mix) :
            tkinter.messagebox.showinfo("Integrity Check", "Integrity verification failed. (mix)")
            # clear product display
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            # clear mixture display
            records = self.treeM.get_children()
            for element in records:
                self.treeM.delete(element)
            # clear pass display
            records = self.passchk.get_children()
            for element in records:
                self.passchk.delete(element)
            return False
        
        # select and show corrresponding data
        with sqlite3.connect(self.db_mix) as conn:
            cursor = conn.cursor()
            for i in range(len(matList)) :
                db_table = cursor.execute('SELECT * FROM material WHERE "index"=?', (matList[i][0],))
                for data in db_table :
                    pf = self.err_ratio(data[1],matList[i][1],data[3])
                    if pf:
                        self.passchk.insert('', 'end', text = matList[i][0], values="Pass")
                    else :
                        self.passchk.insert('', 'end', text = matList[i][0], values="Fail")
                    self.treeM.insert('', 'end', text=data[0], values=data[1:])

    ''' Integrity Check '''
    
    def integrityCheck(self, chain) :
        check = chain.validate_chain()
        if check is True :
            return 0
        else :
            return 1
        
    # Error verifier

    def err_ratio(self,product,ideal,real):
        print(ideal, real)
        err_ratio = (real-ideal)/ideal*100
        print(err_ratio)

        if product == "OPC":
            if err_ratio >2 or err_ratio <-1:
                return 0
            else:
                return 1
            
        elif product == "SAND":
            if err_ratio >2 or err_ratio <-2:
                return 0
            else:
                return 1
            
        elif product == "GRAVEL":
            if err_ratio >2 or err_ratio <-2:
                return 0
            else:
                return 1
            
        elif product == "WATER":
            if err_ratio >1 or err_ratio <-2:
                return 0
            else:
                return 1
            
        elif product == "ADMIXTURE":
            if err_ratio >3 or err_ratio <-3:
                return 0
            else:
                return 1

    '''Function for using buttons'''

    def search(self):
        idx = int(self.searchIndex.get())
        matList = self.search_product(idx)
        if matList : # verified data
            self.search_mat(matList)
        elif matList is False : # product - interity check fail
            # clear product display
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            # clear mixture display
            records = self.treeM.get_children()
            for element in records:
                self.treeM.delete(element)
            # clear pass display
            records = self.passchk.get_children()
            for element in records:
                self.passchk.delete(element)
        else : # out of range (product)
            tkinter.messagebox.showinfo("FAIL TO SEARCH", "Wrong index! Try again.")
            self.veiwing_records()
            # clear mixture
            records = self.treeM.get_children()
            for element in records:
                self.treeM.delete(element)
            # clear pass
            records = self.passchk.get_children()
            for element in records:
                self.passchk.delete(element)

    '''EXIT'''
    
    def ex(self):
        exit = tkinter.messagebox.askquestion('Exit Application','Are you sure you want to close this application?')
        if exit == 'yes':
            # LOGOUT
            self.root.destroy()
            
            # LOGIN again
            newroot2 = tkinter.Tk()
            newroot2.iconbitmap("login.ico") #import an icon to app
            newroot2.geometry('425x185+600+400')
            application2 = Login_Authentication.Authentication(newroot2)
            newroot2.mainloop()


    ''' Data Manipulation '''
    
    def manipulation(self, bc) :
        idx = int(self.searchIndex.get()) # get index for manipulation
        tkinter.messagebox.showinfo("DATA MANIPULATION", "Data manipulated.")
        bc.chain[idx].transactions = {'code' : 1}

    def fakeComp(self) :
        self.manipulation(self.s_comp)

    def fakeMix(self) :
        self.manipulation(self.s_mix)
        
'''MAIN'''

if __name__ == '__main__':
    root = Tk()
    application = Blockchain_Portal(root)
    root.mainloop()
