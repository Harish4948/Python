from tkinter import*
import random
import time
import datetime
import pymysql

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")
root.configure(background="Black")

Tops=Frame(root, width=1600,relief=SUNKEN,background="Black")
Tops.pack()

f1=Frame(root,width=800,height=700,relief=SUNKEN,background="Black")
f1.pack()


#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'underline'),text="RESTAURANT ",fg="Red",bg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'underline'),text=localtime,fg="Light Blue",bg="Black",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    global randomRef,CoRoti,CoDhalmakhani,CoRasgulla,CoLassi,CoRajma,CoFriedrice,CostofMeal,OverAllCost,Service,PayTax,CostofMeal

    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
    
    if (Roti.get()==""):
        CoRoti=0
    else:
        CoRoti=float(Roti.get())
        
    if (Dhalmakhani.get()==""):
        CoDhalmakhani=0
    else:
        CoDhalmakhani=float(Dhalmakhani.get())



    if (Rasgulla.get()==""):
        CoRasgulla=0
    else:
        CoRasgulla=float(Rasgulla.get())



    if (Rajma.get()==""):
        CoRajma=0
    else:
        CoRajma=float(Rajma.get())

        
    if (Friedrice.get()==""):

        CoFriedrice=0
    else:
        CoFriedrice=float(Friedrice.get())

     
    if (Lassi.get()==""):
        CoLassi=0
    else:
        CoLassi=float(Lassi.get())

                   
    CostofRoti =CoRoti * 25
    CostofLassi=CoLassi * 20
    CostofDhalmakhani = CoDhalmakhani* 50
    CostofRasgulla = CoRasgulla * 25
    CostRajma = CoRajma* 40
    CostFriedrice=CoFriedrice * 35

    CostofMeal= "Rs", str('%.2f' % (CostofRoti+CostofLassi+CostofDhalmakhani+CostofRasgulla+CostRajma+CostFriedrice))

    PayTax=((CostofRoti+CostofLassi+CostofDhalmakhani+CostofRasgulla+CostRajma+CostFriedrice) * 0.2)

    TotalCost=(CostofRoti+CostofLassi+CostofDhalmakhani+CostofRasgulla+CostRajma+CostFriedrice)
 
    Ser_Charge= ((CostofRoti+CostofLassi+CostofDhalmakhani+CostofRasgulla+CostRajma+CostFriedrice)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
    
def qExit():
    root.destroy()

def Reset():
    connection = pymysql.connect('localhost','root','','rest')
    cursor = connection.cursor()
    SQLCommand = ("INSERT INTO invoice(Reference, Roti, Dhalmakhani, Rasgulla, Lassi, Rajma, Friedrice, SubTotal, Total, Service_Charge, Tax, Cost) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    Values = [randomRef,CoRoti,CoDhalmakhani,CoRasgulla,CoLassi,CoRajma,CoFriedrice,CostofMeal,OverAllCost,Service,PayTax,CostofMeal]  
    cursor.execute(SQLCommand,Values)
    connection.commit()
    connection.close()
    rand.set("") 
    Roti.set("")
    Dhalmakhani.set("")
    Rasgulla.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Lassi.set("")
    Tax.set("")
    Cost.set("")
    Rajma.set("")
    Friedrice.set("")
   

#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Roti=StringVar()
Dhalmakhani=StringVar()
Rasgulla=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Lassi=StringVar()
Tax=StringVar()
Cost=StringVar()
Rajma=StringVar()
Friedrice=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bg="Black",fg="Red",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="White",justify='right')
txtReference.grid(row=0,column=1)

lblRoti= Label(f1, font=('arial', 16, 'bold'),text="Roti",bg="Black",fg="Red",bd=16,anchor="w")
lblRoti.grid(row=1, column=0)
txtRoti=Entry(f1, font=('arial',16,'bold'),textvariable=Roti,bd=10,insertwidth=4,bg="White",justify='right')
txtRoti.grid(row=1,column=1)


lblDhalmakhani= Label(f1, font=('arial', 16, 'bold'),text="Dhalmakhani",bg="Black",fg="Red",bd=16,anchor="w")
lblDhalmakhani.grid(row=2, column=0)
txtDhalmakhani=Entry(f1, font=('arial',16,'bold'),textvariable=Dhalmakhani,bd=10,insertwidth=4,bg="White",justify='right')
txtDhalmakhani.grid(row=2,column=1)


lblRasgulla= Label(f1, font=('arial', 16, 'bold'),text="Rasgulla",bg="Black",fg="Red",bd=16,anchor="w")
lblRasgulla.grid(row=3, column=0)
txtRasgulla=Entry(f1, font=('arial',16,'bold'),textvariable=Rasgulla,bd=10,insertwidth=4,bg="White",justify='right')
txtRasgulla.grid(row=3,column=1)

lblRajma= Label(f1, font=('arial', 16, 'bold'),text="Rajma",bg="Black",fg="Red",bd=16,anchor="w")
lblRajma.grid(row=4, column=0)
txtRajma=Entry(f1, font=('arial',16,'bold'),textvariable=Rajma,bd=10,insertwidth=4,bg="White",justify='right')
txtRajma.grid(row=4,column=1)
Entry
lblFriedrice= Label(f1, font=('arial', 16, 'bold'),text="Friedrice",bg="Black",fg="Red",bd=16,anchor="w")
lblFriedrice.grid(row=5, column=0)
txtFriedrice=Entry(f1, font=('arial',16,'bold'),textvariable=Friedrice,bd=10,insertwidth=4,bg="White",justify='right')
txtFriedrice.grid(row=5,column=1)

#==========Entry==================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblLassi= Label(f1, font=('arial', 16, 'bold'),text="Lassi",bg="Black",fg="Red",bd=16,anchor="w")
lblLassi.grid(row=0, column=2)
txtLassi=Entry(f1, font=('arial',16,'bold'),textvariable=Lassi,bd=10,insertwidth=4,bg="White",justify='right')
txtLassi.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bg="Black",fg="Red",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="White",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bg="Black",fg="Red",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="White",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bg="Black",fg="Red",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="White",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bg="Black",fg="Red",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="White",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bg="Black",fg="Red",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="White",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="White",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="White",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="Dark Red",command=qExit).grid(row=7,column=3)


    


root.mainloop()


