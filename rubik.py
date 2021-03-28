from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from PIL import Image, ImageTk



def valid_cube_generation(c):
	for i in range(6):
		for j in range(3):
			for k in range(3):
				c[i][j][k]=i

	for i in edges:
		ind = random.randint(0,1)
		# TODO take 2 random edge from edges
		# and place them in cube at random edge_index
	return c
				

def side_displayer(x,y,c33):
	for i1 in range(3):
		for j1 in range(3):
			box_in_cube((x+50*i1),(y+50*j1),c33[i1][j1])
			if not bool(__debug__) :
				canvas.create_text(((x+50*i1), (y+50*j1)), text=f"{i1},{j1}")

def display(cube):
	for i in range(6):
		if cube[i][1][1] == 0:
			#Front  White
			side_displayer(250,250,cube[i])
		elif cube[i][1][1] == 1:
			#Back  Yellow
			side_displayer(700,250,cube[i])
		elif cube[i][1][1] == 2:
			#Right Green
			side_displayer(400,250,cube[i])			
		elif cube[i][1][1] == 3:
			#Top Blue
			side_displayer(250,100,cube[i])
		elif cube[i][1][1] == 4:
			#Left Red
			side_displayer(100,250,cube[i])
		else:
			#Bottom Orange
			side_displayer(250,400,cube[i])

def box_in_cube(x,y,c):
	box=canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff", fill=color_box[c], width=5)



"""
COLOR  : INDEX : FACE
BLACK  :   0   : FRONT
YELLOW :   1   : BACK
GREEN  :   2   : RIGHT
BLUE   :   3   : TOP
RED    :   4   : LEFT
ORANGE :   5   : BOTTOM
"""



def rotate_up_clock(cube):
	#phase(clockwise)
	temp,temp1,temp2 = cube[3][0][2],cube[3][0][1],cube[3][0][0]
	cube[3][0][2],cube[3][0][1],cube[3][0][0] = cube[3][2][2],cube[3][1][2],cube[3][0][2]
	cube[3][2][2],cube[3][1][2],cube[3][0][2] = cube[3][2][0],cube[3][2][1],cube[3][2][2]
	cube[3][2][0],cube[3][2][1],cube[3][2][2] = cube[3][0][0],cube[3][1][0],cube[3][2][0]
	cube[3][0][0],cube[3][1][0],cube[3][2][0] = temp,temp1,temp2
	
	# for a in range(3):
	temp,temp1,temp2 = cube[0][0][0],cube[0][1][0],cube[0][2][0]
	cube[0][0][0],cube[0][1][0],cube[0][2][0] = cube[2][0][0],cube[2][1][0],cube[2][2][0]
	cube[2][0][0],cube[2][1][0],cube[2][2][0] = cube[1][2][0],cube[1][1][0],cube[1][0][0]
	cube[1][2][0],cube[1][1][0],cube[1][0][0] = cube[4][0][0],cube[4][1][0],cube[4][2][0]
	cube[4][0][0],cube[4][1][0],cube[4][2][0] = temp,temp1,temp2
	return cube
def rotate_down_anti(cube):
	# phase(anti-clockwise)
	temp,temp1,temp2 = cube[5][0][2],cube[5][0][1],cube[5][0][0]
	cube[5][0][2],cube[5][0][1],cube[5][0][0] = cube[5][2][2],cube[5][1][2],cube[5][0][2]
	cube[5][2][2],cube[5][1][2],cube[5][0][2] = cube[5][2][0],cube[5][2][1],cube[5][2][2]
	cube[5][2][0],cube[5][2][1],cube[5][2][2] = cube[5][0][0],cube[5][1][0],cube[5][2][0]
	cube[5][0][0],cube[5][1][0],cube[5][2][0] = temp,temp1,temp2
	
	# for a in range(3):
	temp,temp1,temp2 = cube[0][0][2],cube[0][1][2],cube[0][2][2]
	cube[0][0][2],cube[0][1][2],cube[0][2][2] = cube[2][0][2],cube[2][1][2],cube[2][2][2]
	cube[2][0][2],cube[2][1][2],cube[2][2][2] = cube[1][2][2],cube[1][1][2],cube[1][0][2]
	cube[1][2][2],cube[1][1][2],cube[1][0][2] = cube[4][0][2],cube[4][1][2],cube[4][2][2]
	cube[4][0][2],cube[4][1][2],cube[4][2][2] = temp,temp1,temp2
	return cube

def rotate_up_anti(cube):
	cube = rotate_up_clock(cube)
	cube = rotate_up_clock(cube)
	cube = rotate_up_clock(cube)
	return cube

def rotate_down_clock(cube):
	cube = rotate_down_anti(cube)
	cube = rotate_down_anti(cube)
	cube = rotate_down_anti(cube)
	return cube

def rotate_right_anti(cube):
	cube = rotate_right_clock(cube)
	cube = rotate_right_clock(cube)
	cube = rotate_right_clock(cube)
	return cube

def rotate_left_anti(cube):
	cube = rotate_left_clock(cube)
	cube = rotate_left_clock(cube)
	cube = rotate_left_clock(cube)
	return cube

def rotate_right_clock(cube):
	#phase(clockwise)
	temp,temp1,temp2 = cube[2][0][2],cube[2][0][1],cube[2][0][0]
	cube[2][0][2],cube[2][0][1],cube[2][0][0] = cube[2][2][2],cube[2][1][2],cube[2][0][2]
	cube[2][2][2],cube[2][1][2],cube[2][0][2] = cube[2][2][0],cube[2][2][1],cube[2][2][2]
	cube[2][2][0],cube[2][2][1],cube[2][2][2] = cube[2][0][0],cube[2][1][0],cube[2][2][0]
	cube[2][0][0],cube[2][1][0],cube[2][2][0] = temp,temp1,temp2
	
	# for a in range(3):
	temp,temp1,temp2 = cube[0][2][0],cube[0][2][1],cube[0][2][1]
	cube[0][2][0],cube[0][2][1],cube[0][2][2] = cube[3][2][0],cube[3][2][1],cube[3][2][2]
	cube[3][2][0],cube[3][2][1],cube[3][2][2] = cube[1][0][0],cube[1][0][1],cube[1][0][2]
	cube[1][0][0],cube[1][0][1],cube[1][0][2] = cube[5][2][0],cube[5][2][1],cube[5][2][2]
	cube[5][2][0],cube[5][2][1],cube[5][2][2] = temp,temp1,temp2
	return cube

def rotate_left_clock(cube):
	
	temp,temp1,temp2 = cube[4][0][2],cube[4][0][1],cube[4][0][0]
	cube[4][0][2],cube[4][0][1],cube[4][0][0] = cube[4][2][2],cube[4][1][2],cube[4][0][2]
	cube[4][2][2],cube[4][1][2],cube[4][0][2] = cube[4][2][0],cube[4][2][1],cube[4][2][2]
	cube[4][2][0],cube[4][2][1],cube[4][2][2] = cube[4][0][0],cube[4][1][0],cube[4][2][0]
	cube[4][0][0],cube[4][1][0],cube[4][2][0] = temp,temp1,temp2
	
	# for a in range(3):
	temp,temp1,temp2 = cube[0][0][0],cube[0][0][1],cube[0][0][1]
	cube[0][0][0],cube[0][0][1],cube[0][0][2] = cube[3][0][0],cube[3][0][1],cube[3][0][2]
	cube[3][0][0],cube[3][0][1],cube[3][0][2] = cube[1][2][0],cube[1][2][1],cube[1][2][2]
	cube[1][2][0],cube[1][2][1],cube[1][2][2] = cube[5][0][0],cube[5][0][1],cube[5][0][2]
	cube[5][0][0],cube[5][0][1],cube[5][0][2] = temp,temp1,temp2
	return cube

def rotate_front_anti(cube):

	temp,temp1,temp2 = cube[0][0][0],cube[0][1][0],cube[0][2][0]
	cube[0][0][0],cube[0][1][0],cube[0][2][0] = cube[0][2][0],cube[0][2][1],cube[0][2][2]
	cube[0][2][0],cube[0][2][1],cube[0][2][2] = cube[0][2][2],cube[0][1][2],cube[0][0][2]
	cube[0][2][2],cube[0][1][2],cube[0][0][2] = cube[0][0][2],cube[0][0][1],cube[0][0][0]
	cube[0][0][2],cube[0][0][1],cube[0][0][0] = temp,temp1,temp2
	# for a in range(3):
	temp,temp1,temp2 = cube[5][0][0],cube[5][1][0],cube[5][2][0]
	cube[5][0][0],cube[5][1][0],cube[5][2][0] = cube[4][2][0],cube[4][2][1],cube[4][2][2]
	cube[4][2][0],cube[4][2][1],cube[4][2][2] = cube[3][2][2],cube[3][1][2],cube[3][0][2]
	cube[3][2][2],cube[3][1][2],cube[3][0][2] = cube[2][0][2],cube[2][0][1],cube[2][0][0]
	cube[2][0][2],cube[2][0][1],cube[2][0][0] = temp,temp1,temp2

	return cube

def rotate_front_clock(cube):
	
	temp,temp1,temp2 = cube[0][0][2],cube[0][0][1],cube[0][0][0]
	cube[0][0][2],cube[0][0][1],cube[0][0][0] = cube[0][2][2],cube[0][1][2],cube[0][0][2]
	cube[0][2][2],cube[0][1][2],cube[0][0][2] = cube[0][2][0],cube[0][2][1],cube[0][2][2]
	cube[0][2][0],cube[0][2][1],cube[0][2][2] = cube[0][0][0],cube[0][1][0],cube[0][2][0]
	cube[0][0][0],cube[0][1][0],cube[0][2][0] = temp,temp1,temp2
	
	# for a in range(3):
	temp,temp1,temp2 = cube[2][0][2],cube[2][0][1],cube[2][0][0]
	cube[2][0][2],cube[2][0][1],cube[2][0][0] = cube[3][2][2],cube[3][1][2],cube[3][0][2]
	cube[3][2][2],cube[3][1][2],cube[3][0][2] = cube[4][2][0],cube[4][2][1],cube[4][2][2]
	cube[4][2][0],cube[4][2][1],cube[4][2][2] = cube[5][0][0],cube[5][1][0],cube[5][2][0]
	cube[5][0][0],cube[5][1][0],cube[5][2][0] = temp,temp1,temp2
	
	

	return cube
def rotate_back_clock(cube):

	
	temp,temp1,temp2 = cube[1][0][2],cube[1][0][1],cube[1][0][0]
	cube[1][0][2],cube[1][0][1],cube[1][0][0] = cube[1][2][2],cube[1][1][2],cube[1][0][2]
	cube[1][2][2],cube[1][1][2],cube[1][0][2] = cube[1][2][0],cube[1][2][1],cube[1][2][2]
	cube[1][2][0],cube[1][2][1],cube[1][2][2] = cube[1][0][0],cube[1][1][0],cube[1][2][0]
	cube[1][0][0],cube[1][1][0],cube[1][2][0] = temp,temp1,temp2

	# for a in range(3):
	temp,temp1,temp2 = cube[2][2][2],cube[2][2][1],cube[2][2][0]
	cube[2][2][2],cube[2][2][1],cube[2][2][0] = cube[3][2][0],cube[3][1][0],cube[3][0][0]
	cube[3][2][0],cube[3][1][0],cube[3][0][0] = cube[4][0][0],cube[4][0][1],cube[4][0][2]
	cube[4][0][0],cube[4][0][1],cube[4][0][2] = cube[5][0][2],cube[5][1][2],cube[5][2][2]
	cube[5][0][2],cube[5][1][2],cube[5][2][2] = temp,temp1,temp2
	return cube


def rotate_back_anti(cube):
	
	temp,temp1,temp2 = cube[1][0][0],cube[1][1][0],cube[1][2][0]
	cube[1][0][0],cube[1][1][0],cube[1][2][0] = cube[1][2][0],cube[1][2][1],cube[1][2][2]
	cube[1][2][0],cube[1][2][1],cube[1][2][2] = cube[1][2][2],cube[1][1][2],cube[1][0][2]
	cube[1][2][2],cube[1][1][2],cube[1][0][2] = cube[1][0][2],cube[1][0][1],cube[1][0][0]
	cube[1][0][2],cube[1][0][1],cube[1][0][0] = temp,temp1,temp2

	
	# for a in range(3):
	temp,temp1,temp2 = cube[5][0][2],cube[5][1][2],cube[5][2][2]
	cube[5][0][2],cube[5][1][2],cube[5][2][2] = cube[4][0][0],cube[4][0][1],cube[4][0][2]
	cube[4][0][0],cube[4][0][1],cube[4][0][2] = cube[3][2][0],cube[3][1][0],cube[3][0][0]
	cube[3][2][0],cube[3][1][0],cube[3][0][0] = cube[2][2][2],cube[2][2][1],cube[2][2][0]
	cube[2][2][2],cube[2][2][1],cube[2][2][0] = temp,temp1,temp2

	return cube

root = Tk()

root.title("Rubik's Cube Solver")


#Constants number represent color in cube 
color_box=['black','yellow','green','blue','red','orange']
edges = [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(4,3),(4,5)]
corners = [(0,2,3),(0,3,4),(0,4,5),(0,2,5),(1,2,3),(1,3,4),(1,4,5),(1,2,5)]
edge_to_cube_map = {}

color_dict = {0:0,1:0,2:0,3:0,4:0,5:0}

canvas=Canvas(width=960, height=640, background='#808080')

image1 = Image.open("New folder/3.jpg")
test = ImageTk.PhotoImage(image1)
canvas.create_image(0, 0, image=test, anchor='nw')

c = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]
	

cube = valid_cube_generation(c)
move = 'F'
def button_click_event(event):
	move = event.char
	global cube
	# def wrapper(cube=cube, move = move):
	if move == 'f':
		cube = rotate_front_clock(cube)
		display(cube)
	elif move == 'b':
		cube = rotate_back_clock(cube)
		display(cube)
	elif move == 'F':
		cube = rotate_front_anti(cube)
		display(cube)
	elif move == 'B':
		cube = rotate_back_anti(cube)
		display(cube)
	elif move == 'u':
		cube = rotate_up_clock(cube)
		display(cube)
	elif move == 'U':
		cube = rotate_up_anti(cube)
		display(cube)
	elif move == 'l':
		cube = rotate_left_clock(cube)
		display(cube)
	elif move == 'L':
		cube = rotate_left_anti(cube)
		display(cube)
	elif move == 'r':
		cube = rotate_right_clock(cube)
		display(cube)
	elif move == 'R':
		cube = rotate_right_anti(cube)
		display(cube)
	elif move == 'd':
		cube = rotate_down_clock(cube)
		display(cube)
	elif move == 'D':
		cube = rotate_down_anti(cube)
		display(cube)
	# return wrapper
	print(move," ", cube)

for i in range(6):
	print(cube[i])

display(cube)

root.bind("<Key>",button_click_event)

canvas.pack()

root.mainloop()