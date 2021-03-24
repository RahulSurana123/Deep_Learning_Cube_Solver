from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random

root=Tk()

root.title("Rubik's Cube Solver")
canvas=Canvas(width=1080, height=640, background='gray75')
color = ['red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange',
		'red','green','yellow','blue','white','orange']
color_box=['red','green','yellow','blue','white','orange']

color_dict = {0:0,1:0,2:0,3:0,4:0,5:0}

cube = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]

for i in range(6):
	cube[i][1][1] = i

for i in range(6):
	print(cube[i])




def phase_of_cube(x,y,color):

	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+50, y, x+100, y+50, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+100, y, x+150, y+50, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x, y+50, x+50, y+100, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+50, y+50, x+100, y+100, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+100, y+50, x+150, y+100, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x, y+100, x+50, y+150, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+50, y+100, x+100, y+150, outline="#000000", fill=color, width=2)
	box=canvas.create_rectangle(x+100, y+100, x+150, y+150, outline="#000000", fill=color, width=2)

def box_in_cube(x,y):
	col=random.randint(0,5)
	while color_dict[col] >= 9:
		col = random.randint(0,5)
	color_dict[col] += 1
	box1=canvas.create_rectangle(x, y, x+50, y+50, outline="#000000", fill=color[col], width=2)
	# color.remove(color[col])
	print(len(color))


canvas.pack()


#LEFT
button1=Button(canvas, text="<<",bg="gray")
button1.place(x=60, y=262)
button2=Button(canvas, text="<<",bg="gray")
button2.place(x=60, y=312)
button3=Button(canvas, text="<<",bg="gray")
button3.place(x=60, y=362)
#RIGHT
button4=Button(canvas, text=">>",bg="gray")
button4.place(x=562, y=262)
button5=Button(canvas, text=">>",bg="gray")
button5.place(x=562, y=312)
button6=Button(canvas, text=">>",bg="gray")
button6.place(x=562, y=362)
#TOP
button7=Button(canvas, text="^^",bg="gray")
button7.place(x=262, y=60)
button8=Button(canvas, text="^^",bg="gray")
button8.place(x=312, y=60)
button9=Button(canvas, text="^^",bg="gray")
button9.place(x=362, y=60)
#BOTTOM
button10=Button(canvas, text="vv",bg="gray")
button10.place(x=262, y=562)
button11=Button(canvas, text="vv",bg="gray")
button11.place(x=312, y=562)
button12=Button(canvas, text="vv",bg="gray")
button12.place(x=362, y=562)


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

def display():
	for i in range(6):
		if cube[i][1][1] == 0:
			side_displayer(250,100)
		elif cube[i][1][1] == 1:
			side_displayer(250,100)			

def side_displayer(x,y):
	for i1 in range(3):
		for j1 in range(3):
			print((x+50*i1),(y+50*j1))
			box_in_cube((x+50*i1),(y+50*j1))


#PHASES OF THE CUBE
 
#Top
side_displayer(250,100)
# for i1 in range(250,351,50):
# 	for j1 in range(100,201,50):
# 		print(i1,j1)
# 		box_in_cube(i1,j1)

#Right
side_displayer(400,250)
# for i2 in range(400,501,50):
# 	for j2 in range(250,351,50):
# 		print(i2,j2)
# 		box_in_cube(i2,j2)

#Left
side_displayer(100,250)
# for i3 in range(100,201,50):
# 	for j3 in range(250,351,50):
# 		print(i3,j3)
# 		box_in_cube(i3,j3)

#Bottom
side_displayer(250,400)
# for i4 in range(250,351,50):
# 	for j4 in range(400,501,50):
# 		print(i4,j4)
# 		box_in_cube(i4,j4)

#Front
side_displayer(250,250)
# for i5 in range(250,351,50):
# 	for j5 in range(250,351,50):
# 		print(i5,j5)
# 		box_in_cube(i5,j5)

#Back
side_displayer(700,250)
# for i6 in range(700,801,50):
# 	for j6 in range(250,351,50):
# 		print(i6,j6)
# 		box_in_cube(i6,j6)


root.mainloop()