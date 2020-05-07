from tkinter import *
import math,random
from tkinter import messagebox

class billApp:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root,text="Billing Software",bd=12,relief= GROOVE,bg= bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #################### variables ########################

        ######### Customer ###############
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        ##########Cosmatics###############
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.body_spray=IntVar()

        ######################Grocery############
        self.rice=IntVar()
        self.food=IntVar()
        self.dal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.salt=IntVar()

        ###############Cold Drinks###############
        self.maza=IntVar()
        self.coke=IntVar()
        self.sprite=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.seven_up=IntVar()

        #####Total Product Price and Tax Variables#######
        self.cosmatic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_prince=StringVar()
        self.cosmatic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #################### Customer Details Frame ###############
        F1= LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Detals",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5)

        cphn_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5)

        bill_btn = Button(F1,text="search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=20,pady=20)

        ################### Cosmatic Frame ######################
        F2= LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=200,width=325,height=380)

        g1_lbl=Label(F2,text="Bath Soap",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g1_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F2,text="Hair Spray",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F2,text="Hair Gell",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Spray",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        body_txt=Entry(F2,width=10,textvariable=self.body_spray,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ################### Grocery Frame ######################
        F3= LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=200,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F3,width=10,textvariable=self.food,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Dal",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Salt",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6_txt=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ################### Cold Drink Frame ######################
        F4= LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=200,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Coke",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        c2_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        c3_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        c4_txt=Entry(F4,width=10,textvariable=self.thumbs_up,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Seven Up",font=("times new roman",15,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        c6_txt=Entry(F4,width=10,textvariable=self.seven_up,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ################### Bill Area ######################
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=200,width=330,height=380)

        bill_title=Label(F5,text="Bill Area",font="arial 15  bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea= Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        ################### Button Frame ######################
        F6= LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=582,relwidth=1,height=113)
        ## column 1 ##
        m1_lvl=Label(F6,text="Total Cosmatic Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmatic_price,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lvl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lvl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_prince,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        ## column 2 ##
        m1_lvl=Label(F6,text="Cosmatic Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmatic_tax,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        m2_lvl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        m3_lvl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("times new roman",9,"bold"),bd=3,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=3,relief=GROOVE)
        btn_F.place(x=720,width=580,height=78)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=12,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=0)
        generate_bill_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",bd=2,pady=12,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=0)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=12,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=0)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=12,width=10,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=0)
        self.welcome_blll()

    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fc_p=(self.face_wash.get()*120)
        self.c_fw_p=(self.face_cream.get()*60)
        self.c_hs_p=(self.body_spray.get()*60)
        self.c_hg_p=(self.gell.get()*60)
        self.c_bl_p=(self.spray.get()*160)

        self.total_cosmatic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
        )
        self.cosmatic_price.set(str(self.total_cosmatic_price))
        self.c_tax=round((self.total_cosmatic_price*.05),2)
        self.cosmatic_tax.set(str(self.c_tax))

        self.g_r_p=(self.rice.get()*80)
        self.g_f_p=(self.food.get()*120)
        self.g_d_p=(self.dal.get()*60)
        self.g_w_p=(self.wheat.get()*45)
        self.g_s_p=(self.sugar.get()*40)
        self.g_t_p=(self.salt.get()*45)

        self.total_grocery_price=float((
            self.g_r_p
            +self.g_f_p
            +self.g_d_p
            +self.g_w_p
            +self.g_s_p
            +self.g_t_p
        ))

        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*.07),2)
        self.grocery_tax.set(str(self.g_tax))

        self.d_m_p=(self.maza.get()*12)
        self.d_c_p=(self.coke.get()*12)
        self.d_f_p=(self.thumbs_up.get()*20)
        self.d_t_p=(self.sprite.get()*10)
        self.d_l_p=(self.seven_up.get()*25)
        self.d_s_p=(self.limca.get()*15)

        self.total_drinks_price=float((
            self.d_m_p+
            self.d_c_p+
            self.d_f_p+
            self.d_t_p+
            self.d_l_p+
            self.d_s_p
        ))
        self.cold_drink_prince.set(str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*.09),2)
        self.cold_drink_tax.set(str(self.d_tax))
        self.Total_bill=float(self.total_cosmatic_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_blll(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to MyBillApp\n")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n====================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n====================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","enter name and phone number")
        elif self.cosmatic_price.get()=="0.0" and  self.grocery_price.get()=="0.0" and self.cold_drink_prince.get()=="0.0":
            messagebox.showerror("Error","Please select a Product")
        else:

            self.welcome_blll()
            ######cosmatics#######
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t{self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t{self.c_hg_p}")
            if self.body_spray.get()!=0:
                self.txtarea.insert(END,f"\n Body Spray\t\t{self.body_spray.get()}\t{self.c_bl_p}")
            ######grocery#######
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")
            if self.food.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food.get()}\t{self.g_f_p}")
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.g_s_p}")
            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\n Salt\t\t{self.salt.get()}\t{self.g_t_p}")
            ######ColdDrinks#######
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t{self.d_m_p}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t{self.d_c_p}")
            if self.seven_up.get()!=0:
                self.txtarea.insert(END,f"\n Seven Up\t\t{self.seven_up.get()}\t{self.d_f_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumb Up\t\t{self.thumbs_up.get()}\t{self.d_t_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.d_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t{self.d_s_p}")


            self.txtarea.insert(END,f"\n------------------------------------")
            if self.cosmatic_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nCosmatic Tax\t\t\t{self.cosmatic_tax.get()}")
            if self.grocery_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="0.0":
                self.txtarea.insert(END,f"\nCold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\nTotal:\t\t\t{self.Total_bill}")
            self.txtarea.insert(END,f"\n------------------------------------")




root=Tk()
obj = billApp(root)
root.mainloop()
