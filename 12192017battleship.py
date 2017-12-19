# lets give it a shot
from tkinter import *
import random

class battleship():
    
    ''' A battleship game'''
    
    def __init__(self):
        '''boards, display '''
        # two internal boards represantation
        # one is command room
        # other is radar

        self.commandroom=[]
        for i in range(0,11):
                temp=[i]
                if i==0:
                    for element in 'ABCDEFGHIJ':
                        temp.append(element)
                    self.commandroom.append(temp)
                else:
                    temp=[i]
                    for j in range(0,10):
                        temp.append(0)
                    self.commandroom.append(temp)
        self.radar=[]
        for i in range(0,11):
                temp=[i]
                if i==0:
                    for element in 'ABCDEFGHIJ':
                        temp.append(element)
                    self.radar.append(temp)
                else:
                    temp=[i]
                    for j in range(0,10):
                        temp.append(0)
                    self.radar.append(temp)
        #we have our internal empty boards
        #first is command
        self.window = Tk()
        self.window.title('Command Room')
        # Create a canvas within the window to draw on.
        self.canvas = Canvas(self.window, width = 11*50, height = 11*50, bg='white')
        self.canvas.pack()
        # Draw the grid on the canvas.
        for i in range(11):
            for j in range(11):
                self.canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50)
        # Focus the mouse on the canvas.
        self.canvas.focus_set()

        #then i will iterate through the spaces and somehow throw the letter up on the board
        for i in range(11):
            for j in range(11):
               self.canvas.create_text(j*50+25, i*50+25, text=str(self.commandroom[i][j]).upper())

        self.canvas.bind("<Button-1>", self.placeYourShips)
        #bing button 2 to the init
        # we need to innitialize the internal boards for both screens.
        self.initCommandRoom()

        #now lets do this whole thing again only for the radar
        self.window1 = Tk()
        self.window1.title('Radar')
        # Create a canvas within the window to draw on.
        self.canvas1 = Canvas(self.window1, width = 11*50, height = 11*50, bg='white')
        self.canvas1.pack()
        # Draw the grid on the canvas.
        for i in range(11):
            for j in range(11):
                self.canvas1.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50)
        # Focus the mouse on the canvas.
        self.canvas1.focus_set()

        #then i will iterate through the spaces and somehow throw the letter up on the board
        for i in range(11):
            for j in range(11):
               self.canvas1.create_text(j*50+25, i*50+25, text=str(self.radar[i][j]).upper())

        self.canvas1.bind("<Button-1>", self.PlayGame)
        # we need to innitialize the internal boards for both screens.
        self.initRadar()
        self.displayDict={'A':self.A,'B':self.B,'C':self.D,'D':self.D,'E':self.E,'V':self.V,'W':self.W,'X':self.X,'Y':self.Y,'Z':self.Z}
    def updateCommandRoom(self):

        for i in range(11):
            for j in range(11):
                self.canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill='white') 
        #then i will iterate through the spaces and somehow throw the letter up on the board
        for i in range(11):
            for j in range(11):
                #if its one of our letters
                if str(self.commandroom[i][j])in '012345678910':
                    self.canvas.create_text(j*50+25, i*50+25, text=str(self.commandroom[i][j]).upper())
                else:
                    #need to deal with hits and misses
                    # if it's an eleven
                    if self.commandroom[i][j]==11:
                            self.canvas.create_text(j*50+25, i*50+25, text='X', fill='blue')
                    elif str(self.commandroom[i][j]) in 'abcde':#it's a hit and it will be a lower case abcde
                           self.canvas.create_text(j*50+25, i*50+25, text='X', fill='red') 
                    else:
                        self.canvas.create_text(j*50+25, i*50+25, text=str(self.commandroom[i][j]).upper(), fill='green')

    #init the radar
    def updateRadar(self):
        #wipe it all with rectangles
        for i in range(11):
            for j in range(11):
                self.canvas1.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill='white')
        # the code for a hit will be a vwxyz
        # a miss will be 11
        for i in range(11):
            for j in range(11):
                #if it's vwxyz
                if str(self.radar[i][j]) in 'vwxyz':
                    self.canvas1.create_text(j*50+25, i*50+25, text='X', fill='red')
                else:
                    #if its a miss then a blue x
                    if str(self.radar[i][j])=='11':
                        self.canvas1.create_text(j*50+25, i*50+25, text='X', fill='blue')
                    # a ship that hasnt been hit or if its just a 0 it will be a 0
                    if str(self.radar[i][j])=='0' or str(self.radar[i][j]) in 'VWXYZ':
                        self.canvas1.create_text(j*50+25, i*50+25, text='0')
                    #if its 1/10 or A-J itll be that
                    if str(self.radar[i][j]) in '012345678910ABCDEFGHIJ':
                        self.canvas1.create_text(j*50+25, i*50+25, text=str(self.radar[i][j]))
                    


    #lets init the command room
    def initCommandRoom(self):
        '''innitialize the command room '''
        #create 5 objects of class ship
        self.A=ship(size=5,name='Carrier',display='A')
        self.B=ship(size=4,name='Battleship',display='B')
        self.C=ship(size=3,name='Cruiser',display='C')
        self.D=ship(size=3,name='Sub',display='D')
        self.E=ship(size=2,name='Destroyer',display='E')
        self.shiptoplace=[self.A,self.B,self.C,self.D,self.E]
        self.shipsdestroyed=0
        #put em in a list
    def placeYourShips(self,event):
        if len(self.shiptoplace)==0:
            print('No More Ships to Place')
            return 'No More To Place.'
        # manage the event
        row = event.y//50
        col = event.x//50
        

        #make sure the space is empty
        if self.commandroom[row][col]==0:
            #decide which ship placing
            # it will go in decreasing order in length
            ashiptoplace=self.shiptoplace[0]
            print('Place Your '+ashiptoplace.name)
            #find our directions

            #we will do two steps
            #first will consider the size of the ship and how close the ship is to an edge
            #make an empty list and then add the possible directions to it
            directionList=[]

            #you can go up
            if (ashiptoplace.size)<=row:
                directionList.append('UP')
            #can go down
            if row+(ashiptoplace.size)<11:
                directionList.append('DOWN')
            #can go left
            if col+(ashiptoplace.size)<=11:
                directionList.append('RIGHT')
            if ashiptoplace.size<=col:
                directionList.append('LEFT')

            #go through each direction and remove the direction if there is a ship in it's potential path
            #make sure it isnt landlocked
            if len(directionList)==0:
                return None
            else:
                if 'UP' in directionList:
                    #set a var to 0 if we increse it by 1 everytime we hit a ship
                    space=0
                    for i in range(1,ashiptoplace.size+1):
                        if self.commandroom[row-i][col]!=0: #if we hit something besides a ship
                            space+=1
                    if space>0: #we got to remove the direction
                        directionList.remove('UP')
                        
                if 'DOWN' in directionList:
                    space=0
                    for i in range(1,ashiptoplace.size+1):
                        if self.commandroom[row+i][col]!=0:
                            space+=1
                    if space>0:
                        directionList.remove('DOWN')

                if 'RIGHT' in directionList:
                    space=0
                    for i in range(1,ashiptoplace.size+1):
                        if self.commandroom[row][col+i]!=0:
                            size+=1
                    if space>0:
                        directionList.remove('RIGHT')

                if 'LEFT' in directionList:
                    space=0
                    for i in range(1,ashiptoplace.size+1):
                        if self.commandroom[row][col-i]!=0:
                            space+=1
                    if space>0:
                        directionList.remove('LEFT')

            #print all directions to shell for user to decide

            #check once more to see if it's gridlocked
            if len(directionList)==0:
                return None
            else:
                for element in directionList:
                    print(element)
        #if the square is full we need to get out of here
        else:
            return None
        #manage our input
        direction=input('Which Direction?' ).upper()
        if direction=='UP':
            for i in range(ashiptoplace.size):
                #change self.commandroom
                #command room
                self.commandroom[row-i][col]=ashiptoplace.display

                #window
                #self.canvas.create_text(row-i*50+25, col*50+25, text=self.commandroom[row-i][col].upper(), fill='green')
        if direction=='DOWN':
            for i in range(ashiptoplace.size):
                self.commandroom[row+i][col]=ashiptoplace.display
        if direction=='LEFT':
            for i in range(ashiptoplace.size):
                self.commandroom[row][col-i]=ashiptoplace.display
        if direction=='RIGHT':
            for i in range(ashiptoplace.size):
                self.commandroom[row][col+i]=ashiptoplace.display
        #update the window    
        
        self.updateCommandRoom()
        #remove the ship from ship place list
        G=self.shiptoplace.pop(0)
    #init the radar
    def initRadar(self):
        #same thing as initCommandRoom
        self.V=ship(size=5,name='Carrier',display='V')
        self.W=ship(size=4,name='Battleship',display='W')
        self.X=ship(size=3,name='Cruiser',display='X')
        self.Y=ship(size=3,name='Sub',display='Y')
        self.Z=ship(size=2,name='Destroyer',display='Z')
        self.shiptoplace1=[self.V,self.W,self.X,self.Y,self.Z]
        self.shipstodestroy=0
        
        #lets place the ships to with a random thing
        
        for element in self.shiptoplace1:
            validToPlace=False
            while validToPlace==False: 
                row=random.randint(1,10)
                col=random.randint(1,10)
                #empty space first
                if self.radar[row][col]==0:
                    
                    
                    #will be for possible directions
                    possibleDirections=[]
                    #you can go up
                    if (element.size)<row:
                        clear=True
                        for i in range(element.size):
                            if self.radar[row-i][col]!=0:
                                clear=False
                        if clear==True:
                            possibleDirections.append('UP')
                    #can go down
                    if row+(element.size)<11:
                        clear=True
                        for i in range(element.size):
                            if self.radar[row+i][col]!=0:
                                clear=False
                        if clear==True: 
                            possibleDirections.append('DOWN')
                    #can go left
                    if col+(element.size)<11:
                        
                        vclear=True
                        for i in range(element.size):
                            if self.radar[row][col+i]!=0:
                                clear=False
                        if clear==True: 
                            possibleDirections.append('RIGHT')
                    if col-element.size>0:
                        clear=True
                        for i in range(element.size):
                            if self.radar[row][col-i]!=0:
                                clear=False
                        if clear==True: 
                            possibleDirections.append('LEFT')

                    #make sure there is a direction
                    if len(possibleDirections)>0:
                        #randomly choose a direction
                        direction=random.choice(possibleDirections)
                        #apply the change to radar

                        
                        if direction=='UP':
                            for i in range(element.size):
                                #change self.commandroom
                                #command room
                                self.radar[row-i][col]=element.display
                        if direction=='DOWN':
                            for i in range(element.size):
                                self.radar[row+i][col]=element.display
                        if direction=='LEFT':
                            for i in range(element.size):
                                self.radar[row][col-i]=element.display
                        if direction=='RIGHT':
                            for i in range(element.size):
                                self.radar[row][col+i]=element.display
                        #now update the radar window
                        #self.updateRadar()
                        validToPlace=True
        self.updateRadar()

    def PlayGame(self,event):
        #starts with you pressing on radar
        row = event.y//50
        col = event.x//50
        
        #user
        #if it's a hit
        #detract life of thing
        #if life=0 print a message
        if str(self.radar[row][col]) in 'VWXYZ':
            #dicrease life
            self.displayDict[str(self.radar[row][col])].life-= 1
            if self.displayDict[str(self.radar[row][col])].life== 0:
                print('You Destroyed a '+self.displayDict[str(self.radar[row][col])].name)
                self.shipstodestroy+=1
                if self.shipstodestroy==5:
                    return('YOU WIN!')
                        
            #set the radar to a hit
            self.radar[row][col]=self.displayDict[str(self.radar[row][col])].display.lower()
                
        #else change to a miss= 11
        else:
            self.radar[row][col]=11

        #update both
        self.updateCommandRoom()
        self.updateRadar()

        #next the random move

        #need a not hit space
        full=True
        while full==True:
            row=random.randint(1,10)
            col=random.randint(1,10)
            if str(self.commandroom[row][col]) not in '11abcde':
                full=False
                #it hasnt been hit we can use this mark
        #if it's a hit
        #detract life of thing
        #if life=0 print a message
        if str(self.commandroom[row][col]) in 'ABCDEabcde':
            #dicrease life
            self.displayDict[str(self.commandroom[row][col])].life-= 1
            #set it to lower case
            self.commandroom[row][col]=self.commandroom[row][col].lower()
            if self.displayDict[str(self.commandroom[row][col]).upper()].life== 0:
                print('Your '+self.displayDict[str(self.commandroom[row][col]).upper()].name+' was destroyed')
                self.shipsdestroyed+=1
                if self.shipsdestroyed==5:
                    return('YOU LOSE!')

        #set the commandroom to a hit
            self.commandroom[row][col]=self.displayDict[str(self.commandroom[row][col]).upper()].display.lower()
                
        #else change to a miss= 11
        else:
            self.commandroom[row][col]=11
        self.updateRadar()
        self.updateCommandRoom()
        
class ship():
    def __init__(self,name,size,display):
        self.name=name # the name of the ship
        self.size=size # size of the ship
        self.life=size # how many lives the ship will have
        self.display=display #what the ship will display on board as name

if __name__ == "__main__":
    battleship()
    
        
            

        

    
    
