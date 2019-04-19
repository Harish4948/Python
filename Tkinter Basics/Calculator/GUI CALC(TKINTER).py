from tkinter import *
import time

global num1,num2,ch
ch=0
class calc:
    def create(self,btframe):
        button7=Button(btframe,text="7",command=self.seven,bg="grey").grid(row=0,column=0)
        button8=Button(btframe,text="8",command=self.eight,bg="grey").grid(row=0,column=1)
        button9=Button(btframe,text="9",command=self.nine,bg="grey").grid(row=0,column=2)
        buttonmul=Button(btframe,text="*",command=self.mul,bg="grey").grid(row=0,column=3)
        button4=Button(btframe,text="4",command=self.four,bg="grey").grid(row=1,column=0)
        button5=Button(btframe,text="5",command=self.five,bg="grey").grid(row=1,column=1)
        button6=Button(btframe,text="6",command=self.six,bg="grey").grid(row=1,column=2)
        buttondiv=Button(btframe,text="/",command=self.div,bg="grey").grid(row=1,column=3)
        button1=Button(btframe,text="1",command=self.one,bg="grey").grid(row=2,column=0)
        button2=Button(btframe,text="2",command=self.two,bg="grey").grid(row=2,column=1)
        button3=Button(btframe,text="3",command=self.three,bg="grey").grid(row=2,column=2)
        buttonadd=Button(btframe,text="+",command=self.add,bg="grey").grid(row=2,column=3)
        buttonclr=Button(btframe,text="AC",command=self.clr,bg="grey").grid(row=3,column=0)
        button0=Button(btframe,text="0",command=self.zero,bg="grey").grid(row=3,column=1)
        buttoneq=Button(btframe,text="=",command=self.eq,bg="grey").grid(row=3,column=2)
        buttonsub=Button(btframe,text="-",command=self.sub,bg="grey").grid(row=3,column=3)
        buttont=Button(btframe,text="two",command=self.tw,bg="grey").grid(row=4,column=2)


    def one(self):
        a = str(value.get())
        value.set(a + "1")
    def two(self):
        a=str(value.get())
        value.set(a+"2")
    def three(self):
        a=str(value.get())
        value.set(a+"3")

    def four(self):
        a=str(value.get())
        value.set(a+"4")

    def five(self):
        a=str(value.get())
        value.set(a+"5")
    def six(self):
        a=str(value.get())
        value.set(a+"6")
    def seven(self):
        a=str(value.get())
        value.set(a+"7")
    def eight(self):
        a=str(value.get())
        value.set(a+"8")
    def nine(self):
        a=str(value.get())
        value.set(a+"9")
    def zero(self):
        a=str(value.get())
        value.set(a+"0")
    def add(self):
        global num1
        num1=float(value.get())
        value.set(0)
        global ch
        ch=1

    def sub(self):
        global num1
        num1 = float(value.get())
        value.set(0)
        global ch
        ch = 2

    def mul(self):
        global num1
        num1 = float(value.get())
        value.set(0)
        global ch
        #num11.set(num1)
        ch = 3

    def div(self):
        global num1
        num1 = float(value.get())
        value.set(0)
        global ch
        ch = 4

    def clr(self):
        value.set(0)

    def tw(self):
        global num2
        num2 = float(value.get())
        value.set(0)
        #num12.set(num2)

    def eq(self):
        res = 0
        if(ch==1):
            res=num1 + num2
            value.set(res)

        if (ch == 2):
            res = num1 - num2
            value.set(res)

        if (ch == 3):
            res = num1 * num2
            value.set(res)


        if (ch == 4):
            res = num1 / num2
            value.set(res)


root=Tk()
tpframe=Frame(root,width=800,height=600)
tpframe.pack()
value=IntVar()
btframe=Frame(root,width=800,height=600)
btframe.pack(side=BOTTOM)
ip=Entry(tpframe,textvariable=value).grid(row=0,column=0)
ob=calc()
ob.create(btframe)
root.mainloop()