from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from PIL import Image, ImageTk


def valid_cube_generation():
	c = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]
	for i in range(6):
		for j in range(3):
			for k in range(3):
				c[i][j][k] = i
	# for i in edges:
	# 	ind = random.randint(0,1)
		# TODO take 2 random edge from edges
		# and place them in cube at random edge_index
	return c
				

def side_displayer(x,y,c33):
	for i1 in range(3):
		for j1 in range(3):
			box_in_cube((x+50*i1),(y+50*j1),c33[i1][j1])

def display():
	for i in range(6):
		if cube[i][1][1] == 0:
			#Front  Black
			side_displayer(250,250,cube[i])
		elif cube[i][1][1] == 1:
			#Back  Yellow
			side_displayer(700,250,cube[i])
		elif cube[i][1][1] == 2:
			#Right Orange
			side_displayer(400,250,cube[i])			
		elif cube[i][1][1] == 3:
			#Top Blue
			side_displayer(250,100,cube[i])
		elif cube[i][1][1] == 4:
			#Left Red
			side_displayer(100,250,cube[i])
		else:
			#Bottom Green
			side_displayer(250,400,cube[i])

def box_in_cube(x,y,c):
	col=random.randint(0,5)
	while color_dict[col] >= 9:
		col = random.randint(0,5)
	color_dict[col] += 1
	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff" ,fill=color_box[c], width=5)
	# text=canvas.create_text(x+20, y+20, text = str(i)+str(i1)+str(i2), anchor='center', font='TkMenuFont', fill='white')


def rotation_by_phase_clock():
	i = 0

	temp = cube[i][0][0]
	cube[i][0][0]=cube[i][0][1]
	cube[i][0][1]=cube[i][0][2]
	cube[i][0][2]=cube[i][2][1]
	cube[i][1][2]=cube[i][2][2]
	cube[i][2][2]=cube[i][2][1]
	cube[i][2][1]=cube[i][2][0]
	cube[i][2][0]=cube[i][1][0]
	cube[i][1][0]=temp

	temp = cube[(i+3)%6][2][2]
	cube[(i+3)%6][2][2]=cube[(i+3)%6][1][2]
	cube[(i+3)%6][1][2]=cube[(i+3)%6][0][2]
	cube[(i+3)%6][0][2]=cube[(i+4)%6][2][0]

	cube[(i+4)%6][2][0]=cube[(i+4)%6][2][1]
	cube[(i+4)%6][2][1]=cube[(i+4)%6][2][0]
	cube[(i+4)%6][2][2]=cube[(i+5)%6][0][0]
	cube[(i+5)%6][0][0]=cube[(i+5)%6][1][0]
	cube[(i+5)%6][1][0]=cube[(i+5)%6][2][0]
	cube[(i+5)%6][2][0]=cube[(i+2)%6][0][2]
	cube[(i+2)%6][0][2]=cube[(i+2)%6][0][1]
	cube[(i+2)%6][0][1]=cube[(i+2)%6][0][0]
	cube[(i+2)%6][0][0]=temp
	 
	# display()



root = Tk()

root.title("Rubik's Cube Solver")


#Constants number represent color in cube 
color_box=['black','yellow','orange','blue','red','green']
# edges = [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(4,3),(4,5)]
# corners = [(0,2,3),(0,3,4),(0,4,5),(0,2,5),(1,2,3),(1,3,4),(1,4,5),(1,2,5)]
# edge_to_cube_map = {}

color_dict = {0:0,1:0,2:0,3:0,4:0,5:0}


canvas=Canvas(width=960, height=640, background='#808080')

image1 = Image.open("New folder/3.jpg")
test = ImageTk.PhotoImage(image1)
canvas.create_image(0, 0, image=test, anchor='nw')



cube = valid_cube_generation()


# button = Button(root, text="⤾", padx=10, pady=10, command=lambda: rotation_by_phase_clock("black"))
# button.place(x=100,y=100)


rotation_by_phase_clock()






for i in range(6):
	print(cube[i])

display()

canvas.pack()

root.mainloop()