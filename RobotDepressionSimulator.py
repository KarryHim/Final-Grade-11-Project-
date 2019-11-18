##########################################################################################################



##      ##             ####             ########      ########    ##          ## 
##      ##            ##  ##            ##     ##     ##     ##    ##        ##
##      ##           ##    ##           ##      ##    ##      ##    ##      ##
##      ##          ##      ##          ##     ##     ##     ##      ##    ##   
##########         ############         ##    ##      ##    ##        ##  ##    
##########        ##############        #######       #######          ####   
##      ##       ##            ##       ##   ##       ##   ##           ##
##      ##      ##              ##      ##     ##     ##     ##         ##
##      ##     ##                ##     ##      ##    ##      ##        ##
##      ##    ##                  ##    ##       ##   ##       ##       ##            



##     ##    
##    ##         
##   ##         
##  ##            
####             
####                      
##  ##              
##   ##            
##    ##    ##        
##     ##   ##



#Final Gaming Project#

#Coded by: Harry Kim

#Class: ICS 3UI

#Finish Date: June 16, 2019

#Robot Depression Simulator

#~Only people who don't recycle can read this~#

# --------------------------------------------#

#If you can read what is written above, you are a trUe c0DinG b055

#############################################################################################################


from tkinter import *
from time import *
from math import *
from random import *
import winsound 


root = Tk()
s = Canvas(root, width = 1300, height = 900, background = 'grey10')
s.pack()

#Called once at the start of the game.     
def setInitialValues():
    global factoryIntegrity, xMouse, yMouse, xRobotspeed, yRobotspeed, maxDepression, difficulty, robotDepression
    global xRobot, yRobot, robotImage, robotPopulation, factoryExfists, factoryWeak, timeReal, timeInitial, gameEnd, gameIntro
    global happyPoints, time, factoryIntegrity, factoryValue, robotDrawing, robotDepressiondrawing, robotDepressionremaining
    global happyBot, sadBot, musicList, robotRepair 
    global introscr, introtext, introtext2, introX, introY, difficultyBoxes, difficultyColours, difficultyText, difficultyTextbox, distance 

    #Setting Initial Values. These will be used later. 

    factoryValue = 0
    timeInitial = 0
    timeReal = 0
    happyPoints = 0  # :D  :DDDDD
    robotRepair = 0

    happyBot = PhotoImage(file = 'Happy.gif')
    sadBot = PhotoImage(file = 'Sad.gif')
    
    
    factoryIntegrity = 100
    xMouse = 0
    yMouse = 0
    xRobotspeed = []
    yRobotspeed = []
    score = 0
    xRobot = []
    yRobot = []
    robotDepression = []
    maxdepression = 0
    robotPopulation = 30


    gameEnd = False 
    gameIntro = True     
    
    difficulty = 0
    robotDrawing = []
    robotDepressiondrawing = []
    robotDepressionremaining = []

    musicList = ['Sovngarde.wav', 'ScarletForest.wav','HeavenSent.wav','Mars_The_Bringer_of_War.wav', 'UndyneGeno.wav', 'Megalovania.wav'] #Objectively the best soundtrack for anygame in
                                                                                                                                           #ICS 3UI. Approved by Harry Kim.  

    introscr = s.create_rectangle(0,0,1300,900, fill = 'black')
    introtext = s.create_text(650,100, fill = 'white', text = 'Robot Depression Simulator', font = 'FixedSys  50')
    introtext2 = s.create_text(650,200, fill = 'white', text = 'Select Difficulty. Please Turn On the Sound! Normal mode is Recommended.', font = 'FixedSys  20')

    introX = []
    introY = []
    difficultyBoxes = [0,0,0,0,0,0]
    difficultyColours =['#091dba', '#00c3ff', '#1dad3a', '#bbd611', '#d67a11', '#d61111']
    difficultyText = ['Easy', 'Normal', 'Hard', 'Extreme', 'Insane', 'Genocide ']
    difficultyTextbox = [0,0,0,0,0,0]

    
    distance = 100

    #Empty arrays that will be used later.      
    for i in range(robotPopulation):
        robotDrawing.append(0)
        robotDepressiondrawing.append(0)
        robotDepressionremaining.append(0)


    


#Called at the beginning of the game. 
def createBackground():
    global difficulty, musicList
    

    #The Path. 
    path1 = s.create_rectangle(1050, 400, 1300, 500, fill = 'white', outline = 'white')
    path2 = s.create_rectangle(1150, 400, 1050, 150, fill = 'white', outline = 'white')
    path3 = s.create_rectangle(800, 150, 1050, 250, fill = 'white', outline = 'white')
    path4 = s.create_rectangle(800, 250, 900, 700, fill = 'white', outline = 'white')
    path5 = s.create_rectangle(600, 700, 900, 800, fill = 'white', outline = 'white')
    path6 = s.create_rectangle(600, 800, 500, 100, fill = 'white', outline = 'white')
    path7 = s.create_rectangle(500, 100, 250, 200, fill = 'white', outline = 'white')
    path8 = s.create_rectangle(250, 200, 350, 500, fill = 'white', outline = 'white')
    path9 = s.create_rectangle(50, 400, 250, 500, fill = 'white', outline = 'white')
    path10 = s.create_rectangle(50, 400, 150, 600, fill = 'white', outline = 'white')

    s.create_text(200,650, text = 'Factory', fill = 'white')

    #Factory Drawing
        
    factoryDrawing = s.create_rectangle(50,600 , 450,850, fill = '#E7E578')
    s.create_text(250,650, fill = 'black', text = 'Factory', font = 'FixedSys  30')
    

    #Plays music depending on the difficulty. 
    music = winsound.PlaySound(musicList[difficulty], winsound.SND_ASYNC)
        
    


#Called every frame to display score, time, etc.        
def displayStuff():
    global factoryIntegrity, xMouse, yMouse, xRobotspeed, yRobotspeed, maxDepression, difficulty, robotDepression
    global xRobot, yRobot, robotImage, robotPopulation, factoryIntegrityonscreen
    global happyPoints, time, factoryIntegrity, happyText, timePassed, timeText, timeReal
    global happy, stringT

    #Such that factory quality cannot go higher than 100
    while factoryIntegrity > 100:
        factoryIntegrity -= 1
        
    noob = (str(floor(factoryIntegrity))) + '%' #Factory Quality Percentage

    happy = (str(happyPoints)) #How many bots you've made happy! 
    stringT = str(timeReal) #How much time that has elapsed 

    timeText = s.create_text(900, 25, text = 'Time Passed: ' + ' ' + stringT, fill = 'red', font = 'FixedSys 20')
    
    happyText = s.create_text(900,75, text = 'Happy Points: ' + ' ' + happy, fill = 'red', font = 'FixedSys 20')
    
    factoryIntegrityonscreen = s.create_text(900, 125 , text = 'Factory Quality Percentage :' + ' ' + noob, fill = 'red', font = 'FixedSys 20') 




    
#Gets Called ONCE at the Start of the Game to set robot values based on difficulty. 
def difficultyValues():
    #Difficulties Set to 0: Easy, 1: Medium,  2: Hard, 3: Extreme, 4: Insane, 5: Genocide. 

    global factoryIntegrity, xMouse, yMouse, xRobotspeed, yRobotspeed, maxDepression, difficulty, robotStrength 
    global time, score, xRobot, yRobot, robotImage, robotPopulation, robotDepression, robotRepair 

    
    if difficulty == 0: #Easy difficulty 
        robotPopulation = 22
        maxDepression = 3
        
        for i in range(robotPopulation):
            robotDepression.append(3) #How much it takes to reduce the robot's depresion. 
            xRobotspeed.append(1.5) #The speed of the Robot 
            yRobotspeed.append(xRobotspeed[i]) #The Y speed of the robot. (Identical to the X speed.) 
            robotStrength = factoryIntegrity/20 #Allows factory to take 20 hits.
            robotRepair = 10


    elif difficulty == 1: #Normal difficulty
        maxDepression = 5
        robotPopulation = 15
        
        for i in range(robotPopulation):
            robotDepression.append(5) 
            xRobotspeed.append(2.5)
            yRobotspeed.append(xRobotspeed[i])
            robotStrength = factoryIntegrity/15 #Allows 15 hits.
            robotRepair = 8

    elif difficulty == 2: #Hard difficulty
        maxDepression = 6
        robotPopulation = 17
        
        for i in range(robotPopulation):
            robotDepression.append(6)
            xRobotspeed.append(4.5)
            yRobotspeed.append(xRobotspeed[i])
            robotStrength = 8
            robotRepair = 5

    elif difficulty == 3: #Extreme Difficulty
        maxDepression = 7
        robotPopulation = 13
        
        for i in range(robotPopulation):
            robotDepression.append(7)
            xRobotspeed.append(5)
            yRobotspeed.append(xRobotspeed[i])
            robotStrength = 10
            robotRepair = 3

            
    elif difficulty == 4: #Insane Difficulty 
        maxDepression = 10
        robotPopulation = 15

        for i in range(robotPopulation):
            robotDepression.append(10)
            xRobotspeed.append(6.5)
            yRobotspeed.append(xRobotspeed[i])
            robotStrength = 15
            robotRepair = 1

        
    elif difficulty == 5: #Genocide Difficulty - Are you insane??? 
        factoryIntegrity == 1
        maxDepression = 8
        robotPopulation = 20
        robotRepair = 0 
        
        for i in range(robotPopulation):       
            robotDepression.append(8)
            xRobotspeed.append(10)
            yRobotspeed.append(10)

            robotStrength = 1  #Special mode: Factory does not heal, but the robots only reduce the quality by 1. However, the robots are much more depressed. (and faster) 

    else:
        pass

    for i in range(robotPopulation): #If the robot is killed or leaves the screen, recycle the bot instead of creating a new one... 
        #Thus, it reduces the load on the computer! However, there will be a maximum number of robots that can appear at a time.
    
        xRobot.append(randint(1300,4000))
        yRobot.append(450)
        




#Called Every Frame. Draws the factory Depending on its Integrity. 
def drawfactory():
    global xRobot, yRobot, robotImage, factoryIntegrity, robotPopulation, factoryValue, factoryHealthremaining, factoryIntegrityvalue, factoryHealth

    factoryIntegrityvalue = factoryIntegrity * 3    
    factoryHealth = s.create_rectangle(100,725 , 400,775, fill = 'black')
    factoryHealthremaining = s.create_rectangle(100,725, 100 + factoryIntegrityvalue ,775, fill = 'green') 



    


#Called every frame. 
def updateObjects():
    
    global factoryIntegrity, xMouse, yMouse, xRobotspeed, yRobotspeed, hit
    global time, score, xRobot, yRobot, robotImage, robotPopulation, robotDepression 
                
    for i in range(robotPopulation):


        #Y value Increments (When the Robots are moving up/down. 
        if 1050 <= xRobot[i] <= 1150 and 250 <= yRobot[i] < 400:
            yRobot[i] -= yRobotspeed[i]

        elif 800 <= xRobot[i] <= 900 and 250 <= yRobot[i] <= 700:
            yRobot[i] += yRobotspeed[i]

        elif 500 <= xRobot[i] <= 600 and 200 <= yRobot[i] <= 700:
            yRobot[i] -= yRobotspeed[i]

        elif 250 <= xRobot[i] <= 350 and 200 <= yRobot[i] <= 400:
            yRobot[i] += yRobotspeed[i]

        elif 50 <= xRobot[i] <= 150 and 500 <= yRobot[i] <= 600:
            yRobot[i] += yRobotspeed[i]

            
        #X value increments (When Robots are moving left)
            
        elif 1150 < xRobot[i] and 400 <= yRobot[i] <= 500:
            xRobot[i] -= xRobotspeed[i]

        elif 900 <= xRobot[i] <= 1050 and 150 <= yRobot[i] <= 250:
            xRobot[i] -= xRobotspeed[i]

        elif 600 <= xRobot[i] <= 800 and 700 <= yRobot[i] <= 800:
            xRobot[i] -= xRobotspeed[i]

        elif 350 <= xRobot[i] <= 500 and 100 <= yRobot[i] <= 200:
            xRobot[i] -= xRobotspeed[i]

        elif 150 <= xRobot[i] <= 250 and 400 <= yRobot[i] <= 500:
            xRobot[i] -= xRobotspeed[i]


            
        #Both value increments (When both values are affected) 
        elif 1050 <= xRobot[i] <= 1150 and 400 <= yRobot[i] <= 500:
            yRobot[i] -= yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 1050 <= xRobot[i] <= 1150 and 150 <= yRobot[i] <= 250:
            yRobot[i] -= yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 800 <= xRobot[i] <= 900 and 700 <= yRobot[i] <= 800:
            yRobot[i] += yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 800 <= xRobot[i] <= 900 and 150 <= yRobot[i] <= 250:
            yRobot[i] += yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 500 <= xRobot[i] <= 600 and 700 <= yRobot[i] <= 800:
            yRobot[i] -= yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 500 <= xRobot[i] <= 600 and 100 <= yRobot[i] <= 200:
            yRobot[i] -= yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 250 <= xRobot[i] <= 350 and 100 <= yRobot[i] <= 200:
            yRobot[i] += yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 250 <= xRobot[i] <= 350 and 400 <= yRobot[i] <= 500:
            yRobot[i] += yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]

        elif 50 <= xRobot[i] <= 150 and 400 <= yRobot[i] <= 500:
            yRobot[i] += yRobotspeed[i]
            xRobot[i] -= xRobotspeed[i]


        elif 50 <= xRobot[i] <= 450 and 600 <= yRobot[i] <= 850:
            hit = i
            factoryHit()

        else:
            pass






    

#Called every frame. 
def drawRobot():
    global xRobot, yRobot, robotPopulation, robotDepression, maxDepression, robotDrawing, robotDepressiondrawing, robotDepressionremaining, happyPoints
    global healthPercentage, trueLength, happyBot, sadBot 

    #Drawing the robot.     
    for i in range(robotPopulation):
        if robotDepression[i] == 0:
            robotDrawing[i] = s.create_image(xRobot[i],yRobot[i], anchor = CENTER, image = happyBot) #If the robot is happy, a happy bot is drawn. 
             
        else:           
            healthPercentage = robotDepression[i] / maxDepression    #Calculates the depression percentage of the robot for each index. 
            trueLength =  20 * healthPercentage #The Percentage equivalent for 20.            
            nib = trueLength - 10

            robotDrawing[i] = s.create_image(xRobot[i],yRobot[i], anchor = CENTER, image = sadBot) #If the robot is depressed, a sad bot is drawn. 
            
            robotDepressiondrawing[i] = s.create_rectangle(xRobot[i]-10, yRobot[i]-40, xRobot[i]+10, yRobot[i]-30, fill = 'red') #Max health
            robotDepressionremaining[i] = s.create_rectangle(xRobot[i]-10, yRobot[i]-40, xRobot[i] + nib, yRobot[i]-30, fill ='green') #The drawing of the actual health. As health decreases,
                                                                                                                                        #more of the Max health drawing is revealed,




                                                                                                                                        #making it seem as if the Robot's depression is decreasing. 

#Called when The Robot Reaches the Deadly Factory. 
def factoryHit():
    global xRobot, yRobot, robotPopulation, robotDepression, maxDepression, robotDrawing, robotDepressiondrawing, robotDepressionremaining, happy, robotStrength
    global factoryIntegrity, factoryHealthremaining, factoryIntegrityvalue, hit, difficulty, robotRepair 

    #If the robot is happy
    if robotDepression[hit] == 0:

        #Recycling the robots so the game runs indefinately. (Until the player fails like a loser.)         
        xRobot[hit] = (randint(1300,2500))
        yRobot[hit] = 450
        robotDepression[hit] = maxDepression

        #Such that the quality of the factory does not increase indefinately.
        #Also such that if the user chose Genocide mode, happy robots do not increase the quality. 
        if factoryIntegrity < 100 and difficulty != 5: 

            factoryIntegrity += robotRepair 

    #If the robot is sad :(
    #Decreases the quality of the factory.
            
    else:
        factoryIntegrity -= robotStrength

        #Again, recycling the robot.         
        xRobot[hit] = (randint(1300,1500))
        yRobot[hit] = 450
        
        factoryIntegrityvalue -= robotStrength
        robotDepression[hit] = maxDepression 







#Game over! (Mwa Mwa Mwa) 
def gameOver():
    global gameEnd
    
    s.delete ('all')
    gameEnd = True 





    
#This is a lonely comment who wants to be showered with love :( 






#For mouse clicked events 
def mouseClickHandler( event ):
    global xMouse, yMouse, xRobotspeed, yRobotspeed, robotDepression, robotPopulation, happyPoints, happyText, gameIntro, difficulty, timeInitial 

    xMouse = event.x
    yMouse = event.y

    #For introscreen 
    if gameIntro == True:
        if 600 <= yMouse <= 700:
            if 200 <= xMouse <= 400:

                #Reveal the instructions! 
                s.delete('all')
                s.create_rectangle(0,0,1300,900, fill = 'black')

                s.create_text(650,50, fill = 'white', font = 'FixedSys 14', text = ' The year is 2100, and humans have created robots to do virtually everything for us. These robots, however, have feelings!')
                s.create_text(650,75, fill = 'white', font = 'FixedSys 14', text = 'Unfortunately, their human masters have restricted much of their freedom. Thus, almost all of them have developed depression.')
                s.create_text(650,100, fill = 'white', font = 'FixedSys 14', text = 'You, the avid Robot Rights Activist, have decided to give these poor robots some motivation as they go to work!')
                s.create_text(650,125, fill = 'white', font = 'FixedSys 14', text = 'Using your Happyness Shooter 3000, you have found a way to grant these robots with the happyness and love they deserve.')
                s.create_text(650,175, fill = 'white', font = 'FixedSys 14', text = 'Can you provide happyness for every robot?')
                s.create_text(650,200, fill = 'white', font = 'FixedSys 12', text = 'Rules: Everytime a robot enters the factory without feeling happy, the quality of the factory decreases due to the robots lack of motivation')
                s.create_text(650,225, fill = 'white', font = 'FixedSys 12', text = 'If the quality of the factory decreases to a critical level, the factory closes down due to bankrupcy, and the robots are all scrapped. :(')
                s.create_text(650,250, fill = 'white', font = 'FixedSys 14', text = 'Save these poor Robots!!!')
                s.create_text(650,275, fill = 'white', font = 'FixedSys 14', text = 'Click on the robots with your left click button on your mouse to shoot these robots with happyness!')
                s.create_text(650,300, fill = 'white', font = 'FixedSys 14', text = 'You can hit multiple robots at the same time. PRESS q at anytime if you want to quit.')
                s.create_text(650,325, fill = 'white', font = 'FixedSys 14', text = 'IMPORTANT!!! : MAKE SURE YOUR SOUND IS ON!')
                s.create_text(650,350, fill = 'white', font = 'FixedSys 14', text = 'NORMAL mode is recommended. Extreme mode for gamers. Hard for anyone in between.')
                s.create_text(650,375, fill = 'white', font = 'FixedSys 14', text = 'Healthy robots will improve the factory. (Not on Genocide mode)')

                s.create_text(650,550, fill = 'white', font = 'FixedSys 14', text = 'TL;DR: Click with Left Click to make Robots happy before work.')
                s.create_text(650,575, fill = 'white', font = 'FixedSys 14', text = 'Press Q at anytime to Quit.')
                s.create_text(650,600, fill = 'white', font = 'FixedSys 14', text = 'Make sure sound is on! Have fun!')                              
                s.create_text(650,625, fill = 'white', font = 'FixedSys 14', text = 'Normal mode is Recommended, Extreme for gamers.')
                s.create_text(650,650, fill = 'white', font = 'FixedSys 14', text = 'Healthy robots will improve the factory.')
                s.create_text(650,675, fill = 'white', font = 'FixedSys 14', text = 'Except for Genocide.')        

                s.create_text(650,715, fill = 'white', font = 'FixedSys 14', text = 'NOTE: I honestly congratulate you if you can last more than 1 minute')
                s.create_text(650,740, fill = 'white', font = 'FixedSys 14', text = 'on Genocide mode. My (Creator) personal record was 1 minute 23 seconds with practise.')

            #The Exit Button.     
            elif 900 <= xMouse <= 1100:
                root.destroy()
            
        
        elif 400 <= yMouse <= 475:
            #If the user chooses a difficulty...
            
            if 100 <= xMouse <= 200:
                difficulty = 0 #Easy Difficulty
                gameIntro = False
                timeInitial = time() 

            elif 300 <= xMouse <= 400:
                difficulty = 1 #Normal Difficulty
                gameIntro = False
                timeInitial = time()                

            elif 500 <= xMouse <= 600:
                difficulty = 2 #Hard Difficulty (Things are getting spicy)
                gameIntro = False   
                timeInitial = time()
                
            elif 700 <= xMouse <= 800:
                difficulty = 3 #Extreme Difficulty (do people even read these)
                gameIntro = False
                timeInitial = time()

                
            elif 900 <= xMouse <= 1000:
                difficulty = 4 #Insane Difficulty (Please say hi to these comments if ur reading them. They're pretty lonely out here D:   )
                gameIntro = False
                timeInitial = time()
                
            elif 1100 <= xMouse <= 1200:
                difficulty = 5 #Genocide Difficulty (damn) did you say hi to these lonely comments? 
                gameIntro = False       
                timeInitial = time()
                
            else:
                pass
        
        else:
            pass 
            

        

    #While the user is playing, if they click on the robot, it reduces its health. 
    else:
            
        for i in range(robotPopulation): 
            if xMouse >= xRobot[i]-25 and xMouse <= xRobot[i] + 25:
                if yMouse >= yRobot[i]-25 and yMouse <= yRobot[i] + 25:

                    if robotDepression[i] > 1:
                        robotDepression[i] -= 1

                    #If they manage to make the robot happy (their depression is reduced to 0, plus 1 happy points~ 
                    elif robotDepression[i] == 1:
                        robotDepression[i] -= 1
                        happyPoints += 1
                        s.delete(happyText)
                        

                    else:
                        pass
    




            
                
#Handles key presses. 
def keyClickHandler( event ):

    global gameEnd

    if gameEnd == False:

        #Ends the game if the user presses q in game.
        if event.keysym == 'q' or event.keysym =='Q':
            gameEnd = True 


        else:
            pass

    else: 

        #Restarts the game if the user presses Y in the end screen. 
        if event.keysym == 'y'or event.keysym == 'Y':
            introScreenopener()
            gameEnd == False
            s.delete('all') 
            
            runGame()
    #Ends the game (actually ends) if the user presses n in the end screen. 
        elif event.keysym == 'n' or event.keysym == 'N':
            trueEnd() 





#Calculates the distance between the Mouse and every robot.     
def mouseDistance():
    global xMouse, yMouse, xRobot, yRobot, distance 
    distance = []
    for i in range(len(xRobot)): #Calculates the distance between the mouse and every robot. 
        a = (sqrt((xMouse-xRobot[i])^2+(yMouse-yRobot[i])))
        distance.append(a) 





#Delets objects every frame. 
def deleteObjects():
    global xRobot, yRobot, robotPopulation, robotDepression, maxDepression, robotDrawing, robotDepressiondrawing, robotDepressionremaining, factoryhealth, factoryHealthremaining
    global happyText, timeText, factoryIntegrityonscreen

    #Deletes all robots 
    for brub in range(robotPopulation):
        s.delete(robotDrawing[brub])
        s.delete(robotDepressiondrawing[brub])
        s.delete(robotDepressionremaining[brub])

    #Deletes everything else. 
    s.delete(factoryHealthremaining)
    s.delete(factoryHealth)
    s.delete(happyText)
    s.delete(timeText)
    s.delete(factoryIntegrityonscreen)





    
 #Draws the intro screen.
def introScreenopener():
    global introscr, introtext, introtext2, introX, introY, difficultyBoxes, difficultyColours, difficultyText, difficultyTextbox, distance 

    
    for i in range(6): #Appends x and y values for the difficulty  boxes. 
        introX.append(75 + (200*i))
        introY.append(400)

    for i in range(6):

        difficultyBoxes[i] = s.create_rectangle(introX[i], introY[i], introX[i] + 100, introY[i]+75, fill = difficultyColours[i])
        difficultyTextbox[i] = s.create_text(introX[i]+50, introY[i]+37.5, fill = 'black', text = difficultyText[i], font = 'FixedSys 14')

    #Instruction Box 
    s.create_rectangle(200,600, 400, 700, fill = '#93dd73')
    s.create_text(300,650, fill = 'black', text = 'Show Instructions', font = 'FixedSys 14')

    #Exit box. 
    s.create_rectangle(900,600, 1100, 700, fill = '#a51738')
    s.create_text(1000,650, fill = 'black', text = 'Exit', font = 'FixedSys 18')

    s.update()




    
    
#End screen (When user presses q or factory quality reaches 0) 
def endGamescreenopen():
    global happy, stringT, musicList, difficulty, happy

    winsound.PlaySound(None, winsound.SND_PURGE) #Stops music

    #End screen. 
    s.delete('all')
    s.create_rectangle(0,0,1300,900, fill = 'black')
    s.create_text(650,300, fill = 'white', text = 'Your final score was :' + ' ' + happy +'.', font = 'FixedSys  18')
    s.create_text(650,400, fill = 'white', text = 'Time played :' + ' ' + stringT, font = 'FixedSys  18') 

    s.create_text(650,600, fill = 'white', text = 'Continue? (Press Y for Yes, N for No.)', font = 'FixedSys 15')
    h = int(happy)
    if h < 10:
        s.create_text(650,200, fill = 'white', text = 'Pathetic. You could not even make 10 robots happy.', font = 'FixedSys  25')     



    #Plays ending music 
    winsound.PlaySound('EndingMusic.wav', winsound.SND_ASYNC)    





#Actual ending.    
def trueEnd():

    #True end: User presses N in the End game screen.
    s.delete('all')
    s.create_rectangle(0,0, 1300, 900, fill = 'white')
    s.create_text(650,450, fill = 'black', text = 'Thanks for Playing!', font = 'FixedSys  30')

    s.update()
    
    
    sleep(3)
    root.destroy()





#Runs the game! 
def runGame():
    winsound.PlaySound('IntroMusic.wav', winsound.SND_ASYNC)
    global robotDrawing, robotDepressiondrawing, robotDepressionremaining, timeInitial, timeReal, happyPoints, gameEnd, factoryIntegrity, introscr, gameIntro, musicList, difficulty
    
    setInitialValues() #Plays intro music 

    #While the user is in the intro screen... 
    while gameIntro == True:    
        introScreenopener()
        s.delete(introscr)

    winsound.PlaySound(None, winsound.SND_PURGE) #Stops intro music  



    #Prepares and starts the game.         
    s.delete('all')
    s.update()
    createBackground()
    difficultyValues()

    
    while gameEnd == False: #As long as the factory doesn't die or the user does not press q. 


        
        drawRobot() #Draws every robot
        drawfactory()
        displayStuff()

        s.update()
        sleep(0.008)

        
        timeReal = floor(time() - timeInitial)
        
        deleteObjects()             
        updateObjects()


        
        if factoryIntegrity <= 0: #If the factory's integrity reaches a critical point (0), end the game. 
            gameOver() 

    
    s.create_rectangle(0,0,1000,1000, fill = 'white')
    endGamescreenopen()

    
    s.create_text(500,500, fill = 'black', text = 'Thanks for playing. Game over! Your score was' + ": " + (str(happyPoints)) + " " + 'Good job!') 



root.after(0, runGame)

s.bind('<Button-1>', mouseClickHandler)
s.bind('<Key>', keyClickHandler)
s.pack()
s.focus_set()
root.mainloop()







