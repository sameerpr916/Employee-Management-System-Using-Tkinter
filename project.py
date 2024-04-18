from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox



class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x820+0+0")
        self.root.title('Employee Management System')
        
        
        #variables

        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()


        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='red',bg='white')
        lbl_title.place(x=0,y=0,width=1450,height=50)

        #logo
        img_logo=Image.open('pic1.png')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=220,y=0,width=50,height=50)

        #image frame    
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1450,height=160)

        # FIRST
        img1=Image.open('pic2.png')
        img1=img1.resize((540,160))
        self.photo_1=ImageTk.PhotoImage(img1)
        
        self.img1=Label(img_frame,image=self.photo_1)
        self.img1.place(x=0,y=0,width=540,height=160)
        
         # second
        img2=Image.open('pic3.png')
        img2=img1.resize((540,160))
        self.photo_2=ImageTk.PhotoImage(img2)
        
        self.img2=Label(img_frame,image=self.photo_2)
        self.img2.place(x=540,y=0,width=540,height=160)


        #   third
        img3=Image.open('pic2.png')
        img3=img3.resize((540,160))
        self.photo_3=ImageTk.PhotoImage(img3)
        
        self.img3=Label(img_frame,image=self.photo_3)
        self.img3.place(x=1000,y=0,width=540,height=160)


        #Main frame    
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='blue')
        Main_frame.place(x=10,y=190,width=1450,height=560)

        #upper frame

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='yellow',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1450,height=270) 

        #labels and entries

        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='yellow')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10, sticky=W)

        #name
        lbl_name=Label(upper_frame,text='Name:',font=('arial',11,'bold'),bg='yellow')
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial',12,'bold'),width=19)
        txt_name.grid(row=0,column=3,padx=2,pady=7)

         #Designition
        lbl_Designition=Label(upper_frame,text='Designition:',font=('arial',11,'bold'),bg='yellow')
        lbl_Designition.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designation,font=('arial',12,'bold'),width=19)
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)

         #Email
        lbl_Email=Label(upper_frame,text='Email:',font=('arial',11,'bold'),bg='yellow')
        lbl_Email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_email,font=('arial',12,'bold'),width=19)
        txt_Email.grid(row=1,column=3,padx=2,pady=7)

         #Address
        lbl_Address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='yellow')
        lbl_Address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,font=('arial',12,'bold'),width=19)
        txt_Address.grid(row=2,column=1,padx=2,pady=7)

        #Married_Status

        lbl_Married_Status=Label(upper_frame,text='Married_Status:',font=('arial',11,'bold'),bg='yellow')
        lbl_Married_Status.grid(row=2,column=2,padx=2,sticky=W)

        combo_Married_Status=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',12,'bold'),width=17,state='readonly')
        combo_Married_Status['value']=('Married','UnMarried')
        combo_Married_Status.current(0)
        combo_Married_Status.grid(row=2,column=3,padx=2,pady=10, sticky=W)

         #Dob
        lbl_Dob=Label(upper_frame,text='D.O.Birth:',font=('arial',11,'bold'),bg='yellow')
        lbl_Dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_Dob=ttk.Entry(upper_frame,textvariable=self.var_dob,font=('arial',12,'bold'),width=19)
        txt_Dob.grid(row=3,column=1,padx=2,pady=7)
         
         
         #Doj
        lbl_Doj=Label(upper_frame,text='D.O.Joining:',font=('arial',11,'bold'),bg='yellow')
        lbl_Doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_Doj=ttk.Entry(upper_frame,textvariable=self.var_doj,font=('arial',12,'bold'),width=19)
        txt_Doj.grid(row=3,column=3,padx=2,pady=7)


        #Id_Proof

        # lbl_Id_Proof=Label(upper_frame,text='Id_Proof:',font=('arial',11,'bold'),bg='white',width=19,state=READABLE)
        # lbl_Id_Proof.grid(row=2,column=2,padx=2,sticky=W)

        combo_Id_Proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',12,'bold'),width=17,state='readonly')
        combo_Id_Proof['value']=("Select ID Proof","PAN CARD","AADHAR CARD","DRIVING LICENSE")
        combo_Id_Proof.current(0)
        combo_Id_Proof.grid(row=4,column=0,padx=2,pady=7, sticky=W)

        txt_Id_Proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,font=('arial',12,'bold'),width=19)
        txt_Id_Proof.grid(row=4,column=1,padx=2,pady=7)


        #gender

        lbl_Gender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='yellow')
        lbl_Gender.grid(row=4,column=2,padx=2,sticky=W)
        combo_Gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_Gender['value']=("Male","Female","Other")
        combo_Gender.current(0)
        combo_Gender.grid(row=4,column=3,padx=2,pady=7, sticky=W)

        # txt_Gender=ttk.Entry(upper_frame,font=('arial',12,'bold'),width=19)
        # txt_Gender.grid(row=4,column=1,padx=2,pady=7)

        #phone

        lbl_Phone=Label(upper_frame,text='Phone:',font=('arial',11,'bold'),bg='yellow')
        lbl_Phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_Phone=ttk.Entry(upper_frame,textvariable=self.var_phone,font=('arial',12,'bold'),width=19)
        txt_Phone.grid(row=0,column=5,padx=2,pady=7)

        #country

        lbl_Country=Label(upper_frame,text='Country:',font=('arial',11,'bold'),bg='yellow')
        lbl_Country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_Country=ttk.Entry(upper_frame,textvariable=self.var_country,font=('arial',12,'bold'),width=19)
        txt_Country.grid(row=1,column=5,padx=2,pady=7)


        #ctc

        lbl_CTC=Label(upper_frame,text='Salary(CTC):',font=('arial',11,'bold'),bg='yellow')
        lbl_CTC.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_salary,font=('arial',12,'bold'),width=19)
        txt_CTC.grid(row=2,column=5,padx=2,pady=7)

         #Button_Frame    
        Button_Frame=Frame(upper_frame,bd=0.5,relief=RIDGE,bg='yellow')
        Button_Frame.place(x=1155,y=19,width=170,height=210)

        btn_add=Button(Button_Frame,text="Save",command=self.add_data,font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_delete=Button(Button_Frame,text="Delete",command=self.delete_data,font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_delete.grid(row=1,column=0,padx=1,pady=5)

        btn_Update=Button(Button_Frame,text="Update",command=self.update_data,font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_Update.grid(row=2,column=0,padx=1,pady=5)

        btn_Clear=Button(Button_Frame,text="Clear",command=self.reset_data,font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_Clear.grid(row=3,column=0,padx=1,pady=5)

        #mask image

        # img4=Image.open('pic3.png')
        # img4=img4.resize((540,160))
        # self.mask_pic=ImageTk.PhotoImage(img4)
        
        # self.img4=Label(upper_frame,image=self.mask_pic)
        # self.img4.place(x=950,y=10,width=200,height=200)

        img5=Image.open('te.jpeg')
        img5=img5.resize((540,160))
        self.photo_5=ImageTk.PhotoImage(img5)
        
        self.img5=Label(upper_frame,image=self.photo_5,bg='yellow')
        self.img5.place(x=950,y=0,width=200,height=250)


        


        #down frame

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        #Search_frame    
        Search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        Search_frame.place(x=0,y=0,width=1470,height=60)

        Search_by=Label(Search_frame,text='Search_by:',font=('arial',11,'bold'),bg='red',fg="white")
        Search_by.grid(row=0,column=0,padx=5,sticky=W)

        #search
        self.var_com_search=StringVar()
        com_search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=17,state='readonly')
        com_search['value']=("Select Option","Phone","id_proof")
        com_search.current(0)
        com_search.grid(row=0,column=1,padx=5, sticky=W)

        self.var_search=StringVar()

        txt_search=ttk.Entry(Search_frame,textvariable=self.var_search,font=('arial',11,'bold'),width=19)
        txt_search.grid(row=0,column=2,padx=5)

       

        btn_Search=Button(Search_frame,command=self.search_data,text="Search",font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_Search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_frame,text="ShowAll",command=self.fetch_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        stayhome=Label(Search_frame,text="Manage The Data With Ease!",font=("times new roman",25,"bold"),fg="red")
        stayhome.place(x=780,y=0,width=600,height=35)

        #mask image

        mask=Image.open('pic3.png')
        mask=mask.resize((50,50))
        self.mask_pic=ImageTk.PhotoImage(mask)
        
        self.mask=Label(Search_frame,image=self.mask_pic)
        self.mask.place(x=800,y=0,width=50,height=30)

        #========================emp table====================

         #Table frame    
        Table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(Table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)
        
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

        #*************************functions***********************

    def add_data(self):
            if self.var_dep.get()=="" or self.var_email.get()=="":
                messagebox.showerror('Error','All Fields Are Required')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost', username='root',password='admin@123',database='mydata')
                    mycursor=conn.cursor()
                    mycursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_designation.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_idproofcomb.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get()
                                                                                                                                     ))    

                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Success','Employee has been added',parent=self.root)
                except Exception as es:
                    messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)   

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='admin@123',database='mydata')
        mycursor=conn.cursor()
        mycursor.execute('select * from employee1')
        data=mycursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
#get cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
                messagebox.showerror('Error','All Fields Are Required')
        else:
                try:
                    update=messagebox.askyesno('Update','Are You Sure This Employee Data')
                    if update>0:
                       conn=mysql.connector.connect(host='localhost', username='root',password='admin@123',database='mydata')
                       mycursor=conn.cursor()
                       mycursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s ',(
                            
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                        self.var_designation.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_married.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                                        self.var_idproof.get()
                                                                                                                                                                                                                                    ))

                    else:
                         if not update:
                              return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success','Employee Successfully Updated',parent=self.root)
                except Exception as es:    
                     messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)      

    def delete_data(self):
        if self.var_idproof.get()=="":
              messagebox.showerror('Error','All Fields Are Required')
        else:
             try:
                  Delete=messagebox.askyesno('Delete','Are You Sure To Delete This Employee')
                  if Delete>0:
                       conn=mysql.connector.connect(host='localhost', username='root',password='admin@123',database='mydata')
                       mycursor=conn.cursor()
                       sql='delete from employee1 where id_proof=%s'
                       value=(self.var_idproof.get(),)
                       mycursor.execute(sql,value)
                  else:
                       if not Delete:
                            return
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
             except Exception as es:    
                     messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)             
                       
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #searchdata
    def search_data(self):
         if self.var_com_search.get()=='' or self.var_search.get()=='':
              messagebox.showerror('Error','Please Select Option')
         else:
              try:
                   conn=mysql.connector.connect(host='localhost', username='root',password='admin@123',database='mydata')
                   mycursor=conn.cursor()
                   mycursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                   rows=mycursor.fetchall()
                   if len(rows)!=0:
                        self.employee_table.delete(*self.employee_table.get_children())
                        for i in rows:
                             self.employee_table.insert("",END,values=i)
                   conn.commit() 
                   conn.close() 
              except Exception as es:  
                   messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)            
             
                        

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()