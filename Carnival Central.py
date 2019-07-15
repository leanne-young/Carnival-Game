#map.py
import pygame, time, random
pygame.init()

#some important numerical values
size = (640,400)
white = (255,255,255)
black = (0,0,0)
go = 0
x=0
y=0
startscreen = 1
#mole values
playnowclick = 0
timecount = 0
score = 0
moleplace=0
hitplace=0
win = 0
#hammer values
arrowy = 35
belly = 335
dir = 6
runningmeter=0
hammerfinish = 0
hammerplayclick = 0
instructionsclick=0
#store values
prizesdisplay = 0
buyclick = 0
#general
ticketcount = 0
ticketswon = 0
whileloop = 0

#title
pygame.display.set_caption("Carnival Central!")

#on screen text
font = pygame.font.Font(None, 37)
fontbowl = pygame.font.Font(None, 27)
prizelist = [1,2,3,4,5,6,7]
numtics = ""

#button variables
command = ""
command2 = ""
command3 = ""
command4 = ""
prize = ""
prize2 = ""
prize3 = ""
prize4 = ""
prize5 = ""
prize6 = ""
prize7 = ""

#WELCOME screen pictures
circusscene = pygame.image.load("circusscene.jpg")
circusscene = pygame.transform.scale(circusscene, (795,400))
title = pygame.image.load("title.png")
title = pygame.transform.scale(title, (530,180))


#MAP pictures
screen = pygame.display.set_mode(size)
parkmap = pygame.image.load("parkmap.jpg")
parkmap = pygame.transform.scale(parkmap, (640,445))

moleicon=pygame.sprite.Sprite()
moleicon.image = pygame.image.load("moleicon.png")
moleicon.rect=moleicon.image.get_rect()
moleicon.rect.topleft=(70,150)

hammericon=pygame.sprite.Sprite()
hammericon.image = pygame.image.load("hammericon.png")
hammericon.rect=hammericon.image.get_rect()
hammericon.rect.topleft=(380,220)    #(375,225)

bowlingicon=pygame.sprite.Sprite()
bowlingicon.image = pygame.image.load("bowlingicon.png")
bowlingicon.rect=bowlingicon.image.get_rect()
bowlingicon.rect.topleft=(270,50)

storeicon=pygame.sprite.Sprite()
storeicon.image = pygame.image.load("storeicon.png")
storeicon.rect=storeicon.image.get_rect()
storeicon.rect.topleft=(480,110)

tickets = pygame.image.load("tickets.png")
tickets = pygame.transform.scale(tickets, (50,40))

ticketbox = pygame.image.load("ticketbox.png")
ticketbox = pygame.transform.scale(ticketbox, (135,37))

parkmap = pygame.transform.scale(parkmap, (640,445))

#Game menu buttons 
instructions=pygame.sprite.Sprite()
instructions.image = pygame.image.load("instructions.png")
instructions.rect=instructions.image.get_rect()

back=pygame.sprite.Sprite()
back.image = pygame.image.load("back.png")
back.rect=back.image.get_rect()

arrowbutton=pygame.sprite.Sprite()
arrowbutton.image = pygame.image.load("arrowbutton.png")
arrowbutton.rect=arrowbutton.image.get_rect()
arrowbutton.rect.topleft=(525,285)

play=pygame.sprite.Sprite()
play.image = pygame.image.load("play.png")
play.rect=play.image.get_rect()
play.rect.topleft=(175,165)

playnow=pygame.sprite.Sprite()
playnow.image = pygame.image.load("playnow.png")
playnow.rect=playnow.image.get_rect()
playnow.rect.topleft=(5,225)

#win screen pictures
rainbowback = pygame.image.load("rainbowback.jpg")
rainbowback = pygame.transform.scale(rainbowback, (640,400))

playagain=pygame.sprite.Sprite()
playagain.image = pygame.image.load("playagain.png")
playagain.rect=playagain.image.get_rect()
playagain.rect.topleft=(3,330)

arrowbutton2=pygame.sprite.Sprite()
arrowbutton2.image = pygame.image.load("arrowbutton2.png")
arrowbutton2.rect=arrowbutton2.image.get_rect()
arrowbutton2.rect.topleft=(540,305)

greatjob = pygame.image.load("greatjob.png")

youhavewon = pygame.image.load("youhavewon.png")

ticketsword = pygame.image.load("ticketsword.png")

tics0 = pygame.image.load("0tics.png")
tics1 = pygame.image.load("1tics.png")
tics2 = pygame.image.load("tics2.png")
tics3 = pygame.image.load("tics3.png")
tics4 = pygame.image.load("tics4.png")

#countdown numbers
num1 = pygame.image.load("1.png")
num2 = pygame.image.load("2.png")
num3 = pygame.image.load("3.png")

#MOLE game pictures
moles = pygame.image.load("moles.png")

moleinstructionstitle = pygame.image.load("moleinstructionstitle.png")

molesinstructions = pygame.image.load("molesinstructions.png")

moletitle = pygame.image.load("moletitle.png")
moletitle = pygame.transform.scale(moletitle, (440,140))

whackamole = pygame.image.load("whackamole.jpg")
whackamole = pygame.transform.scale(whackamole, (640,400))

mole=pygame.sprite.Sprite()
mole.image = pygame.image.load("mole.png")
mole.rect=mole.image.get_rect()


#HAMMER game pictures
hammertitle = pygame.image.load("hammertitle.png")

hammerplay=pygame.sprite.Sprite()
hammerplay.image = pygame.image.load("hammerplay.png")
hammerplay.rect=hammerplay.image.get_rect()
hammerplay.rect.topleft=(80,300) #y=275

hammer2 = pygame.image.load("hammer2.png")
hammer2 = pygame.transform.scale(hammer2, (115,130))

hammerhit = pygame.image.load("hammerhit.png")
hammerhit = pygame.transform.scale(hammerhit, (130,115))

hammergame = pygame.image.load("hammergame.png")
hammergame = pygame.transform.scale(hammergame, (640,400))

hammerbell = pygame.image.load("hammerbell.png")
hammerbell = pygame.transform.scale(hammerbell, (30,10))

hammerbackbutton=pygame.sprite.Sprite()
hammerbackbutton.image = pygame.image.load("hammerbackbutton.png")
hammerbackbutton.rect=hammerbackbutton.image.get_rect()
hammerbackbutton.rect.topleft=(0,0)

hammerarrow = pygame.image.load("hammerarrow.png")

hammermeter = pygame.image.load("hammermeter.png")

hammerinstructionstitle = pygame.image.load("hammerinstructionstitle.png")
hammerinstructions = pygame.image.load("hammerinstructions.png")


#BOWLING game pictures
bowling2 = pygame.image.load("bowling2.png")
bowling2 = pygame.transform.scale(bowling2, (640,400))

bowlwords = pygame.image.load("bowlwords.png")
bowlwords = pygame.transform.scale(bowlwords, (275,125))

strike = pygame.image.load("strike.png")
strike = pygame.transform.scale(strike, (640,400))

bowlingballscene1 = pygame.image.load("bowlingballscene1.jpg")
bowlingballscene1 = pygame.transform.scale(bowlingballscene1, (640,400))

bowlingballscene2 = pygame.image.load("bowlingballscene2.jpg")
bowlingballscene2 = pygame.transform.scale(bowlingballscene2, (640,400))


#STORE pictures
storebackground = pygame.image.load("storebackground.jpg")
storebackground = pygame.transform.scale(storebackground, (640,400))

shelves = pygame.image.load("shelves.png")

notickets = pygame.image.load("notickets.png")

myprizestitle = pygame.image.load("myprizestitle.png")
myprizestitle = pygame.transform.scale(myprizestitle, (320,75))

giftshoplogo = pygame.image.load("giftshoplogo.png")

storeback=pygame.sprite.Sprite()
storeback.image = pygame.image.load("storeback.png")
storeback.rect=storeback.image.get_rect()
storeback.rect.topleft=(560,360)

buy=pygame.sprite.Sprite()
buy.image = pygame.image.load("buy.png")
buy.rect=buy.image.get_rect()
buy.rect.topleft=(255,25)

myprizes=pygame.sprite.Sprite()
myprizes.image = pygame.image.load("myprizes.png")
myprizes.rect=myprizes.image.get_rect()
myprizes.rect.topleft=(50,200)

bear=pygame.sprite.Sprite()
bear.image = pygame.image.load("bear.png")
bear.rect=bear.image.get_rect()

car=pygame.sprite.Sprite()
car.image = pygame.image.load("car.png")
car.rect=car.image.get_rect()

giftcard=pygame.sprite.Sprite()
giftcard.image = pygame.image.load("giftcard.png")
giftcard.rect=giftcard.image.get_rect()

ipod=pygame.sprite.Sprite()
ipod.image = pygame.image.load("ipod.png")
ipod.rect=ipod.image.get_rect()

rainbowball=pygame.sprite.Sprite()
rainbowball.image = pygame.image.load("rainbowball.png")
rainbowball.rect=rainbowball.image.get_rect()

snake=pygame.sprite.Sprite()
snake.image = pygame.image.load("snake.png")
snake.rect=snake.image.get_rect()

monkeys=pygame.sprite.Sprite()
monkeys.image = pygame.image.load("monkeys.png")
monkeys.rect=monkeys.image.get_rect()



#game (map)
while (True):
	#start screen
	while (startscreen==1):
		screen.blit(circusscene,(-120,0))
		screen.blit(title,(55,-15))
		screen.blit(play.image,play.rect)
		
		event=pygame.event.poll()
		if (event.type == pygame.QUIT):
			break
		
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
			(x,y)=event.pos
		if (play.rect.collidepoint(x,y)):
			whileloop=1
			startscreen=0
		
		pygame.display.update()
	
	#map/navigation screen
	while (whileloop==1):
		#map screen with icons
		screen.blit(parkmap,(0,0))
		screen.blit(moleicon.image, moleicon.rect)
		screen.blit(bowlingicon.image, bowlingicon.rect)
		screen.blit(hammericon.image, hammericon.rect)
		screen.blit(storeicon.image, storeicon.rect)
		screen.blit(ticketbox,(5,5))
		screen.blit(tickets,(5,0))
		text = font.render(str(ticketcount), True, (0,255,255), (0,0,255))
		screen.blit(text, (75,12))
		
		event=pygame.event.poll()
		if (event.type == pygame.QUIT):
			break
			
		#clicking on icons	
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
			(x,y)=event.pos
		if (moleicon.rect.collidepoint(x,y)):
			command = "mole"
		if (hammericon.rect.collidepoint(x,y)):
			command2 = "hammer"
		if (bowlingicon.rect.collidepoint(x,y)):
			command3 = "bowling"
		if (storeicon.rect.collidepoint(x,y)):
			command4 = "store"
			#time.sleep(1)

		#icon commands to direct to other scenes
		if (command=="mole"):
			print ("mole")
			whileloop=2
			break	
			
		if (command2=="hammer"):
			print ("hammer")
			whileloop=3
			break
			
		if (command3=="bowling"):
			print ("bowling")
			whileloop=4
			break
			
		if (command4=="store"):
			print ("store")
			whileloop=5
			break
		
		pygame.display.update()
		
		
	#molegame
	while (whileloop==2):
		#game menu
		score = 0
		screen.fill((90,203,57))
		screen.blit(moletitle,(100,0))
		screen.blit(moles,(217,150))
		screen.blit(playnow.image, playnow.rect)
		instructions.rect.topleft=(423,215)
		screen.blit(instructions.image, instructions.rect)
		back.rect.topleft=(5,5)
		screen.blit(back.image, back.rect)
		pygame.display.update()
		
		event=pygame.event.poll()
		if (event.type == pygame.QUIT):
			break
		
		#clicking on the menu
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				(x,y)=event.pos
		if (playnow.rect.collidepoint(x,y)):
			playnowclick = 1
		if (instructions.rect.collidepoint(x,y)):
			instructionsclick = 1
		if (back.rect.collidepoint(x,y)):
			command = ""
			whileloop = 1
			break
		
		#instructions page
		while (instructionsclick==1):
			screen.fill((90,203,57))
			screen.blit(moleinstructionstitle,(100,10))
			screen.blit(molesinstructions,(115,100))
			screen.blit(arrowbutton.image, arrowbutton.rect)
			
			event=pygame.event.poll()
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				(x,y)=event.pos
			if (arrowbutton.rect.collidepoint(x,y)):
				playnowclick = 1
				instructionsclick = 0
				
			pygame.display.update()
		
		#actual whackamole game
		while (playnowclick==1):
			score = 0
			screen.blit(whackamole,(0,0))
			text = font.render(str(timecount), True, (255,255,0), (164,99,31))
			screen.blit(text, (145,30))
			scoretext = font.render(str(score), True, (255,255,0), (164,99,31))
			screen.blit(scoretext, (460,30))
			
			#countdown
			event=pygame.event.poll()
			if (event.type==pygame.KEYDOWN):
				if (event.key==pygame.K_s):
					screen.blit(num3,(180,50))
					pygame.display.flip()
					
					time.sleep(1)
					screen.blit(num2,(180,50))
					pygame.display.flip()
					
					time.sleep(1)
					screen.blit(num1,(180,50))
					pygame.display.flip()
					time.sleep(1)
					
					#timecount = 30
					#while (timecount>0):
					win = 1
					
					#game starts
					for c in range (30,-1,-1):
						screen.blit(whackamole,(0,0))
						text = font.render(str(c), True, (255,255,0), (164,99,31))
						screen.blit(text, (145,30))
						scoretext = font.render(str(score), True, (255,255,0), (164,99,31))
						screen.blit(scoretext, (460,30))
						
						moleplace = random.randint(1,12)
						
						#identitying the mole position + blitting
						if (moleplace==1):
							mole.rect.topleft=(129,90)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==2):
							mole.rect.topleft=(234,90)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==3):
							mole.rect.topleft=(334,90)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==4):
							mole.rect.topleft=(435,90)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==5):
							mole.rect.topleft=(121,179)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==6):
							mole.rect.topleft=(228,179)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==7):
							mole.rect.topleft=(337,179)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==8):
							mole.rect.topleft=(443,179)
							screen.blit(mole.image, mole.rect)
							pygame.display.flip()
							
						if (moleplace==9):
							mole.rect.topleft=(110,276)
							screen.blit(mole.image, mole.rect)
							pygame.display.update()
							
						if (moleplace==10):
							mole.rect.topleft=(227,276)
							screen.blit(mole.image, mole.rect)
							pygame.display.update()
							
						if (moleplace==11):
							mole.rect.topleft=(341,276)
							screen.blit(mole.image, mole.rect)
							pygame.display.update()
							
						if (moleplace==12):
							mole.rect.topleft=(451,276)
							screen.blit(mole.image, mole.rect)
							pygame.display.update()
								
						event=pygame.event.poll()
						if (event.type == pygame.QUIT):
							break
						
						if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
							(x,y)=event.pos
						if (mole.rect.collidepoint(x,y)):
							print ("hitttt")
							score = score + 100
							screen.blit(whackamole,(0,0))
							text = font.render(str(c), True, (255,255,0), (164,99,31))
							screen.blit(text, (145,30))
							scoretext = font.render(str(score), True, (255,255,0), (164,99,31))
							screen.blit(scoretext, (460,30))
							pygame.display.flip()
						
						
						pygame.display.update()
						time.sleep(1)
						
						
						#identifying the user strike
						#if (event.type==pygame.KEYDOWN):
							#if (event.key==pygame.K_KP1):
								#hitplace = 1
								#print ("1")
							#if (event.key==pygame.K_KP2):
								#hitplace = 2
								#print ("2")
							#if (event.key==pygame.K_KP3):
								#hitplace = 3
								#print ("3")
							#if (event.key==pygame.K_KP4):
								#hitplace = 4
								#print ("4")
			
			#tickets won
			if (score<=500):
				numtics = tics0
				ticketswon = 0
			if (500<score<=1000):
				numtics = tics1
				ticketswon = 1
			if (1000<score<=1500):
				numtics = tics2
				ticketswon = 2
			if (1500<score<=2000):
				numtics = tics3
				ticketswon = 3
			if (score>2000):
				numtics = tics4
				ticketswon = 4
			
			ticketcount = ticketcount + ticketswon
			#win screen
			while (win==1):
				screen.blit(rainbowback,(0,0))
				screen.blit(greatjob,(165,-40))
				screen.blit(playagain.image, playagain.rect)
				screen.blit(arrowbutton2.image, arrowbutton2.rect)
				screen.blit(youhavewon,(125,169))
				screen.blit(numtics,(285,225))
				screen.blit(ticketsword,(185,300))
				
				event=pygame.event.poll()
				if (event.type == pygame.QUIT):
					break
				
				if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
					(x,y)=event.pos
					if (playagain.rect.collidepoint(x,y)):
						win=0
						break
					if (arrowbutton2.rect.collidepoint(x,y)):
						command = ""
						whileloop=1
						win=0
						playnowclick=0
						break
				
				pygame.display.flip()
			
			pygame.display.update()	
		
	#hammer
	while (whileloop==3):
		#game menu screen
		screen.fill((0,0,0))
		screen.blit(hammertitle,(50,40)) #y=15
		screen.blit(hammerplay.image, hammerplay.rect)
		instructions.rect.topleft=(325,300)
		screen.blit(instructions.image, instructions.rect)
		back.rect.topleft=(5,5)
		screen.blit(back.image, back.rect)
		pygame.display.update()
		
		event=pygame.event.poll()
		if (event.type == pygame.QUIT):
			break
		
		#clicking on the menu
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
			(x,y)=event.pos
		if (hammerplay.rect.collidepoint(x,y)):
			hammerplayclick = 1
		if (instructions.rect.collidepoint(x,y)):
			instructionsclick = 1
		if (back.rect.collidepoint(x,y)):
			command2 = ""
			whileloop = 1
			break
		
		#instructions page
		while (instructionsclick==1):
			screen.fill((0,0,0))
			screen.blit(hammerinstructionstitle,(105,15))
			screen.blit(hammerinstructions,(90,90))
			screen.blit(arrowbutton.image, arrowbutton.rect)
			pygame.display.flip()
			event=pygame.event.poll()
			if (event.type == pygame.QUIT):
				break
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				(x,y)=event.pos
			if (arrowbutton.rect.collidepoint(x,y)):
				instructionsclick = 0
				hammerplayclick = 1
				break
		
		#actual hammer game
		while (hammerplayclick==1):
			arrowy = 35
			belly = 335
			ticketswon = 0
			hammerfinish = 0
			screen.blit(hammergame,(0,0))
			screen.blit(hammermeter,(585,58))
			screen.blit(hammer2,(400,215))
			screen.blit(hammerarrow,(530,arrowy))
			screen.blit(hammerbackbutton.image, hammerbackbutton.rect)
			
			event=pygame.event.poll()
			if (event.type == pygame.QUIT):
				break
					
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
					(x,y)=event.pos
			if (hammerbackbutton.rect.collidepoint(x,y)):
				whileloop=3
				hammerplayclick=0
			
			#countdown	
			if (event.type==pygame.KEYDOWN):
				if (event.key==pygame.K_s):
					screen.blit(num3,(180,50))
					pygame.display.flip()
					
					time.sleep(1)
					screen.blit(num2,(180,50))
					pygame.display.flip()
					
					time.sleep(1)
					screen.blit(num1,(180,50))
					pygame.display.flip()
					time.sleep(1)
					
					#game starts (meter starts moving)
					while (runningmeter!=1):
						screen.blit(hammergame,(0,0))
						screen.blit(hammer2,(400,215))
						screen.blit(hammermeter,(585,58))
						screen.blit(hammerbackbutton.image, hammerbackbutton.rect)
						screen.blit(hammerarrow,(530,arrowy))
						arrowy = arrowy + dir
						if (arrowy>334):
							dir = dir*(-1)
						if (arrowy<25):
							dir = dir*(-1)
						pygame.display.flip()
						
						#when user hits space (swinging the hammer)
						event=pygame.event.poll()
						if (event.type==pygame.KEYDOWN):
							if (event.key==pygame.K_SPACE):
								runningmeter = 0
								screen.blit(hammergame,(0,0))
								screen.blit(hammermeter,(585,58))
								screen.blit(hammerbackbutton.image, hammerbackbutton.rect)
								screen.blit(hammerarrow,(530,arrowy))
								screen.blit(hammerhit,(270,265))
								pygame.display.flip()
								hammerfinish = 1
								break
						if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
							(x,y)=event.pos
							if (hammerbackbutton.rect.collidepoint(x,y)):
								hammerplayclick=0

								break
								
			#after hammer is hit
			if (hammerfinish==1):								
				#print (arrowy)
				win = 1
				screen.blit(hammerbell,(305,belly))
				screen.blit(hammerhit,(270,265))
				pygame.display.flip()
				time.sleep(1)
				
				#determining the height the bell goes to
				if (arrowy<=65):
					while (belly>250):
						belly = belly - 2
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics0
					ticketswon = 0
				if (65<arrowy<=110):
					while (belly>200):
						belly = belly - 1.5
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics1
					ticketswon = 1
				if (110<arrowy<=155):
					while (belly>145):
						belly = belly - 1.5
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics2
					ticketswon = 2
				if (155<arrowy<=205):
					while (belly>110):
						belly = belly - 1.5
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics3
					ticketswon = 3
				if (205<arrowy<=240):
					while (belly>145):
						belly = belly - 1.5
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics2
					ticketswon = 2
				if (240<arrowy<=290):
					while (belly>200):
						belly = belly - 1.5
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics1
					ticketswon = 1
				if (arrowy>290):
					while (belly>250):
						belly = belly - 2
						screen.blit(hammerbell,(305,belly))
						screen.blit(hammerhit,(270,265))
						pygame.display.flip()
					numtics = tics0
					ticketswon = 0
				
				ticketcount = ticketcount + ticketswon
				time.sleep(1.4)
				
				#congrats page / tickets won
				while (win==1):
					screen.blit(rainbowback,(0,0))
					screen.blit(greatjob,(165,-40))
					screen.blit(playagain.image, playagain.rect)
					screen.blit(arrowbutton2.image, arrowbutton2.rect)
					screen.blit(youhavewon,(125,169))
					screen.blit(numtics,(285,225))
					screen.blit(ticketsword,(185,300))
					#screen.draw.text(str(ticketswon), (100, 100), color=(200, 200, 200), background=None)
					#screen.blit(text, (300,250))
					
					event=pygame.event.poll()
					if (event.type == pygame.QUIT):
						break
					
					if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
						(x,y)=event.pos
						if (playagain.rect.collidepoint(x,y)):
							win=0
							break
						if (arrowbutton2.rect.collidepoint(x,y)):
							command2 = ""
							whileloop=1
							win=0
							hammerplayclick=0
							break
					
					pygame.display.flip()		
			
			
			
			
			
			pygame.display.flip()
			#pygame.display.update()
		
	#bowling
	if (whileloop==4):
		#bowling scene 1
		screen.blit(bowling2,(0,0))
		screen.blit(bowlwords,(45,25))
		back.rect.topleft=(5,350)
		screen.blit(back.image, back.rect)
		text = fontbowl.render(str("(Win 1 ticket for each bowl!)"), True, (0,255,255), (0,0,150))
		screen.blit(text, (60,150))
		pygame.display.flip()
		
		event=pygame.event.poll()
		
		#back button
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
			(x,y)=event.pos
		if (back.rect.collidepoint(x,y)):
			command3 = ""
			whileloop = 1
			#break
		
		#bowling animation
		if (event.type==pygame.KEYDOWN):
			if (event.key==pygame.K_SPACE):
				screen.blit(bowlingballscene1,(0,0))
				pygame.display.flip()
						
				time.sleep(1.2)
				screen.blit(bowlingballscene2,(0,0))
				pygame.display.flip()
				
				time.sleep(1.2)
				screen.blit(strike,(0,0))
				pygame.display.flip()
				time.sleep(1.8)
				
				ticketcount = ticketcount + 1
		
				#command3 = ""
				#whileloop = 1
	
	
	#store
	while (whileloop==5):
		print (prizelist)
		
		event=pygame.event.poll()
		if (event.type == pygame.QUIT):
			break
		
		#main store screen
		command4 = ""
		event.button = 0
		screen.blit(storebackground,(0,0))
		shelves = pygame.transform.scale(shelves, (550,500))
		screen.blit(shelves,(155,-20))
		screen.blit(giftshoplogo,(5,5))
		screen.blit(ticketbox,(5,355))
		screen.blit(tickets,(5,350))
		text = font.render(str(ticketcount), True, (0,255,255), (0,0,255))
		screen.blit(text, (68,361))
		screen.blit(storeback.image, storeback.rect)
		screen.blit(myprizes.image, myprizes.rect)
		
		#prize locations
		bear.rect.topleft=(490,135)
		car.rect.topleft=(365,145)
		giftcard.rect.topleft=(325,270)
		ipod.rect.topleft=(480,250)
		rainbowball.rect.topleft=(265,150)
		snake.rect.topleft=(465,45)
		monkeys.rect.topleft=(310,35)
		
		screen.blit(buy.image, buy.rect)
		
		event=pygame.event.poll()
		if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
			(x,y)=event.pos
		if (buy.rect.collidepoint(x,y)):
			buyclick = 1
		if (storeback.rect.collidepoint(x,y)):
				whileloop=1
				break
		if (myprizes.rect.collidepoint(x,y)):
			prizesdisplay = 1
		
		#buying loop
		if (buyclick==1):
			screen.blit(storebackground,(0,0))
			shelves = pygame.transform.scale(shelves, (550,500))
			screen.blit(shelves,(155,-20))
			screen.blit(giftshoplogo,(5,5))
			screen.blit(ticketbox,(5,355))
			screen.blit(tickets,(5,350))
			text = font.render(str(ticketcount), True, (0,255,255), (0,0,255))
			screen.blit(text, (68,361))
			screen.blit(storeback.image, storeback.rect)
			screen.blit(myprizes.image, myprizes.rect)
			
			#determining if the item has already been purchased or not to blit on the screen
			for c in range (0,7):
				if (prizelist[c]==1):
					screen.blit(bear.image, bear.rect)
				if (prizelist[c]==2):
					screen.blit(car.image, car.rect)
				if (prizelist[c]==3):	
					screen.blit(giftcard.image, giftcard.rect)
				if (prizelist[c]==4):
					screen.blit(ipod.image, ipod.rect)
				if (prizelist[c]==5):
					screen.blit(monkeys.image, monkeys.rect)
				if (prizelist[c]==6):
					screen.blit(snake.image, snake.rect)
				if (prizelist[c]==7):
					screen.blit(rainbowball.image, rainbowball.rect)
			
			#clicking on prizes
			event=pygame.event.poll()
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				(x,y)=event.pos
			if (ticketcount>=3):
				if (bear.rect.collidepoint(x,y)):
					prize = "bear"
			else:
				screen.blit(notickets,(300,100))
				pygame.display.flip()
				time.sleep(3)
				
			if (ticketcount>=5):
				if (car.rect.collidepoint(x,y)):
					prize2 = "car"
			if (ticketcount>=7):
				if (giftcard.rect.collidepoint(x,y)):
					prize3 = "giftcard"
			if (ticketcount>=10):
				if (ipod.rect.collidepoint(x,y)):
					prize4 = "ipod"
			if (ticketcount>=3):
				if (monkeys.rect.collidepoint(x,y)):
					prize5 = "monkeys"
			if (ticketcount>=2):
				if (snake.rect.collidepoint(x,y)):
					prize6 = "snake"
			if (ticketcount>=2):
				if (rainbowball.rect.collidepoint(x,y)):
					prize7 = "rainbowball"
			if (storeback.rect.collidepoint(x,y)):
				whileloop=1
				break
			if (myprizes.rect.collidepoint(x,y)):
				prizesdisplay = 1
			
			pygame.display.update()
			
			#ticket reduction (purchase)
			if (prize=="bear"):
				print ("bear")
				ticketcount = ticketcount - 3
				print (str(ticketcount))
				prizelist[0]=0
				prize = ""
				buyclick = 0
				break
				
			if (prize2=="car"):
				print ("car")
				ticketcount = ticketcount - 5
				print (str(ticketcount))
				prizelist[1]=0
				prize2 = ""
				buyclick = 0
				break
				
			if (prize3=="giftcard"):
				print ("giftcard")
				ticketcount = ticketcount - 7
				print (str(ticketcount))
				prizelist[2]=0
				prize3 = ""
				buyclick = 0
				break
				
			if (prize4=="ipod"):
				print ("ipod")
				ticketcount = ticketcount - 10
				print (str(ticketcount))
				prizelist[3]=0
				prize4 = ""
				buyclick = 0
				break
			
			if (prize5=="monkeys"):
				print ("monkeys")
				ticketcount = ticketcount - 3
				print (str(ticketcount))
				prizelist[4]=0
				prize5 = ""
				buyclick = 0
				break
				
			if (prize6=="snake"):
				print ("snake")
				ticketcount = ticketcount - 2
				print (str(ticketcount))
				prizelist[5]=0
				prize6 = ""
				buyclick = 0
				break
				
			if (prize7=="rainbowball"):
				print ("rainbowball")
				ticketcount = ticketcount - 2
				print (str(ticketcount))
				prizelist[6]=0
				prize7 = ""
				buyclick = 0
				break
	
		#viewing the prizes you have purchased page
		while (prizesdisplay==1):
			screen.blit(rainbowback,(0,0))
			shelves = pygame.transform.scale(shelves, (575,400))
			screen.blit(arrowbutton.image, arrowbutton.rect)
			screen.blit(shelves,(25,65))
			screen.blit(myprizestitle,(155,0))
			
			#prize locations
			bear.rect.topleft=(390,180)
			car.rect.topleft=(265,190)
			giftcard.rect.topleft=(197,285)
			ipod.rect.topleft=(375,265)
			rainbowball.rect.topleft=(165,190)
			snake.rect.topleft=(350,100)
			monkeys.rect.topleft=(190,90)
			
			event=pygame.event.poll()
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
				(x,y)=event.pos
			if (arrowbutton.rect.collidepoint(x,y)):
				prizesdisplay = 0
				
			#showing prizes
			if (prizelist[0]==0):
				screen.blit(bear.image, bear.rect)
			if (prizelist[1]==0):
				screen.blit(car.image, car.rect)
			if (prizelist[2]==0):
				screen.blit(giftcard.image, giftcard.rect)
			if (prizelist[3]==0):
				screen.blit(ipod.image, ipod.rect)
			if (prizelist[4]==0):
				screen.blit(monkeys.image, monkeys.rect)
			if (prizelist[5]==0):
				screen.blit(snake.image, snake.rect)
			if (prizelist[6]==0):
				screen.blit(rainbowball.image, rainbowball.rect)
				
			
			
			pygame.display.flip()
		
		
		
	
		pygame.display.flip()
		
		
		
	pygame.display.update()

		
