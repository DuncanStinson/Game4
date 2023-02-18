import pygame
import math
import random

screen = pygame.display.set_mode((800, 800))
start = 0
x = 370
y = 370
acceleration = 0
ax = 0
ay = 0
angle = 0
laser = False
laserangle = 0
laserx = 0
lasery = 0
lasert = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() 
			exit()

	#Background
	screen.fill((0,0,0))
	if(start == 0):
		starx = []
		stary = []
		for x1 in range(75):
			starx.append(random.randint(0, 800))
			stary.append(random.randint(0, 800))
	
		start += 1

	for a in range(75):
		pygame.draw.circle(screen,(255,255,230),(starx[a],stary[a]),3)



	#Rocks
	asteroid = pygame.image.load("ROCK.png")
	screen.blit(asteroid, (ax,ay))
	ay+=0.2
	ax+=0.2

	#Spaceship
	if acceleration > 2:
		ship = pygame.image.load("Spaceship1.png")
	else:
		ship = pygame.image.load("Spaceship.png")

	rotateship = pygame.transform.rotate(ship, angle)
	new_rect = rotateship.get_rect(center = ship.get_rect(topleft = (x,y)).center)
	screen.blit(rotateship, new_rect)

	#Movement(Fuel)
	keys = pygame.key.get_pressed()	

	if (keys[pygame.K_a] or keys[pygame.K_LEFT]): 
		angle += 2

	if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): 
		angle -= 2
	
	if (keys[pygame.K_s] or keys[pygame.K_DOWN]): 
		acceleration = -0.5


	if (keys[pygame.K_w] or keys[pygame.K_UP]): 
		acceleration = 2.5

	if acceleration > 0:
		acceleration -= 0.01
		y -= acceleration * math.cos(angle*3.14/180)
		x -= acceleration * math.sin(angle*3.14/180)

	if acceleration < 0:
		acceleration = 0
		
	#Out of bounds	
	if(x < -10):
		x = -10

	if(x > 750):
		x = 750

	if(y < -10):
		y = -10

	if(y > 730):
		y = 730




	#Angle(+) left side
	#Angle(-) right side
	if(angle >= 180):
		angle = -178

	if(angle <= -180):
		angle = 178


	#Shooting(takes time to reload)
	if (keys[pygame.K_SPACE]): 
		if(laser == False):
			laser = True
			laserangle = angle
			laserx = x
			lasery = y
			lasert = 100
		
	
	if(laser == True):
		lasery -= 7 * math.cos(laserangle*3.14/180)
		laserx -= 7 * math.sin(laserangle*3.14/180)
		lasert -= 1

		pygame.draw.rect(screen,(255,0,0),(laserx + 25,lasery+25, 20,20))

		if(lasert <= 0):
			laser = False
	

	pygame.display.update()
	pygame.event.pump()
