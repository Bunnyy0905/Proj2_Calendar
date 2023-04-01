from tkinter import *
root=Tk()
root.geometry("800x400")
c=Canvas(root, width=800, height=400,borderwidth=6, relief=RAISED)
c.pack()
c.create_line(0,0,800,400, fill="red") #create_line-->used to create a line on canvas, specify 2 points(X,Y) i.e. 4 coordinates(x1,y1) and (x2,y2)

c.create_rectangle(100,200,350,400,fill="yellow")#create.rectangle-->used to create a rectangle on canvas. Specify 2 points --> Top Left Coordinate, Bootom Right Coordinate --> points(X,Y) i.e. 4 coordinates(x1,y1) and (x2,y2)
c.create_text(225,300,text="Hello! I am a rectangle")#create.text-->used to write a text on canvas. To get a text on center, use the center cordinates 
#for e.g here we used the center coordinates of rectangle X=x1+x2/2=100+350/2=450/2=225 , Y=y1+y2/2=200+400/2=600/2=300

c.create_oval(400,100,800,200,fill="green")#create_oval-->used to create an oval on canvas. Firstly draw a rectangle, specify 2 points --> Top Left Coordinate, Bootom Right Coordinate --> points(X,Y) i.e. 4 coordinates(x1,y1) and (x2,y2)
c.create_text(600,150,text="Hii! I am an oval")#create.text-->used to write a text on canvas. To get a text on center, use the center cordinates.
#for e.g here we used the center coordinates of oval X=x1+x2/2=400+800/2=1200/2=600 , Y=y1+y2/2=100+200/2=300/2=150

root.mainloop()