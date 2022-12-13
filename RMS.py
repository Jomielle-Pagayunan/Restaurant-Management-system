from tkinter import*
import random

root = Tk()
root.geometry("1350x700+0+0")
root.resizable(0,0)
root.title("Restaurant Management System")

topFrame = Frame(root,bd=10,bg='navajo white',relief=RIDGE)
topFrame.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
labelTitle = Label(topFrame,text="Restaurant Management System", font=( 'georgia' ,30 , 'bold' ),fg="black",bg='navajo White',bd=10,width=48)
labelTitle.grid(row=0,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('georgia' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="navajo white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    # rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Php.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Php.",str('%.2f'% Ser_Charge)
    OverAllCost="Php.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Php.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

#calculator
btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="7",bg="navajo white", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="8",bg="navajo white", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="9",bg="navajo white", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="+",bg="navajo white", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('geogia', 20 ,'bold'),text="4",bg="navajo white", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('geogia', 20 ,'bold'),text="5",bg="navajo white", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('geogia', 20 ,'bold'),text="6",bg="navajo white", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="-",bg="navajo white", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('eorgia', 20 ,'bold'),text="1",bg="navajo white", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('geogia', 20 ,'bold'),text="2",bg="navajo white", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('geogia', 20 ,'bold'),text="3",bg="navajo white", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="*",bg="navajo white", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="0",bg="navajo white", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="c",bg="navajo white", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('georgia', 20 ,'bold'),text="=",bg="navajo white",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text=".",bg="navajo white", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('georgia', 20 ,'bold'),text="/",bg="navajo white", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)

#---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=('georgia', 15 ,'bold'),text="Order No.",fg="black",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=('georgia', 15 ,'bold'),text="Fries Meal",fg="black",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=('georgia', 15 ,'bold'),text="Lunch Meal",fg="black",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=('georgia', 15 ,'bold'),text="Burger Meal",fg="black",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=('georgia', 15 ,'bold'),text="Pizza Meal",fg="black",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=('georgia', 15 ,'bold'),text="Cheese burger",fg="black",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=('georgia', 15 ,'bold'),text="Drinks",fg="black",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Drinks , bd=6,insertwidth=3,bg="navajo white" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=('georgia', 15 ,'bold'),text="cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=('georgia', 15 ,'bold'),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=('georgia', 15 ,'bold'),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=('georgia', 15 ,'bold'),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=('georgia', 15 ,'bold'),text="Total",fg="black",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('georgia', 15 ,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="navajo white" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="navajo white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=10,pady=8, bd=10 ,fg="black",font=('georgia', 15 ,'bold'),width=10, text="TOTAL", bg="navajo white",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=10,pady=8, bd=10 ,fg="black",font=('georgia', 15 ,'bold'),width=10, text="RESET", bg="navajo white",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=10,pady=8, bd=10 ,fg="black",font=('georgia', 15 ,'bold'),width=10, text="EXIT", bg="navajo white",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Fries Meal", fg="black", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="25", fg="black", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Lunch Meal", fg="black", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="40", fg="black", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Burger Meal", fg="black", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="35", fg="black", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Pizza Meal", fg="black", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="50", fg="black", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Cheese Burger", fg="black", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="30", fg="black", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="Drinks", fg="black", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('georgia', 15, 'bold'), text="35", fg="black", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=10,pady=8, bd=10 ,fg="black",font=('georgia', 16, 'bold'),width=10, text="PRICE", bg="navajo white",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()