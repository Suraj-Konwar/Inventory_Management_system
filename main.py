#all imports
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Dublin City Medical Center")
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.product=StringVar()
        self.noofitems=StringVar()
        self.lot=StringVar()
        self.issusdate=StringVar()
        self.expdate=StringVar()
        self.address=StringVar()
        self.fill1=StringVar()
        self.fill2=StringVar()
        self.fill3=StringVar()
        self.fill4=StringVar()
        self.fill5=StringVar()
        self.fill6=StringVar()
        self.fill7=StringVar()
        self.fill8=StringVar()
        self.fill9=StringVar()
        self.fill10=StringVar()
        lbltitle = Label(self.root, bd=10,relief=RIDGE,text="INVENTORY MANAGEMENT SYSTEM",fg="#5755FE",bg="white",font=("times new roman",20,"bold"))
        lbltitle.pack(side=TOP,fill=X)

#=================data frame=======================================
        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=54,width=1280,height=370)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Product Information")
        DataframeLeft.place(x=0,y=1,width=770,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Invoice")
        DataframeRight.place(x=770,y=1,width=488,height=350)
#=================Button frame=======================================
        Buttonframe=Frame(self.root,bd=7,relief=RIDGE)
        Buttonframe.place(x=0,y=425,width=1280,height=60)
#=================Details frame=======================================
        Detailsframe=Frame(self.root,bd=7,relief=RIDGE)
        Detailsframe.place(x=0,y=485,width=1280,height=170)
#=======================Data Frame Left======================================
        lblNameTablet=Label(DataframeLeft,text="Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        lblRefNo=Label(DataframeLeft, text="Reference No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRefNo.grid(row=1,column=0,sticky=W)

        lblDose=Label(DataframeLeft,text="Product:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)

        lblNooftablets=Label(DataframeLeft,text="No of Items:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)

        lblLot=Label(DataframeLeft,text="Lot:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)

        lblissueDate=Label(DataframeLeft,text="Issue Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)

        lblExpDate=Label(DataframeLeft,text="Exp Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)

        lblDailyDose=Label(DataframeLeft,text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill1:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=8,column=0,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill2:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=0,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill3:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=1,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill4:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=2,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill5:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=3,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill6:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=4,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill7:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=5,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill8:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=6,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill9:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=7,column=2,sticky=W)

        lblSideeffect=Label(DataframeLeft,text="Fill10:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=8,column=2,sticky=W)

#=======================Data Entry Left======================================
        comNametablet=ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("Nice","Corona vacacine",)
        comNametablet.grid(row=0,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.ref, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=1,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.product, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=2,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.noofitems, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=3,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.lot,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=4,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.issusdate,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=5,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.expdate,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=6,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.address,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=7,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill1,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=8,column=1)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill2, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=0,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill3, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=1,column=3)

        comNametablet=Entry(DataframeLeft,textvariable=self.fill4, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=2,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill5,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=3,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill6,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=4,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill7,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=5,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill8,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=6,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill9, font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=7,column=3)

        comNametablet=Entry(DataframeLeft, textvariable=self.fill10,font=("times new roman",12,"bold"),width=30)
        comNametablet.grid(row=8,column=3)


#==================Data Frame Right=============================
        self.txtPrescription=Text(DataframeRight,font=("arial",11,),width=56,height=18)
        self.txtPrescription.grid(row=0,column=0)
#==================Buttons======================================
        btnPrint=Button(Buttonframe,command=self.iPrectioption, text="Print",bg="#9BCF53",fg="white",font=("arial",10,"bold"),width="25", height="2")
        btnPrint.grid(row=0,column=0)

        btnSaveData=Button(Buttonframe,command=self.iPrescriptionData, text="Save Data",bg="green",fg="white",font=("arial",10,"bold"),width="25", height="2")
        btnSaveData.grid(row=0,column=1)

        btnPrescriptionUpdate=Button(Buttonframe, text="Update",bg="#496989",fg="white",font=("arial",10,"bold"),width="25", height="2")
        btnPrescriptionUpdate.grid(row=0,column=2)

        btnPrescriptionDelete=Button(Buttonframe, command=self.idelete, text="Delete",bg="#22092C",fg="white",font=("arial",10,"bold"),width="25", height="2")
        btnPrescriptionDelete.grid(row=0,column=3)

        btnPrescriptionClear=Button(Buttonframe, command=self.iclear,text="Clear",bg="#F2BE22",fg="white",font=("arial",10,"bold"),width="25", height="2")
        btnPrescriptionClear.grid(row=0,column=4)

        btnPrescriptionExit=Button(Buttonframe, command=self.iexit,text="Exit",bg="#E72929",fg="white",font=("arial",10,"bold"),width="26", height="2")
        btnPrescriptionExit.grid(row=0,column=5)

#=================Table=========================================
#===============Scroll Y Bar=====================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","Lot","Issusdate","expdate","dailydose","sideeffect","futureinfo","bloodpressure","storageadvice","med","patientid","nhsno","patientnam","dob","patientaddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
#Storage Advice, Medication, Patient Id, NHS Number, Patient Name, Date of Birth, Patient Address
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name")
        self.hospital_table.heading("ref",text="Ref No")
        self.hospital_table.heading("dose",text="Product")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("Issusdate",text="Issus Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("futureinfo",text="Future Info")
        self.hospital_table.heading("bloodpressure",text="B.P")
        self.hospital_table.heading("storageadvice",text="Storage advice")
        self.hospital_table.heading("med",text="Med")
        self.hospital_table.heading("patientid",text="PatientID")
        self.hospital_table.heading("nhsno",text="NHS No")
        self.hospital_table.heading("patientnam",text="Fill8")
        self.hospital_table.heading("dob",text="Fill9")
        self.hospital_table.heading("patientaddress",text="Fill10")
       

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
 #       self.fatch_data()

        self.hospital_table.column("nameoftable",width=60)
        self.hospital_table.column("ref",width=70)
        self.hospital_table.column("dose",width=70)
        self.hospital_table.column("nooftablets",width=70)
        self.hospital_table.column("Lot",width=70)
        self.hospital_table.column("Issusdate",width=70)
        self.hospital_table.column("expdate",width=70)
        self.hospital_table.column("dailydose",width=70)
        self.hospital_table.column("sideeffect",width=70)
        self.hospital_table.column("futureinfo",width=70)
        self.hospital_table.column("bloodpressure",width=70)
        self.hospital_table.column("storageadvice",width=70)
        self.hospital_table.column("med",width=70)
        self.hospital_table.column("patientid",width=70)
        self.hospital_table.column("nhsno",width=70)
        self.hospital_table.column("patientnam",width=70)
        self.hospital_table.column("dob",width=70)
        self.hospital_table.column("patientaddress",width=60)


#===================Functionality Declration===============================

    def  iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Suraj@123",database="Surajdb")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(self.Nameoftablets.get(),
                                                                                                   self.ref.get(),
                                                                                                   self.product.get(),
                                                                                                   self.noofitems.get(),
                                                                                                   self.lot.get(),
                                                                                                   self.issusdate.get(),
                                                                                                   self.expdate.get(),
                                                                                                   self.address.get(),
                                                                                                   self.fill1.get(),
                                                                                                   self.fill2.get(),
                                                                                                   self.fill3.get(),
                                                                                                   self.fill4.get(),
                                                                                                   self.fill5.get(),
                                                                                                   self.fill6.get(),
                                                                                                   self.fill7.get(),
                                                                                                   self.fill8.get(),
                                                                                                   self.fill8.get(),
                                                                                                   self.fill9.get(),
                                                                                                   self.fill10.get()))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
#   def update(self):
            conn=mysql.connector
#   def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Suraj@123",database="Surajdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.product.set(row[2])
        self.noofitems.set(row[3])
        self.lot.set(row[4])
        self.issusdate.set(row[5])
        self.expdate.set(row[6])
        self.address.set(row[7])
        self.fill1.set(row[8])
        self.fill2.set(row[9])
        self.fill3.set(row[10])
        self.fill4.set(row[11])
        self.fill5.set(row[12])
        self.fill6.set(row[13])
        self.fill7.set(row[14])
        self.fill8.set(row[15]) 
        self.fill9.set(row[16])
        self.fill10.set(row[17])
    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Referance No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Product:\t\t\t"+self.product.get()+"\n")
        self.txtPrescription.insert(END,"No of Item:\t\t\t"+self.noofitems.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.lot.get()+"\n")
        self.txtPrescription.insert(END,"Issuse Date:\t\t\t"+self.issusdate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.expdate.get()+"\n")
        self.txtPrescription.insert(END,"Address:\t\t\t"+self.address.get()+"\n")
        self.txtPrescription.insert(END,"Fill1:\t\t\t"+self.fill1.get()+"\n")
        self.txtPrescription.insert(END,"Fill2:\t\t\t"+self.fill2.get()+"\n")
        self.txtPrescription.insert(END,"Fill3:\t\t\t"+self.fill3.get()+"\n")
        self.txtPrescription.insert(END,"Fill4:\t\t\t"+self.fill4.get()+"\n")
        self.txtPrescription.insert(END,"Fill5:\t\t\t"+self.fill5.get()+"\n")
        self.txtPrescription.insert(END,"Fill6:\t\t\t"+self.fill6.get()+"\n")
        self.txtPrescription.insert(END,"Fill7:\t\t\t"+self.fill7.get()+"\n")
        self.txtPrescription.insert(END,"Fill8:\t\t\t"+self.fill8.get()+"\n")
        self.txtPrescription.insert(END,"Fill9:\t\t\t"+self.fill9.get()+"\n")
        self.txtPrescription.insert(END,"Fill10:\t\t\t"+self.fill10.get()+"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Suraj@123",database="Surajdb")
        my_cursor=conn.cursor()
        query="delete from hospital where Referance_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
    def iclear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.product.set("")
        self.noofitems.set("")
        self.lot.set("")
        self.issusdate.set("")
        self.expdate.set("")
        self.address.set("")
        self.fill1.set("")
        self.fill2.set("")
        self.fill3.set("")
        self.fill4.set("")
        self.fill5.set("")
        self.fill6.set("")
        self.fill7.set("")
        self.fill8.set("")
        self.fill9.set("")
        self.fill10.set("")
        self.txtPrescription.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("Inventory Management system","Confirm you want to exit")
        if iexit>0:
            root.destroy()
            return

    



root=Tk()
ob=Hospital(root)
root.mainloop()
