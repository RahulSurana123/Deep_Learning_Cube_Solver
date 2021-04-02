from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from PIL import Image,ImageTk

class Rubik:
	
	"""
	COLOR  : INDEX : FACE
	BLACK  :   0   : FRONT
	YELLOW :   1   : BACK
	BLUE   :   2   : RIGHT
	ORANGE :   3   : UP
	GREEN  :   4   : LEFT
	RED    :   5   : BOTTOM
	"""

	#Constants number represent color in self.cube 
	color_box=['black','yellow','blue','orange','green','red']
	edges = [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(4,3),(4,5)]
	corners = [(0,2,3),(0,3,4),(0,4,5),(0,2,5),(1,2,3),(1,3,4),(1,4,5),(1,2,5)]
	moveCharList = ['f','F', 'b', 'B', 'r', 'R', 'l', 'L', 'u', 'U', 'd', 'D']
	reverse_move = {0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,8:9,9:8,10:11,11:10}

	def __init__(self):
		self.cube = self.valid_cube_generation()
		self.moveList = []
		self.root = Tk()
		self.root.title("Rubik's cube Solver")

		self.canvas = Canvas(width=960, height=640, background='#808080')

		image1 = Image.open("New folder/3.jpg")
		test = ImageTk.PhotoImage(image1)
		self.canvas.create_image(0, 0, image=test, anchor='nw')
		for i in range(6):
			print(self.cube[i])
		self.display(self.cube)
		self.root.bind("<Enter>",self.enter)
		self.root.bind("<Key>",self.button_click_event)
		
	def maybe(self):

		self.canvas.pack()
		self.root.mainloop()
		

	def enter(self,event):
		self.display(self.cube)

	def valid_cube_generation(self):
		c = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]
		for i in range(6):
			for j in range(3):
				for k in range(3):
					c[i][j][k]=i

		return c		

	def rotate_up_clock(self):
		#phase(clockwise)  verified
		self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2], self.cube[3][1][2], self.cube[3][0][2], self.cube[3][0][1] = self.cube[3][0][2], self.cube[3][0][1], self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2], self.cube[3][1][2]


		self.cube[0][2][0], self.cube[0][1][0], self.cube[0][0][0], self.cube[4][2][0], self.cube[4][1][0], self.cube[4][0][0], self.cube[1][2][0], self.cube[1][1][0], self.cube[1][0][0], self.cube[2][2][0], self.cube[2][1][0], self.cube[2][0][0] = self.cube[2][2][0], self.cube[2][1][0], self.cube[2][0][0], self.cube[0][2][0], self.cube[0][1][0], self.cube[0][0][0], self.cube[4][2][0], self.cube[4][1][0], self.cube[4][0][0], self.cube[1][2][0], self.cube[1][1][0], self.cube[1][0][0]		
		# for i in range(3):
		# 	for j in range(3):
		# 		print(self.color_box[self.cube[3][i][j]] , end = " ")
		# 	print("")
		# print("")
		

	def rotate_down_clock(self):
		# phase(anti-clockwise) verified
		self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2], self.cube[5][1][2], self.cube[5][0][2], self.cube[5][0][1] = self.cube[5][0][2], self.cube[5][0][1], self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2], self.cube[5][1][2]

		self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2], self.cube[4][2][2], self.cube[4][1][2], self.cube[4][0][2], self.cube[1][2][2], self.cube[1][1][2], self.cube[1][0][2], self.cube[2][2][2], self.cube[2][1][2], self.cube[2][0][2] = self.cube[4][2][2], self.cube[4][1][2], self.cube[4][0][2], self.cube[1][2][2], self.cube[1][1][2], self.cube[1][0][2], self.cube[2][2][2], self.cube[2][1][2], self.cube[2][0][2], self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2]	
		 

	def rotate_up_anti(self):
		self.rotate_up_clock()
		self.rotate_up_clock()
		self.rotate_up_clock()
		 

	def rotate_down_anti(self):
		self.rotate_down_clock()
		self.rotate_down_clock()
		self.rotate_down_clock()
		 

	def rotate_right_anti(self):
		self.rotate_right_clock()
		self.rotate_right_clock()
		self.rotate_right_clock()
		 

	def rotate_left_anti(self):
		self.rotate_left_clock()
		self.rotate_left_clock()
		self.rotate_left_clock()
		 

	def rotate_right_clock(self):
		
		self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2], self.cube[2][1][2], self.cube[2][0][2], self.cube[2][0][1] = self.cube[2][0][2], self.cube[2][0][1], self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2], self.cube[2][1][2]

		self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2], self.cube[1][0][2], self.cube[1][0][1], self.cube[1][0][0], self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2] = self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2], self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], self.cube[3][2][0], self.cube[3][2][1], self.cube[3][2][2], self.cube[1][0][2], self.cube[1][0][1], self.cube[1][0][0]
		 

	def rotate_left_clock(self):
		
		self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0], self.cube[4][2][1], self.cube[4][2][2], self.cube[4][1][2], self.cube[4][0][2], self.cube[4][0][1] = self.cube[4][0][2], self.cube[4][0][1], self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0], self.cube[4][2][1], self.cube[4][2][2], self.cube[4][1][2]

		self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2], self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0], self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2] = self.cube[3][0][0], self.cube[3][0][1], self.cube[3][0][2], self.cube[1][2][2], self.cube[1][2][1], self.cube[1][2][0], self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2], self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2]
		 

	def rotate_front_anti(self):
		self.rotate_front_clock()
		self.rotate_front_clock()
		self.rotate_front_clock()
	

	def rotate_back_anti(self):
		self.rotate_back_clock()
		self.rotate_back_clock()
		self.rotate_back_clock()

	def rotate_front_clock(self):
		
		self.cube[0][0][0], self.cube[0][1][0], self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2], self.cube[0][0][1] = self.cube[0][0][2], self.cube[0][0][1], self.cube[0][0][0], self.cube[0][1][0], self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], self.cube[0][1][2]

		self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2], self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0], self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0] = self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], self.cube[4][2][2], self.cube[4][2][1], self.cube[4][2][0], self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0], self.cube[2][0][0], self.cube[2][0][1], self.cube[2][0][2]
		
		# for a in range(3):
		

	def rotate_back_clock(self):
		
		temp = self.cube[1][0][0]
		self.cube[1][0][0], self.cube[1][2][0], self.cube[1][2][2], self.cube[1][0][2] = self.cube[1][0][2], self.cube[1][2][2], self.cube[1][2][0], temp
		temp = self.cube[1][1][0]
		self.cube[1][1][0], self.cube[1][0][1], self.cube[1][1][2], self.cube[1][2][1] = self.cube[1][0][1], self.cube[1][1][2], self.cube[1][2][1], temp
		
		# for a in range(3):
		temp,temp1,temp2 = self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0]
		self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0] = self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0]
		self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0] = self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2]
		self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2] = self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2]
		self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2] = temp,temp1,temp2
		 

		

	def move(self,move):
		if not __debug__:
			self.canvas.create_text(((10), (10)), font="10",anchor = "nw",text=f"{' '.join([str(i) for i in self.moveList])}")
		if move == 'f':
			self.rotate_front_clock()
		elif move == 'F':
			self.rotate_front_anti()
		elif move == 'b':
			self.rotate_back_clock()
		elif move == 'B':
			self.rotate_back_anti()
		elif move == 'u':
			self.rotate_up_clock()
		elif move == 'U':
			self.rotate_up_anti()
		elif move == 'l':
			self.rotate_left_clock()
		elif move == 'L':
			self.rotate_left_anti()
		elif move == 'r':
			self.rotate_right_clock()
		elif move == 'R':
			self.rotate_right_anti()
		elif move == 'd':
			self.rotate_down_clock()
		elif move == 'D':
			self.rotate_down_anti()
		# self.display(self.cube)


	def box_in_cube(self,x,y,c):
		self.canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff", fill=self.color_box[c], width=5)

	def side_displayer(self,x,y,c):
		for i1 in range(3):
			for j1 in range(3):
				self.box_in_cube((x+50*i1),(y+50*j1),c[i1][j1])
				if not bool(__debug__) :
					self.canvas.create_text(((x+50*i1), (y+50*j1)), text=f"{i1},{j1}")

	def display(self,cube):
		for i in range(6):
			if cube[i][1][1] == 0:
				#Front  White
				self.side_displayer(250,250,cube[i])
			elif cube[i][1][1] == 1:
				#Back  Yellow
				self.side_displayer(700,250,cube[i])
			elif cube[i][1][1] == 2:
				#Right Green
				self.side_displayer(400,250,cube[i])			
			elif cube[i][1][1] == 3:
				#Top Blue
				self.side_displayer(250,100,cube[i])
			elif cube[i][1][1] == 4:
				#Left Red
				self.side_displayer(100,250,cube[i])
			else:
				#Bottom Orange
				self.side_displayer(250,400,cube[i])


	def button_click_event(self,event):
		move = event.char
		self.moveList.append(move)
		self.move(move)
		self.display(self.cube)


if __name__ == "__main__":
	c = Rubik()
	c.maybe()
