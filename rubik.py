from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from PIL import Image, ImageTk


def side_displayer(x,y,c33):
	for i1 in range(3):
		for j1 in range(3):
			box_in_cube((x+50*i1),(y+50*j1),c33[i1][j1])

def display():
	for i in range(6):
		if cube[i][1][1] == 0:
			#Front
			side_displayer(250,250,cube[i])
		elif cube[i][1][1] == 1:
			#Back
			side_displayer(700,250,cube[i])
		elif cube[i][1][1] == 2:
			#Right
			side_displayer(400,250,cube[i])			
		elif cube[i][1][1] == 3:
			#Top
			side_displayer(250,100,cube[i])
		elif cube[i][1][1] == 4:
			#Left
			side_displayer(100,250,cube[i])
		else:
			#Bottom
			side_displayer(250,400,cube[i])

def box_in_cube(x,y,c):
	col=random.randint(0,5)
	while color_dict[col] >= 9:
		col = random.randint(0,5)
	color_dict[col] += 1
	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#666666", fill=color_box[c], width=5)


root = Tk()

root.title("Rubik's Cube Solver")

canvas=Canvas(width=960, height=640, background='#808080')

image1 = Image.open("New folder/2.jpg")
test = ImageTk.PhotoImage(image1)
canvas.create_image(0, 0, image=test, anchor='nw')

cube = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]

for i in range(6):
	cube[i][1][1] = i

for i in range(6):
	print(cube[i])

color_box=['white','yellow','green','blue','red','orange']

color_dict = {0:0,1:0,2:0,3:0,4:0,5:0}

display()

canvas.pack()

root.mainloop()