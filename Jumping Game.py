import pygame
import random
import math
from PIL import Image
pygame.init()

screen=pygame.display.set_mode((1400,800))
#-----Title----------------------------------
pygame.display.set_caption("Python Game")
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
NJump = pygame.font.Font('freesansbold.ttf', 64)
scoring= pygame.font.Font('freesansbold.ttf', 64)
#-----vALUES------------------------------------------------
isJump=False
jumpCount=0
INDEX=0
START=1
running=True
#-----------------------------------------------------------
#--PLAYER---------------------------------------------------
playerImg=pygame.image.load("4.png")
playerX=200
playerY=300
Pname=[]
for m in range(1,60):
   for j in range(5):
      Pname.append(m)
# Set Player Image   
def player(name):
   global playerX,playerY,playerImg,tree
   screen.blit(pygame.image.load(name),(playerX,playerY))
#------obstacle-----------------------------------------------
obstacles=['wood','rocks','mount','wbox']
obst=obstacles[random.randint(0,3)]
OX=800
OY=600
OBSTACLE_VELOCITY=20
im = Image.open(f'{obst}.png')
width, height = im.size
DIMENSION=[width,height]
#------STUFFS-----------------------------------------------------------------------------------
BACK_GROUND=['back7','back6','back2','back4','back1']
BX    =[i*1800 for i in range(0,len(BACK_GROUND))]
BY    =[0 for i in range(len(BACK_GROUND))]
BV    =[4 for i in range(len(BACK_GROUND))]

Object=['sun','house1','house2','tree3','tree2','road','road']#,'boy']
objX=[1300 , 500    , 1000   , 1500       , 10    ,-10     ,2500]#, 1500]
objY=[50   ,400     , 400    , 20         ,10     ,680   ,680   ]#,400  ]
objV=[1    ,4       ,4       ,4              ,4      ,10     ,10  ]#   ,12    ]
#----COINS---------------------------------------------------------------------------------------
coins  = ['coin2','coin2','coin2','coin2']
Cpoint = [5]
CX     = [1400,800,500,1500]
CY     = [500,400,500,300]
CV     = [4,4,4,4]
COIN=coins[random.randint(0,3)]
Cim=[]
coinDIMENSION=[]
for i in range(len(coins)):
   Cim.append(Image.open(f'{COIN}.png'))
   width, height = Cim[-1].size
   coinDIMENSION.append(width)
#------------------------------------------------------------------------------------------------
for i in Object:
   globals()[i]=pygame.image.load(f"{i}.png")#.convert()
for i in BACK_GROUND:
   globals()[i]=pygame.image.load(f"{i}.png")#.convert()
no=0
SCORE=0
LIFE=200 #################
JUMP=0
pas=0
class objects:
   def SetObject(self,objX,objY):
      no1=0
      for i in BACK_GROUND:
         screen.blit(eval(i),(BX[no1],BY[no1]))
         no1+=1

      no=0
      for i in Object:
         screen.blit(eval(i),(objX[no],objY[no]))
         no+=1

   def MoveObstacle(self,OX,OY):
      OBSTACLES=pygame.image.load(f"{obst}.png")#.convert()
      screen.blit(OBSTACLES,(OX,OY))
   def MoveCoins(self,CX,CY):
      COINS=pygame.image.load(f"{COIN}.png")#.convert()
      screen.blit(COINS,(CX,CY))

   def isCollision(self,i):
      global no,DIMENSION,SCORE,coins,CX,CY,LIFE,OBSTACLE_VELOCITY
      if playerX>OX-100 and playerX<OX+DIMENSION[0]:
         if playerY>450:
            LIFE-=1
      if playerX+100>CX[i]and playerY<CY[i]:
         CX[i]=random.randint(1500,1600)
         CY[i]=random.randint(300,500)
         SCORE+=1
         if SCORE%5==0:
            OBSTACLE_VELOCITY+=1
      no+=1

   def END_X(self):
      global OX,obst,DIMENSION,coins
      if OX<-800:
         OX=1500
         objects().MoveObstacle(OX,OY)
         obst=obstacles[random.randint(0,3)]
         im = Image.open(f'{obst}.png')
         width, height = im.size
         DIMENSION=[width,height]
   def life(self):
      global over_font,NJump,SCORE,LIFE,JUMP,scoring
      over_text = over_font.render("Life "+str(LIFE), True, (255, 255, 255))
      jump_text = NJump.render("Jump "+str(JUMP), True, (255, 255, 255))
      score = scoring.render("Score "+str(SCORE), True, (255, 255, 255))
      screen.blit(over_text, (20,20))
      screen.blit(score, (1000,100))
      screen.blit(jump_text, (1000,20))
   def END_GAME(self):
      global LIFE,OBSTACLE_VELOCITY
      if LIFE<=0:
         LIFE=1
         OBSTACLE_VELOCITY=0
   def SCREEN_MOVE(self): #1850
      global BACK_GROUND,BX,BV,Object,objX,objY,objV,pas
      for i in range(len(BACK_GROUND)):
         BX[i]-=BV[i]
         if BX[i]<-1900:
            BX[i]=1850*(len(BACK_GROUND)-1)
      for i in range(len(Object)):
         objX[i]-=objV[i]
      # Display Road image one by one
      for i in range(len(Object)):
         objX[i]-=objV[i]
         if Object[i]=='back1':
            if objX[i]<-1500:
               if i==1:
                  objX[1]=objX[0]+1444
               if i==0:
                  objX[0]=objX[1]+1444
      # Display Road image one by one
         elif Object[i]=='road':
            m=Object.index('road')
            if objX[i]<-2660:
               if i==m+1:
                  objX[m+1]=objX[m]+1444
               if i==m:
                  objX[m]=objX[m+1]+1444
                  
      # Display Other Obstecle image one by one
         else:
            if objX[i]<-1100:
               objX[i]=1550
                  
      # Display Other Obstecle image one by one



while running:
#   pygame.time.delay(10)
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         running=False
   keys= pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]:
      if playerX<200:
         playerX+=30
   if keys[pygame.K_LEFT]:
      if playerX>0:
         playerX-=30

# Jumping of player
   if not(isJump):      
      if keys[pygame.K_SPACE]:
         isJump=True
         JUMP+=1
      if START==1:
         START+=1
         isjump=True
   else:
      if jumpCount>=-10:
         neg=1
         if jumpCount<0:
            neg=-1
         playerY-=(jumpCount**2)*0.5*neg
         jumpCount-=0.9
         playerY+=0.5
         if INDEX<=len(Pname)-2:
            INDEX+=1
         else:
            INDEX=0

      else:
         isJump=False
         jumpCount=10
         INDEX=0
       

      
   screen.fill((10,10,20 ))
   objects().SetObject(objX,objY)
   
   name=f"{Pname[INDEX]}.png"
   player(name)
   
   objects().MoveObstacle(OX,OY)
   for i in range(len(coins)):
      objects().MoveCoins(CX[i],CY[i])
      CX[i]-=OBSTACLE_VELOCITY
      objects().isCollision(i)
      objects().life()
      objects().END_GAME()
   objects().SCREEN_MOVE()
   OX-=OBSTACLE_VELOCITY
   objects().END_X()
   pygame.display.update()

         
pygame.quit()


















