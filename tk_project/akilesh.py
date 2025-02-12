From tkinter import *
From tkinter import ttk
Import tkinter.messagebox as tmsg
Import os
Import time

#===================Python Variables=======================
Menu_category = ["Tea &Coffee","Beverages","FastFood","SouthIndian","Starters","MainCourse","Dessert"]

Menu_category_dict = {“Tea & Coffee”:”1 Tea & Coffee.txt”,”Beverages”:”2 Beverages.txt”,
                “Fast Food”:”3 Fast Food.txt”,”South Indian”:”4 South Indian.txt”,
                “Starters”:”5 Starters.txt”,”Main Course”:”6 Main Course.txt”,
                “Dessert”:”7 Dessert.txt”}

Order_dict = {}
For I in menu_category:
Order_dict[i] = {}

Os.chdir(os.path.dirname(os.path.abspath(__file__)))
#====================Backend Functions===========================
Def load_menu():
menuCategory.set(“”)
menu_tabel.delete(*menu_tabel.get_children())
menu_file_list = os.listdir(“Menu”)
    for file in menu_file_list:
        f = open(“Menu\\” + file , “r”)
        category=””
        while True:
            line = f.readline()
            if(line==””):
menu_tabel.insert(‘’,END,values=[“”,””,””])
                break
elif (line==”\n”):
                continue
elif(line[0]==’#’):
                category = line[1:-1]
                name = “\t\t”+line[:-1]
                price = “”
elif(line[0]==’*’):
                name = line[:-1]
                price = “”
            else:
                name = line[:line.rfind(“ “)]
                price = line[line.rfind(“ “)+1:-3]

menu_tabel.insert(‘’,END,values=[name,price,category])
        #menu_tabel.insert(‘’,END,values=[“Masala Dosa”,”50”])

Def load_order():
Order_tabel.delete(*order_tabel.get_children())
    For category in order_dict.keys():
        If order_dict[category]:
            For lis in order_dict[category].values():
Order_tabel.insert(‘’,END,values=lis)
Update_total_price()

Def add_button_operation():
    Name = itemName.get()
    Rate = itemRate.get()
    Category = itemCategory.get()
    Quantity = itemQuantity.get()

    If name in order_dict[category].keys():
Tmsg.showinfo(“Error”, “Item already exist in your order”)
        Return
    If not quantity.isdigit():
Tmsg.showinfo(“Error”, “Please Enter Valid Quantity”)
        Return
    Lis = [name,rate,quantity,str(int(rate)*int(quantity)),category]
Order_dict[category][name] = lis
Load_order()

Def load_item_from_menu(event):
Cursor_row = menu_tabel.focus()
    Contents = menu_tabel.item(cursor_row)
    Row = contents[“values”]

itemName.set(row[0])
itemRate.set(row[1])
itemCategory.set(row[2])
itemQuantity.set(“1”)

defload_item_from_order(event):
cursor_row = order_tabel.focus()
    contents = order_tabel.item(cursor_row)
    row = contents[“values”]

itemName.set(row[0])
itemRate.set(row[1])
itemQuantity.set(row[2])
itemCategory.set(row[4])

defshow_button_operation():
    category = menuCategory.get()
    if category not in menu_category:
tmsg.showinfo(“Error”, “Please select valid Choice”)
    else:
menu_tabel.delete(*menu_tabel.get_children())
        f = open(“Menu\\” + menu_category_dict[category] , “r”)
        while True:
            line = f.readline()
            if(line==””):
                break
            if (line[0]==’#’ or line==”\n”):
                continue
            if(line[0]==’*’):
                name = “\t”+line[:-1]
menu_tabel.insert(‘’,END,values=[name,””,””])
            else:
                name = line[:line.rfind(“ “)]
                price = line[line.rfind(“ “)+1:-3]
menu_tabel.insert(‘’,END,values=[name,price,category])

defclear_button_operation():
itemName.set(“”)
itemRate.set(“”)
itemQuantity.set(“”)
itemCategory.set(“”)

defcancel_button_operation():
    names = []
    for I in menu_category:
names.extend(list(order_dict[i].keys()))
    if len(names)==0:
tmsg.showinfo(“Error”, “Your order list is Empty”)
        return
ans = tmsg.askquestion(“Cancel Order”, “Are You Sure to Cancel Order?”)
    if ans==”no”:
        return
order_tabel.delete(*order_tabel.get_children())
    for I in menu_category:
order_dict[i] = {}
clear_button_operation()
update_total_price()

defupdate_button_operation():
    name = itemName.get()
    rate = itemRate.get()
    category = itemCategory.get()
    quantity = itemQuantity.get()

    if category==””:
        return
    if name not in order_dict[category].keys():
tmsg.showinfo(“Error”, “Item is not in your order list”)
        return
    if order_dict[category][name][2]==quantity:
tmsg.showinfo(“Error”, “No changes in Quantity”)
        return
order_dict[category][name][2] = quantity
order_dict[category][name][3] = str(int(rate)*int(quantity))
load_order()

defremove_button_operation():
    name = itemName.get()
    category = itemCategory.get()

    if category==””:
        return
    if name not in order_dict[category].keys():
tmsg.showinfo(“Error”, “Item is not in your order list”)
        return
    del order_dict[category][name]
load_order()

defupdate_total_price():
    price = 0
    for I in menu_category:
        for j in order_dict[i].keys():
            price += int(order_dict[i][j][3])
    if price == 0:
totalPrice.set(“”)
    else:
totalPrice.set(“Rs. “+str(price)+”  /-“)

defbill_button_operation():
customer_name = customerName.get()
customer_contact = customerContact.get()
    names = []
    for I in menu_category:
names.extend(list(order_dict[i].keys()))
    if len(names)==0:
tmsg.showinfo(“Error”, “Your order list is Empty”)
        return
    if customer_name==”” or customer_contact==””:
tmsg.showinfo(“Error”, “Customer Details Required”)
        return
    if not customerContact.get().isdigit():
tmsg.showinfo(“Error”, “Invalid Customer Contact”)
        return   
ans = tmsg.askquestion(“Generate Bill”, “Are You Sure to Generate Bill?”)
ans = “yes”
    if ans==”yes”:
        bill = Toplevel()
bill.title(“Bill”)
bill.geometry(“670x500+300+100”)
bill.wm_iconbitmap(“Coffee.ico”)
bill_text_area = Text(bill, font=(“arial”, 12))
st = “\t\t\t\tKD RESTAURAUNTS\n\t\t\tAttur, Salem-636102\n”
st += “\t\t\tGST.NO:- 27AHXPP3379HIZH\n”
st += “-“*61 + “BILL” + “-“*61 + “\nDate:- “

        #Date and time
        T = time.localtime(time.time())
Week_day_dict = {0:”Monday”,1:”Tuesday”,2:”Wednesday”,3:”Thursday”,4:”Friday”,5:”Saturday”,
                            6:”Sunday”}
        St += f”{t.tm_mday} / {t.tm_mon} / {t.tm_year} ({week_day_dict[t.tm_wday]})”
        St += “ “*10 + f”\t\t\t\t\t\tTime:- {t.tm_hour} : {t.tm_min} : {t.tm_sec}”

        #Customer Name & Contact
        St += f”\nCustomer Name:- {customer_name}\nCustomer Contact:- {customer_contact}\n”
        St += “-“*130 + “\n” + “ “*4 + “DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n”
        St += “-“*130 + “\n”

        #List of Items
        For I in menu_category:
            For j in order_dict[i].keys():
                Lis = order_dict[i][j]
                Name = lis[0]
                Rate = lis[1]
                Quantity = lis[2]
                Price = lis[3]
                St += name + “\t\t\t\t\t” + rate + “\t      “ + quantity + “\t\t  “ + price + “\n\n”
        St += “-“*130

        #Total Price
        St += f”\n\t\t\tTotal price : {totalPrice.get()}\n”
        St += “-“*130

        #display bill in new window
Bill_text_area.insert(1.0, st)

        #write into file
        Folder = f”{t.tm_mday},{t.tm_mon},{t.tm_year}”
        If not os.path.exists(f”Bill Records\\{folder}”):
Os.makedirs(f”Bill Records\\{folder}”)
        File = open(f”Bill Records\\{folder}\\{customer_name+customer_contact}.txt”, “w”)
File.write(st)
File.close()

        #Clear operaitons
Order_tabel.delete(*order_tabel.get_children())
        For I in menu_category:
Order_dict[i] = {}
Clear_button_operation()
Update_total_price()
customerName.set(“”)
customerContact.set(“”)

bill_text_area.pack(expand=True, fill=BOTH)
bill.focus_set()
bill.protocol(“WM_DELETE_WINDOW”, close_window)

defclose_window():
tmsg.showinfo(“Thanks”, “Thanks for using our service”)
root.destroy()
#[name,rate,quantity,str(int(rate)*int(quantity)),category]
#==================Backend Code Ends===============

#================Frontend Code Start==============
Root = Tk()
W, h = root.winfo_screenwidth(), root.winfo_screenheight()
Root.geometry(“%dx%d+0+0” % (w, h))
Root.title(“Welcome to KD RESTAURANTS”)
Root.wm_iconbitmap(“Burger.ico”)
#root.attributes(‘-fullscreen’, True)
#root.resizable(0, 0)

#================Title==============
Style_button = ttk.Style()
Style_button.configure(“TButton”,font = (“arial”,10,”bold”),
   Background=”lightgreen”)

Title_frame = Frame(root, bd=8, bg=”yellow”, relief=GROOVE)
Title_frame.pack(side=TOP, fill=”x”)

Title_label = Label(title_frame, text=”KD RESTAURANTS”, 
                    Font=(“times new roman”, 20, “bold”),bg = “yellow”, fg=”red”, pady=5)
Title_label.pack()

#==============Customer=============
Customer_frame = LabelFrame(root,text=”Customer Details”,font=(“times new roman”, 15, “bold”),
Bd=8, bg=”lightblue”, relief=GROOVE)
Customer_frame.pack(side=TOP, fill=”x”)

Customer_name_label = Label(customer_frame, text=”Name”, 
                    Font=(“arial”, 15, “bold”),bg = “lightblue”, fg=”blue”)
Customer_name_label.grid(row = 0, column = 0)

customerName = StringVar()
customerName.set(“”)
customer_name_entry = Entry(customer_frame,width=20,font=”arial 15”,bd=5,
textvariable=customerName)
customer_name_entry.grid(row = 0, column=1,padx=50)

customer_contact_label = Label(customer_frame, text=”Contact”, 
                    font=(“arial”, 15, “bold”),bg = “lightblue”, fg=”blue”)
customer_contact_label.grid(row = 0, column = 2)

customerContact = StringVar()
customerContact.set(“”)
customer_contact_entry = Entry(customer_frame,width=20,font=”arial 15”,bd=5,
textvariable=customerContact)
customer_contact_entry.grid(row = 0, column=3,padx=50)

#===============Menu===============
Menu_frame = Frame(root,bd=8, bg=”lightgreen”, relief=GROOVE)
Menu_frame.place(x=0,y=125,height=585,width=680)

Menu_label = Label(menu_frame, text=”Menu”, 
                    Font=(“times new roman”, 20, “bold”),bg = “lightgreen”, fg=”red”, pady=0)
Menu_label.pack(side=TOP,fill=”x”)

Menu_category_frame = Frame(menu_frame,bg=”lightgreen”,pady=10)
Menu_category_frame.pack(fill=”x”)

Combo_lable = Label(menu_category_frame,text=”Select Type”, 
                    Font=(“arial”, 12, “bold”),bg = “lightgreen”, fg=”blue”)
Combo_lable.grid(row=0,column=0,padx=10)

menuCategory = StringVar()
combo_menu = ttk.Combobox(menu_category_frame,values=menu_category,
textvariable=menuCategory)
combo_menu.grid(row=0,column=1,padx=30)

show_button = ttk.Button(menu_category_frame, text=”Show”,width=10,
                        command=show_button_operation)
show_button.grid(row=0,column=2,padx=60)

show_all_button = ttk.Button(menu_category_frame, text=”Show All”,
                        width=10,command=load_menu)
show_all_button.grid(row=0,column=3)

############################# Menu Tabel ##########################################
Menu_tabel_frame = Frame(menu_frame)
Menu_tabel_frame.pack(fill=BOTH,expand=1)

Scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
Scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)

Style = ttk.Style()
Style.configure(“Treeview.Heading”,font=(“arial”,13, “bold”))
Style.configure(“Treeview”,font=(“arial”,12),rowheight=25)

Menu_tabel = ttk.Treeview(menu_tabel_frame,style = “Treeview”,
            Columns =(“name”,”price”,”category”),xscrollcommand=scrollbar_menu_x.set,
Yscrollcommand=scrollbar_menu_y.set)

Menu_tabel.heading(“name”,text=”Name”)
Menu_tabel.heading(“price”,text=”Price”)
Menu_tabel[“displaycolumns”]=(“name”, “price”)
Menu_tabel[“show”] = “headings”
Menu_tabel.column(“price”,width=50,anchor=’center’)

Scrollbar_menu_x.pack(side=BOTTOM,fill=X)
Scrollbar_menu_y.pack(side=RIGHT,fill=Y)

Scrollbar_menu_x.configure(command=menu_tabel.xview)
Scrollbar_menu_y.configure(command=menu_tabel.yview)

Menu_tabel.pack(fill=BOTH,expand=1)


#menu_tabel.insert(‘’,END,values=[“Masala Dosa”,”50”])
Load_menu()
Menu_tabel.bind(“<ButtonRelease-1>”,load_item_from_menu)


#===============Item Frame=============
Item_frame = Frame(root,bd=8, bg=”lightgreen”, relief=GROOVE)
Item_frame.place(x=680,y=125,height=230,width=680)

Item_title_label = Label(item_frame, text=”Item”, 
                    Font=(“times new roman”, 20, “bold”),bg = “lightgreen”, fg=”red”)
Item_title_label.pack(side=TOP,fill=”x”)

Item_frame2 = Frame(item_frame, bg=”lightgreen”)
Item_frame2.pack(fill=X)

Item_name_label = Label(item_frame2, text=”Name”, 
                    Font=(“arial”, 12, “bold”),bg = “lightgreen”, fg=”blue”)
Item_name_label.grid(row=0,column=0)

itemCategory = StringVar()
itemCategory.set(“”)

itemName = StringVar()
itemName.set(“”)
item_name = Entry(item_frame2, font=”arial 12”,textvariable=itemName,state=DISABLED, width=25)
item_name.grid(row=0,column=1,padx=10)

item_rate_label = Label(item_frame2, text=”Rate”, 
                    font=(“arial”, 12, “bold”),bg = “lightgreen”, fg=”blue”)
item_rate_label.grid(row=0,column=2,padx=40)

itemRate = StringVar()
itemRate.set(“”)
item_rate = Entry(item_frame2, font=”arial 12”,textvariable=itemRate,state=DISABLED, width=10)
item_rate.grid(row=0,column=3,padx=10)

item_quantity_label = Label(item_frame2, text=”Quantity”, 
                    font=(“arial”, 12, “bold”),bg = “lightgreen”, fg=”blue”)
item_quantity_label.grid(row=1,column=0,padx=30,pady=15)

itemQuantity = StringVar()
itemQuantity.set(“”)
item_quantity = Entry(item_frame2, font=”arial 12”,textvariable=itemQuantity, width=10)
item_quantity.grid(row=1,column=1)

item_frame3 = Frame(item_frame, bg=”lightgreen”)
item_frame3.pack(fill=X)

add_button = ttk.Button(item_frame3, text=”Add Item”
                        ,command=add_button_operation)
Add_button.grid(row=0,column=0,padx=40,pady=30)

Remove_button = ttk.Button(item_frame3, text=”Remove Item”
                        ,command=remove_button_operation)
Remove_button.grid(row=0,column=1,padx=40,pady=30)

Update_button = ttk.Button(item_frame3, text=”Update Quantity”
                        ,command=update_button_operation)
Update_button.grid(row=0,column=2,padx=40,pady=30)

Clear_button = ttk.Button(item_frame3, text=”Clear”,
                        Width=8,command=clear_button_operation)
Clear_button.grid(row=0,column=3,padx=40,pady=30)

#==============Order Frame=====================
Order_frame = Frame(root,bd=8, bg=”lightgreen”, relief=GROOVE)
Order_frame.place(x=680,y=335,height=370,width=680)

Order_title_label = Label(order_frame, text=”Your Order”, 
                    Font=(“times new roman”, 20, “bold”),bg = “lightgreen”, fg=”red”)
Order_title_label.pack(side=TOP,fill=”x”)

############################## Order Tabel ###################################
Order_tabel_frame = Frame(order_frame)
Order_tabel_frame.place(x=0,y=40,height=260,width=680)

Scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
Scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

Order_tabel = ttk.Treeview(order_tabel_frame,
            Columns =(“name”,”rate”,”quantity”,”price”,”category”),xscrollcommand=scrollbar_order_x.set,
Yscrollcommand=scrollbar_order_y.set)

Order_tabel.heading(“name”,text=”Name”)
Order_tabel.heading(“rate”,text=”Rate”)
Order_tabel.heading(“quantity”,text=”Quantity”)
Order_tabel.heading(“price”,text=”Price”)
Order_tabel[“displaycolumns”]=(“name”, “rate”,”quantity”,”price”)
Order_tabel[“show”] = “headings”
Order_tabel.column(“rate”,width=100,anchor=’center’, stretch=NO)
Order_tabel.column(“quantity”,width=100,anchor=’center’, stretch=NO)
Order_tabel.column(“price”,width=100,anchor=’center’, stretch=NO)

Order_tabel.bind(“<ButtonRelease-1>”,load_item_from_order)

Scrollbar_order_x.pack(side=BOTTOM,fill=X)
Scrollbar_order_y.pack(side=RIGHT,fill=Y)

Scrollbar_order_x.configure(command=order_tabel.xview)
Scrollbar_order_y.configure(command=order_tabel.yview)

Order_tabel.pack(fill=BOTH,expand=1)

# order_tabel.insert(‘’,END,text=”Hello”,values=[“Masala Dosa”,”50”,”2”,”100”])

Total_price_label = Label(order_frame, text=”Total Price”, 
                    Font=(“arial”, 12, “bold”),bg = “lightgreen”, fg=”blue”)
Total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=10)

totalPrice = StringVar()
totalPrice.set(“”)
total_price_entry = Entry(order_frame, font=”arial 12”,textvariable=totalPrice,state=DISABLED, 
                            width=10)
total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=10)

bill_button = ttk.Button(order_frame, text=”Bill”,width=8,
                        command=bill_button_operation)
bill_button.pack(side=LEFT,anchor=SW,padx=80,pady=10)

cancel_button = ttk.Button(order_frame, text=”Cancel Order”,command=cancel_button_operation)
cancel_button.pack(side=LEFT,anchor=SW,padx=20,pady=10)

root.mainloop()
