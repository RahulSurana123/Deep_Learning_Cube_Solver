#!/usr/bin/env python
# coding: utf-8

# In[71]:


from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
import numpy as np
from PIL import Image,ImageTk

class Rubik:

    """
    COLOR  : INDEX : FACE
    BLACK  :   0   : FRONT
    YELLOW :   1   : BACK
    GREEN  :   2   : RIGHT
    ORANGE :   3   : UP
    BLUE   :   4   : LEFT
    RED    :   5   : BOTTOM
    """

    #Constants number represent color in self.cube 
    

    def __init__(self):
        self.color_box=['black','yellow','green','orange','blue','red']
        self.edges = [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(4,3),(4,5)]
        self.corners = [(0,2,3),(0,3,4),(0,4,5),(0,2,5),(1,2,3),(1,3,4),(1,4,5),(1,2,5)]
        self.moveCharList = ['f','F', 'b', 'B', 'r', 'R', 'l', 'L', 'u', 'U', 'd', 'D']
#         self.action_space = [0,1,2,3,4,5,6,7,8,9,0,10,11]
        self.reverse_move = {0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,8:9,9:8,10:11,11:10}
        self.temp = self.valid_cube_generation()
        self.cube = self.valid_cube_generation()
        self.cube,y=self.random_data_set_generation(15)
        self.moveList = []
        self.root = Tk()
        self.root.title("Rubik's cube Solver")
        self.moves=0
        self.state=0
        self.canvas = Canvas(width=960, height=640, background='#808080')

        image1 = Image.open("New folder/3.jpg")
        test = ImageTk.PhotoImage(image1)
        self.canvas.create_image(0, 0, image=test, anchor='nw')
        Button(self.canvas, padx=8,text="X",bg='grey', command=self.root.destroy).place(x=50,y=50)
        self.display(self.cube)
#         self.play_step()
        self.root.bind("<Key>",self.button_click_event)
        self.canvas.pack()
        self.root.mainloop()


    def valid_cube_generation(self):
        c = [[[0 for i in range(3)] for j in range(3)]for k in range(6)]
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    c[i][j][k]=i
        return c          

    def random_data_set_generation(self,n):
        moves_Y = []
#         cube_X = []
        while n:     
            m = random.randint(0,11)
            n-=1
            moves_Y.append(self.reverse_move[m])
            self.move(self.moveCharList[m])
#             cube_X.append(np.array(self.cube).flatten())

#         print(moves_Y)
#         self.temp = valid_cube_generation() 
        arr1=np.subtract(np.array(self.cube),np.array(self.temp))
        
        arr2=[np.sum(i) for i in self.temp]
        arr3=[np.sum(i) for i in self.cube]
        arr4=[np.sum(i) for i in arr1]
        ar3=np.subtract(np.array(arr4),np.array(arr2))
        self.state = sum(i for i in ar3 if i > 0)
        print(self.state)

#         self.moves = int("".join([str(int) for int in moves_Y]))
#         print(self.moves)
#         print(type(self.move))

        return self.cube, self.state

    def quit(self):
        self.root.destroy()
        
    def rotate_up_clock(self):
        #phase(clockwise)
        temp,temp1,temp2 = self.cube[3][0][2],self.cube[3][0][1],self.cube[3][0][0]
        self.cube[3][0][2],self.cube[3][0][1],self.cube[3][0][0] = self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2]
        self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2] = self.cube[3][2][0],self.cube[3][2][1],self.cube[3][2][2]
        self.cube[3][2][0],self.cube[3][2][1],self.cube[3][2][2] = self.cube[3][0][0],self.cube[3][1][0],self.cube[3][2][0]
        self.cube[3][0][0],self.cube[3][1][0],self.cube[3][2][0] = temp,temp1,temp2

        # for a in range(3):
        temp,temp1,temp2 = self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0]
        self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0] = self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0]
        self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0] = self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0]
        self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0] = self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0]
        self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0] = temp,temp1,temp2


    def rotate_down_anti(self):
        temp,temp1,temp2 = self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0]
        self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0] = self.cube[5][2][0],self.cube[5][2][1],self.cube[5][2][2]
        self.cube[5][2][0],self.cube[5][2][1],self.cube[5][2][2] =self.cube[5][2][2],self.cube[5][1][2],self.cube[5][0][2]
        self.cube[5][2][2],self.cube[5][1][2],self.cube[5][0][2] = self.cube[5][0][2],self.cube[5][0][1],self.cube[5][0][0]
        self.cube[5][0][2],self.cube[5][0][1],self.cube[5][0][0] = temp,temp1,temp2

        # for a in range(3):
        temp,temp1,temp2 = self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2]
        self.cube[0][0][2],self.cube[0][1][2],self.cube[0][2][2] = self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2]
        self.cube[2][0][2],self.cube[2][1][2],self.cube[2][2][2] = self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2]
        self.cube[1][0][2],self.cube[1][1][2],self.cube[1][2][2] = self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2]
        self.cube[4][0][2],self.cube[4][1][2],self.cube[4][2][2] = temp,temp1,temp2


    def rotate_up_anti(self):
        self.rotate_up_clock()
        self.rotate_up_clock()
        self.rotate_up_clock()


    def rotate_down_clock(self):
        self.rotate_down_anti()
        self.rotate_down_anti()
        self.rotate_down_anti()


    def rotate_right_anti(self):
        self.rotate_right_clock()
        self.rotate_right_clock()
        self.rotate_right_clock()


    def rotate_left_anti(self):
        self.rotate_left_clock()
        self.rotate_left_clock()
        self.rotate_left_clock()


    def rotate_right_clock(self):
        temp,temp1,temp2 =  self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0]
        self.cube[2][0][0],self.cube[2][1][0],self.cube[2][2][0] = self.cube[2][2][0],self.cube[2][2][1],self.cube[2][2][2]
        self.cube[2][2][0],self.cube[2][2][1],self.cube[2][2][2] = self.cube[2][2][2],self.cube[2][1][2],self.cube[2][0][2]
        self.cube[2][2][2],self.cube[2][1][2],self.cube[2][0][2] = self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0]
        self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0] = temp,temp1,temp2


        temp,temp1,temp2 = self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2]
        self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2] = self.cube[3][2][0],self.cube[3][2][1],self.cube[3][2][2]
        self.cube[3][2][0],self.cube[3][2][1],self.cube[3][2][2] = self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0]
        self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0] = self.cube[5][2][0],self.cube[5][2][1],self.cube[5][2][2]
        self.cube[5][2][0],self.cube[5][2][1],self.cube[5][2][2] = temp,temp1,temp2


    def rotate_left_clock(self):

        temp,temp1,temp2 = self.cube[4][0][2],self.cube[4][0][1],self.cube[4][0][0]
        self.cube[4][0][2],self.cube[4][0][1],self.cube[4][0][0] = self.cube[4][2][2],self.cube[4][1][2],self.cube[4][0][2]
        self.cube[4][2][2],self.cube[4][1][2],self.cube[4][0][2] = self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2]
        self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2] = self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0]
        self.cube[4][0][0],self.cube[4][1][0],self.cube[4][2][0] = temp,temp1,temp2

    # for a in range(3):
        temp,temp1,temp2 = self.cube[0][0][0],self.cube[0][0][1],self.cube[0][0][2]
        self.cube[0][0][0],self.cube[0][0][1],self.cube[0][0][2] = self.cube[3][0][0],self.cube[3][0][1],self.cube[3][0][2]
        self.cube[3][0][0],self.cube[3][0][1],self.cube[3][0][2] = self.cube[1][2][2],self.cube[1][2][1],self.cube[1][2][0]
        self.cube[1][2][2],self.cube[1][2][1],self.cube[1][2][0] = self.cube[5][0][0],self.cube[5][0][1],self.cube[5][0][2]
        self.cube[5][0][0],self.cube[5][0][1],self.cube[5][0][2] = temp,temp1,temp2


    def rotate_front_anti(self):

        temp,temp1,temp2 = self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0]
        self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0] = self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2]
        self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2] = self.cube[0][2][2],self.cube[0][1][2],self.cube[0][0][2]
        self.cube[0][2][2],self.cube[0][1][2],self.cube[0][0][2] = self.cube[0][0][2],self.cube[0][0][1],self.cube[0][0][0]
        self.cube[0][0][2],self.cube[0][0][1],self.cube[0][0][0] = temp,temp1,temp2
        # for a in range(3):
        temp,temp1,temp2 = self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0]
        self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0] = self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2]
        self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2] = self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2]
        self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2] = self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0]
        self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0] = temp,temp1,temp2



    def rotate_front_clock(self):

        temp,temp1,temp2 = self.cube[0][0][2],self.cube[0][0][1],self.cube[0][0][0]
        self.cube[0][0][2],self.cube[0][0][1],self.cube[0][0][0] = self.cube[0][2][2],self.cube[0][1][2],self.cube[0][0][2]
        self.cube[0][2][2],self.cube[0][1][2],self.cube[0][0][2] = self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2]
        self.cube[0][2][0],self.cube[0][2][1],self.cube[0][2][2] = self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0]
        self.cube[0][0][0],self.cube[0][1][0],self.cube[0][2][0] = temp,temp1,temp2

        # for a in range(3):
        temp,temp1,temp2 = self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0]
        self.cube[2][0][2],self.cube[2][0][1],self.cube[2][0][0] = self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2]
        self.cube[3][2][2],self.cube[3][1][2],self.cube[3][0][2] = self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2]
        self.cube[4][2][0],self.cube[4][2][1],self.cube[4][2][2] = self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0]
        self.cube[5][0][0],self.cube[5][1][0],self.cube[5][2][0] = temp,temp1,temp2



    def rotate_back_clock(self):
        temp,temp1,temp2 =self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0]
        self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0] = self.cube[1][2][0],self.cube[1][2][1],self.cube[1][2][2]
        self.cube[1][2][0],self.cube[1][2][1],self.cube[1][2][2] = self.cube[1][2][2],self.cube[1][1][2],self.cube[1][0][2] 
        self.cube[1][2][2],self.cube[1][1][2],self.cube[1][0][2] = self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0]
        self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0] = temp,temp1,temp2




        # for a in range(3):
        temp,temp1,temp2 = self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0]
        self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0] = self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0]
        self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0] = self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2]
        self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2] = self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2]
        self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2] = temp,temp1,temp2


    def rotate_back_anti(self):

        temp,temp1,temp2 = self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0]
        self.cube[1][0][0],self.cube[1][1][0],self.cube[1][2][0] = self.cube[1][2][0],self.cube[1][2][1],self.cube[1][2][2]
        self.cube[1][2][0],self.cube[1][2][1],self.cube[1][2][2] = self.cube[1][2][2],self.cube[1][1][2],self.cube[1][0][2]
        self.cube[1][2][2],self.cube[1][1][2],self.cube[1][0][2] = self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0]
        self.cube[1][0][2],self.cube[1][0][1],self.cube[1][0][0] = temp,temp1,temp2


        # for a in range(3):
        temp,temp1,temp2 = self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2]
        self.cube[5][0][2],self.cube[5][1][2],self.cube[5][2][2] = self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2]
        self.cube[4][0][0],self.cube[4][0][1],self.cube[4][0][2] = self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0]
        self.cube[3][2][0],self.cube[3][1][0],self.cube[3][0][0] = self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0]
        self.cube[2][2][2],self.cube[2][2][1],self.cube[2][2][0] = temp,temp1,temp2


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
        elif move == 'q':
            self.root.destroy()
        elif move == 'p':
            self.play_step()
        
    def get_rewards(self,cube):
        rewards=0
        for i in range(6):
            flatten_arr = np.ravel(cube[i])
            result = np.all(cube==i)
            if not result:
                rewards-=1
            else:
                rewards+=1
        return rewards
        
    def box_in_cube(self,x,y,c):
        try:
            self.canvas.create_rectangle(x, y, x+50, y+50, outline="#ffffff", fill=self.color_box[c], width=5)
        except TclError:
            pass

    def side_displayer(self,x,y,c):
        for i1 in range(3):
            for j1 in range(3):
                self.box_in_cube((x+50*i1),(y+50*j1),c[i1][j1])
        if not bool(__debug__) :
            self.canvas.create_text(((x+50*i1), (y+50*j1)), text=f"{i1},{j1}")

    def game_over(self):
        arr = self.valid_cube_generation()
        # np.subtract(self.cube,arr)
        return np.sum(np.absolute(np.array(self.cube)-np.array(arr)))==0

    def display(self,cube):
        for i in range(6):
            if cube[i][1][1] == 0:
                self.side_displayer(250,250,cube[i])
            elif cube[i][1][1] == 1:
                self.side_displayer(700,250,cube[i])
            elif cube[i][1][1] == 2:
                self.side_displayer(400,250,cube[i])
            elif cube[i][1][1] == 3:
                self.side_displayer(250,100,cube[i])
            elif cube[i][1][1] == 4:
                self.side_displayer(100,250,cube[i])
            else:
                self.side_displayer(250,400,cube[i])

        if self.game_over():
            print('if statement')
            Message(self.canvas,text="You've won the game!!!😎",padx=10,pady=30).place(x=800,y=10)

    def button_click_event(self,event):
        move = event.char
        self.moveList.append(move)
        self.move(move)
        self.display(self.cube)
        
    def play_step(self,action):
        move=self.moveCharList[action]
        self.move(move)
        self.display(self.cube)
        reward = self.get_rewards(self.cube)
        
        arr1=np.subtract(np.array(self.cube),np.array(self.temp))
        arr4=[np.sum(i) for i in arr1]
        new_state = sum(i for i in ar3 if i > 0)
#         print(new_state)
        
        
        if self.game_over():
#             done = True
            print('if statement')
            Message(self.canvas,text="You've won the game!!!😎",padx=10,pady=30).place(x=800,y=10)
#             break
        
            
        return new_state, reward, done

    
    

if __name__ == "__main__":
    c = Rubik()


# In[78]:


action_size = 12
state_size = 136
qtable = np.zeros((state_size, action_size))

total_episodes = 100000        # Total episodes
learning_rate = 0.8           # Learning rate
max_steps = 150                # Max steps per episode
gamma = 0.95                  # Discounting rate

# Exploration parameters
epsilon = 1.0                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability 
decay_rate = 0.005 


# In[ ]:


rewards = []

# 2 For life or until learning is stopped
for episode in range(total_episodes):
    # Reset the environment
    t = c.valid_cube_generation()
    c.cube, state=c.random_data_set_generation(15)
#     state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)
        
        ## If this number > greater than epsilon --> exploitation (taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])

        # Else doing a random choice --> exploration
        else:
#             action = c.action_space.sample()
            action = random.choice(range(12))

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done = c.play_step(action)

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        
        total_rewards += reward
        
        # Our new state is state
        state = new_state
        
        # If done (if we're dead) : finish episode
        if done == True: 
            break
        
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    rewards.append(total_rewards)

print ("Score over time: " +  str(sum(rewards)/total_episodes))
print(qtable)


# In[ ]:





# In[ ]:





# In[ ]:




