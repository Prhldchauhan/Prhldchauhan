from tkinter import *

import csv
key=["price","size","time"]
from datetime import datetime


class LOB(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.var = IntVar()
        self.create_widgets()
        self.history=[]
        self.tx=str("")
        self.i=0
        
        

    def create_widgets(self):
        #FOR CREATING THE ENTRY FOR A
        self.a=Entry(self)
        self.a.grid(row =1, column =0,sticky=W+E)
        
        #FOR CREATING THE ENTRY FOR B    
        self.b=Entry(self)
        self.b.grid(row =1, column =1,sticky=W+E)
        
        #FOR CREATING THE ENTRY FOR INPUT
        self.inp=Entry(self,width=44)
        self.inp.grid(row =2, column =0,columnspan=2,sticky=E)

        #FOR CREATING THE RADIO BUTTON R1
        self.r1=Radiobutton(self, text="BUY",variable = self.var,value=1,command=self.sel )
        self.r1.grid(row =1, column =2,sticky=W)
        

        #FOR CREATING THE RADIO BUTTON R2
        self.r2=Radiobutton(self, text="SELL",variable = self.var,value=2,command=self.sel)
        self.r2.grid(row =2, column =2,sticky=W)
       

        #FOR CREATING THE BUTTON FOR BACKSPACE
        self.cut=Button(self,text="<---",command=self.CUT,width=10
                        )
        self.cut.grid(row=4,column=1,sticky=W)

        #FOR CREATING THE LABLE FOR A
        self.a_=Label(self, text ="Number of Shares",font=('Helvetica', 12, 'bold'))
        self.a_.grid(row =0, column =0,sticky=W)
         
        #FOR CREATING THE LABLE FOR B
        self.b_=Label(self, text ="Limit Price:",font=('Helvetica', 12, 'bold'))
        self.b_.grid(row =0, column =1,sticky=W)

        #FOR CREATING THE LABLE FOR B
        self.b_=Label(self, text ="Buy or Sell:",font=('Helvetica', 12, 'bold'),)
        self.b_.grid(row =0, column =2,sticky=W)
        
        #FOR CREATING THE STATUS LABLE
        self.status_label =Label(self, height =20, width =60, bg ="black", fg ="#00FF00", text ="---", wraplength =250)
        self.status_label.grid(row =9, column =0, columnspan=3)

        #FOR CREATING THE ANSWER LABLE
        self.ANL1 =Label(self, text ="OPERATION PERFORMED:",)
        self.ANL1.grid(row =6, column =0,columnspan=2,sticky=W)
        
        
        #FOR CREATING THE ONSCREEN PANAEL LABLE
        self.OSP =Label(self, text ="ONSCREEN PANEL")
        self.OSP.grid(row =3, column =0,columnspan=2,sticky=W)
        #FOR CREATING THE INPUT  LABLE
        self.OSP =Label(self, text ="INPUT")
        self.OSP.grid(row =2, column =0,columnspan=2,sticky=W)

        
        #FOR CREATING THE BUTTON HISTORY
        self.h_=Button(self, text="HISTORY", command=self.H, width=11)
        self.h_.grid(row =5, column =0,sticky=E)

        #FOR CREATING THE BUTTON REMOVE
        self.remove_=Button(self, text="REMOVE", command=self.REMOVE, width=11)
        self.remove_.grid(row =4, column =0,sticky=E)
        

        #FOR CREATING THE BUTTON GRAPH
        self.g_=Button(self, text="GRAPH", command=self.G, width=8)
        self.g_.grid(row =4, column =1,sticky=E)

        #FOR CREATING THE BUTTON SHOW
        self.g_=Button(self, text="SHOW", command=self.SHOW, width=8)
        self.g_.grid(row =4, column =2,sticky=W)
        
        #FOR CREATING THE BUTTON ENTER
        self.e_=Button(self, text="MARKET ORDER", command=self.market_order, width=22,justify="center")
        self.e_.grid(row =5, column =1,columnspan=2)
        
        
        #FOR CREATING THE BUTTON RESET
        self.reset_=Button(self, text="RESET", command=self.RESET, width=11)
        self.reset_.grid(row=5,column=0,sticky=W)
        #FOR CREATING THE BUTTON ADD
        self.add_=Button(self, text="ADD", command=self.ADD, width=11)
        self.add_.grid(row=4,column=0,sticky=W)

        #FOR CREATING THE BUTTON QUIT
        self.b1= Button(self,text="QUIT",command=self.QUIT, width=10)
        self.b1.grid(row=5,column=1,sticky=W) 

    #FUNCTION SELECTION
    def sel(self):
       selection = "You selected the option " + str(self.var.get())
       self.status_label.configure(text = selection)
    #FUNCTION QUIT    
    def QUIT(self):
        #print("QUIT")
        try:
            self.h.destroy()
        except:
            pass
        finally:
            self.master.destroy()
    
    #FUNCTION SHOW
    def SHOW(self):
        self.history.append("*****DATA SEEN*****")
        t=''
        with open("bid.txt", 'r') as file:
            csv_file = csv.DictReader(file)
            data=[]
            for row in csv_file:
                data.append(list(row.values()))
            data.sort(reverse=True)
            t+="BID="+str(data)
        with open("ask.txt", 'r') as file:
            csv_file = csv.DictReader(file)
            data=[]
            for row in csv_file:
                data.append(list(row.values()))
            data.sort()
            t+="\n\n\nASK="+str(data)
        self.status_label.configure(text =t)

    #FUNCTION ADD
    def ADD(self):
        self.history.append("*****ORDER ADDED*****")
        opt=self.var.get()
        now = datetime.now()
        
        current_time = now.strftime("%H:%M:%S")
        inp=self.inp.get()+','+str(current_time)
        if opt==1:
            opt="buy"
        if opt==2:
            opt="sell"
        if opt=="buy":
            with open("bid.txt", 'r') as file:
                csv_file = csv.DictReader(file)
                data=[]
                for row in csv_file:
                    data.append(list(row.values()))
            data.append(inp.split(','))
            data.sort(reverse=True)
            data.insert(0,key)
            
            with open("bid.txt", 'w') as file:
                writer = csv.writer(file)
                for i in data:
                    writer.writerow(i)
            
            
        if opt=="sell":
            with open("ask.txt", 'r') as file:
                csv_file = csv.DictReader(file)
                data=[]
                for row in csv_file:
                    data.append(list(row.values()))
            data.append(inp.split(','))
            data.sort()
            data.insert(0,key)
            
            
            with open("ask.txt", 'w') as file:
                writer = csv.writer(file)
                for i in data:
                    writer.writerow(i)
        self.SHOW()

    #FUNCTION REMOVE
    def REMOVE(self):
        self.history.append("*****ORDER REMOVED*****")
        opt=self.var.get()
        inp=self.inp.get()
        if opt==1:
            opt="buy"
        if opt==2:
            opt="sell"
        if opt=="buy":
                
            a_file = open("bid.txt", "r")
        

            lines = a_file.readlines()
            a_file.close()

            new_file = open("bid.txt", "w")
            
            for line in lines:
                if inp not in line.strip("\n") :

                    new_file.write(line)

            new_file.close()
        if opt=="sell":
                
            a_file = open("ask.txt", "r")
        

            lines = a_file.readlines()
            a_file.close()

            new_file = open("ask.txt", "w")
            for line in lines:
                if inp not in line.strip("\n") :

                    new_file.write(line)

            new_file.close()
        self.SHOW()

    #FUNCTION
    def market_order(self):
        self.SHOW()
        opt=self.var.get()
        if opt==1:
            opt="buy"
        else:
            opt="sell"
        no_of_shares=self.a.get()
        
        
        if self.b.get()!='':
            t='1'
            limit=self.b.get()
        
        
            if opt=="sell":
                with open("bid.txt", 'r') as file:
                    csv_file = csv.DictReader(file)
                    data=[]
                    for row in csv_file:
                        data.append(list(row.values()))
                
                data.sort(reverse=True)
                for i in data:
                    if t=='1':
                        if float(i[0])>=float(limit):
                            if float(i[1])>float(no_of_shares):
                                i[1]=str(float(i[1])-float(no_of_shares))
                                no_of_shares=str(0)
                                break
                            else:
                                no_of_shares=str(float(no_of_shares)-float(i[1]))
                                i[1]=str(0)
                        else:
                            t=0
                if t==0:
                    self.status_label.configure(text ="NOT POSSIBLE")
                else:
                    data=[i for i in data if float(i[1])!=float('0')]           
                    data.insert(0,key)
                
                    with open("bid.txt", 'w') as file:
                        writer = csv.writer(file)
                        for i in data:
                            writer.writerow(i)
                
                
            if opt=="buy":
                with open("ask.txt", 'r') as file:
                    csv_file = csv.DictReader(file)
                    data=[]
                    for row in csv_file:
                        data.append(list(row.values()))
                
                data.sort()
                for i in data:
                    if t=='1':
                        if float(i[0])<=float(limit):
                            if float(i[1])>float(no_of_shares):
                                i[1]=str(float(i[1])-float(no_of_shares))
                                no_of_shares=str(0)
                                break
                            else:
                                no_of_shares=str(float(no_of_shares)-float(i[1]))
                                i[1]=str(0)
                        
                        else:
                            t=0
                if t==0:
                    self.status_label.configure(text ="NOT POSSIBLE")
                else:
                    data=[i for i in data if float(i[1])!=float('0')] 
                    data.insert(0,key)
                
                
                with open("ask.txt", 'w') as file:
                    writer = csv.writer(file)
                    for i in data:
                        writer.writerow(i)
        else:
            if opt=="sell":
                with open("bid.txt", 'r') as file:
                    csv_file = csv.DictReader(file)
                    data=[]
                    for row in csv_file:
                        data.append(list(row.values()))
                data.sort(reverse=True)
                for i in data:
            
                    if float(i[1])>=float(no_of_shares):
                        i[1]=str(float(i[1])-float(no_of_shares))
                        no_of_shares='0'
                        
                    else:
                        no_of_shares=str(float(no_of_shares)-float(i[1]))
                        i[1]='0'
                if no_of_shares!='0':
                    self.status_label.configure(text ="NOT POSSIBLE")
                else:    
                    data=[i for i in data if float(i[1])!=float('0')]           
                    data.insert(0,key)
                    
                    with open("bid.txt", 'w') as file:
                        writer = csv.writer(file)
                        for i in data:
                            writer.writerow(i)
                
                
            if opt=="buy":
                with open("ask.txt", 'r') as file:
                    csv_file = csv.DictReader(file)
                    data=[]
                    for row in csv_file:
                        data.append(list(row.values()))
                data.sort()
                for i in data:
                    if float(i[1])>=float(no_of_shares):
                        i[1]=str(float(i[1])-float(no_of_shares))
                        no_of_shares='0'
                        
                    else:
                        no_of_shares=str(float(no_of_shares)-float(i[1]))
                        i[1]='0'
                if no_of_shares!='0':
                    self.status_label.configure(text ="NOT POSSIBLE")
                else:   
                    data=[i for i in data if float(i[1])!=float('0')] 
                    data.insert(0,key)
                    
                    
                    with open("ask.txt", 'w') as file:
                        writer = csv.writer(file)
                        for i in data:
                            writer.writerow(i)
        
    #FUNCTION H
    def H(self):
        try:
            try:
                self.h.destroy()
            except:
                pass
            try:
                self.g.destroy()
            except:
                pass
        except:
            pass
        finally:
            self.h = Tk()
            self.h.title("HISTORY")
            self.h.geometry("300x700+400+200")
            self.h.l=Label(self.h,text="NO HISTORY",justify="left")
            self.h.l.grid(row=0,column=0)
            self.tx=str("")
            for i in self.history:
                self.tx+=i+"\n"
                self.h.l.configure(text=self.tx) 
            self.h.mainloop()
    
    def G(self):
        data1,data2=[],[]
        with open("bid.txt", 'r') as file:
            csv_file = csv.DictReader(file)
            
            for row in csv_file:
                data1.append(list(row.values()))
            data1.sort(reverse=True)
            
        with open("ask.txt", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                data2.append(list(row.values()))
            data2.sort(reverse=True)
            
        now = datetime.now()
        l=len(max(data2)[0])
        current_time = now.strftime("%H:%M:%S")
        t="Current   Time   is  "+str(current_time)
        
        try:
            try:
                self.h.destroy()
            except:
                pass
            try:
                self.g.destroy()
            except:
                pass
        except:
            pass
        finally:
            self.history.append("*****GRAPH SEEN*****")
            self.g = Tk()
            self.g.title("Graph")
            self.g.geometry("400x450")
            self.g.l=Label(self.g,text=t)
            self.g.l.grid(row=0,column=0,columnspan=3,sticky=W)
            self.g.l=Label(self.g,text=" "*5,justify="left")
            self.g.l.grid(row=1,column=0,sticky=W)
            self.g.l=Label(self.g,text="Price", justify="left")
            self.g.l.grid(row=1,column=1,sticky=W)
            self.g.l=Label(self.g,text="Ask Size", justify="left")
            self.g.l.grid(row=1,column=2,sticky=W)
            self.g.l=Label(self.g,text="-"*45,justify="left")
            self.g.l.grid(row=2,column=0,columnspan=3,sticky=W)
            for i in range(len(data2)):
                self.g.l=Label(self.g,text=" "*11,justify="left")
                self.g.l.grid(row=3+i,column=0,sticky=W)
                self.g.l=Label(self.g,text=str(data2[i][0]), justify="left")
                self.g.l.grid(row=3+i,column=1,sticky=W)
                self.g.l=Label(self.g,text=str(data2[i][1]), justify="left")
                self.g.l.grid(row=3+i,column=2,sticky=W)
            self.g.l=Label(self.g,text="-"*45,justify="left")
            self.g.l.grid(row=4+len(data2),column=0,columnspan=3,sticky=W)
            for i in range(len(data1)):
                self.g.l=Label(self.g,text=" "*11,justify="left")
                self.g.l.grid(row=5+len(data2)+i,column=2,sticky=W)
                self.g.l=Label(self.g,text=str(data1[i][1]), justify="left")
                self.g.l.grid(row=5+len(data2)+i,column=0,sticky=W)
                self.g.l=Label(self.g,text=str(data1[i][0]), justify="left")
                self.g.l.grid(row=5+len(data2)+i,column=1,sticky=W)
            self.g.l=Label(self.g,text="-"*45,justify="left")
            self.g.l.grid(row=6+len(data1)+len(data2),column=0,columnspan=3,sticky=W)
            self.g.l=Label(self.g,text=" "*11,justify="left")
            self.g.l.grid(row=7+len(data1)+len(data2),column=2,sticky=W)
            self.g.l=Label(self.g,text="Price", justify="left")
            self.g.l.grid(row=7+len(data1)+len(data2),column=1,sticky=W)
            self.g.l=Label(self.g,text="Bid Size", justify="left")
            self.g.l.grid(row=7+len(data1)+len(data2),column=0,sticky=W)
            self.g.l=Label(self.g,text="-"*45,justify="left")
            self.g.l.grid(row=8+len(data1)+len(data2),column=0,columnspan=3,sticky=W)
            self.g.mainloop()
        
            
        
    #FUNCTION RESET
    def RESET(self):
        #print("reset")
        self.history.append("*****VALUE RESET*****")
        self.r1.deselect()
        self.r2.deselect()
        self.a.delete(0,25)
        self.b.delete(0,25)
        
        self.inp.delete(0,30)
        self.ANS="------------"
        
        self.status_label.configure(text ="Successfully RESET done")

    #FUNCTION INSERT
    
    def CUT(self):
        try:
            r=self.focus_get()
            sd=len(str(r.get()))
            r.delete(sd-1)
        except:
            self.status_label.configure(text ="wrong operation")
 
cal = Tk()
cal.title("Limit_Order_Book")
cal.geometry("428x500")
app = LOB(cal)
app.mainloop()
