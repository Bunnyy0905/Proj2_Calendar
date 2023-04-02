from tkinter import *
import calendar
#Creating main Window
root=Tk()
root.geometry("400x600")
root.resizable(0,0)
root.title("Calendar")

#defining function to display calendar
def show():
    a=int(spinbox1.get())
    b=int(spinbox2.get())
# typecasting them to integer, as function which we are using for getting calendar it requires data as integer arguments
    cal=calendar.month(b,a)#pass here your year and then month values
    #in our case we use b for year and a for month
    txtbox.delete(0.0,END)
    txtbox.insert(INSERT,cal)

#Creating Label
label1=Label(root, text="Month", font=("arial",9,"bold")).place(x=15,y=0)
label2=Label(root, text="Year", font=("arial",9,"bold")).place(x=140,y=0)
#Creating Spinbox
spinbox1=Spinbox(root, values=(1,2,3,4,5,6,7,8,9,10,11,12), width =4)
spinbox1.place(x=60,y=0)

spinbox2=Spinbox(root,from_=1999, to= 2100, width =4)
spinbox2.place(x=175,y=0)

#Creating Buttons
Button(root, text="Show",font=("times new roman",10,"bold"),command=show).place(x=100,y=30)

#Creating textbox to display calendar
txtbox=Text(root,width=24,height=8)
txtbox.place(x=20,y=57)

root.mainloop()
