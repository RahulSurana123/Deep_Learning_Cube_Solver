from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from PIL import Image, ImageTk



# label1 = Label(image=test)
# label1.image = test

# label1.pack()

root = Tk()

root.title("Rubik's Cube Solver")

canvas=Canvas(width=960, height=640, background='#808080')

image1 = Image.open("New folder/5.jpg")
test = ImageTk.PhotoImage(image1)
canvas.create_image(0, 0, image=test, anchor='nw')

color_box=['black','yellow','green','blue','red','orange']

color_dict = {0:0,1:0,2:0,3:0,4:0,5:0}

arr=[[[]*3]*6]



# def phase_of_cube(x,y,color):
# 	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+50, y, x+100, y+50, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+100, y, x+150, y+50, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x, y+50, x+50, y+100, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+50, y+50, x+100, y+100, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+100, y+50, x+150, y+100, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x, y+100, x+50, y+150, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+50, y+100, x+100, y+150, outline="#ffffff", fill=color, width=5)
# 	box=canvas.create_rectangle(x+100, y+100, x+150, y+150, outline="#ffffff", fill=color, width=5)

def box_in_cube(x,y):
	col=random.randint(0,5)
	while color_dict[col] >= 9:
		col = random.randint(0,5)
	color_dict[col] += 1
	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff", fill=color_box[col], width=5)


canvas.pack()


# #LEFT
# button1=Button(canvas, text="<<",bg="white")
# button1.place(x=60, y=262)
# button2=Button(canvas, text="<<",bg="white")
# button2.place(x=60, y=312)
# button3=Button(canvas, text="<<",bg="white")
# button3.place(x=60, y=362)
# #RIGHT
# button4=Button(canvas, text=">>",bg="white")
# button4.place(x=562, y=262)
# button5=Button(canvas, text=">>",bg="white")
# button5.place(x=562, y=312)
# button6=Button(canvas, text=">>",bg="white")
# button6.place(x=562, y=362)
# #TOP
# button7=Button(canvas, text="^^",bg="white")
# button7.place(x=262, y=60)
# button8=Button(canvas, text="^^",bg="white")
# button8.place(x=312, y=60)
# button9=Button(canvas, text="^^",bg="white")
# button9.place(x=362, y=60)
# #BOTTOM
# button10=Button(canvas, text="vv",bg="white")
# button10.place(x=262, y=562)
# button11=Button(canvas, text="vv",bg="white")
# button11.place(x=312, y=562)
# button12=Button(canvas, text="vv",bg="white")
# button12.place(x=362, y=562)



# #PHASES OF THE CUBE
 
# #Top
# phase_of_cube(250,100,'red')
# #Right
# phase_of_cube(400,250,'yellow')
# #Left
# phase_of_cube(100,250,'orange')
# #Bottom
# phase_of_cube(250,400,'white')
# #Front
# phase_of_cube(250,250,'blue')
# #Back
# phase_of_cube(750,250,'green')


#PHASES OF THE CUBE
def side_displayer(x,y):
	for i1 in range(3):
		for j1 in range(3):
			# print((x+50*i1),(y+50*j1))
			box_in_cube((x+50*i1),(y+50*j1))


#PHASES OF THE CUBE
 
#Top
side_displayer(250,100)

#Right
side_displayer(400,250)

#Left
side_displayer(100,250)

#Bottom
side_displayer(250,400)

#Front
side_displayer(250,250)

#Back
side_displayer(700,250)

root.mainloop()