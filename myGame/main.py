# content from kids can code: http://kidscancode.org/blog/
# content from geeks for geeks: https://www.geeksforgeeks.org/building-space-invaders-using-pygame-python/#
# content from pygame.org: https://www.pygame.org/docs/ref/mouse.html


'''

GameDesign:

Goals - complete the level/survive for as long as possible
Rules - kill aliens, don't let the aliens reach the player
Score counter at the top of the screen
Add harder levels as the game moves on or have harder enemies spawn

FeatureGoals:

Have new levels generate when all mobs are killed/current level is passed
Have new mobs increase in difficulty


'''

import pygame 
import pygame as pg
import os
import random
import math
from pygame import mixer
from settings import *
from sprites import *


import pygame
import random
import math
from pygame import mixer

# sets the directories for the images, sound, and game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# initializing pygame
pygame.init()






# adding a Score Counter in the top left corner of the screen
score_val = 0
scoreX = 5
scoreY = 5
# changing the font of the Score Counter
font = pygame.font.Font('freesansbold.ttf', 20)

# adding a Game Over screen when the invader reaches and collides with the player
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# function that adds score to the score counter
def show_score(x, y):
	# adds points when the bullet collides with the invader
	score = font.render("Points: " + str(score_val),
						True, (255,255,255))
	screen.blit(score, (x , y ))

# function that runs the game over screen when the requirements are met
def game_over():
	game_over_text = game_over_font.render("GAME OVER",
										True, (255,255,255))
	screen.blit(game_over_text, (190, 250))




# generating the invaders/mobs using randint
for num in range(no_of_invaders):
	invaderImage.append(pygame.image.load(os.path.join(img_folder, 'alien.png')))
	invader_X.append(random.randint(64, 737))
	invader_Y.append(random.randint(30, 180))
	invader_Xchange.append(1.2)
	invader_Ychange.append(50)


# initializing the collision function - when the invader collides with the player, and when the bullet collides with the invader
def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

# setting the player image (theBigBell.png)
def player(x, y):
	screen.blit(playerImage, (x - 16, y + 10))

# setting the invader image (alien.png)
def invader(x, y, i):
	screen.blit(invaderImage[i], (x, y))

# setting the bullet image (bullet.png)
def bullet(x, y):
	global bullet_state
	screen.blit(bulletImage, (x, y))
	bullet_state = "fire"


	
# game loop
running = True
while running:

	# detects if pygame is running or not
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# controlling the player movement
		# from the arrow keys, a and d, and space for firing the bullet
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_Xchange = -1.7
			if event.key == pygame.K_a:
				player_Xchange = -1.7
			if event.key == pygame.K_RIGHT:
				player_Xchange = 1.7
			if event.key == pygame.K_d:
				player_Xchange = 1.7
			if event.key == pygame.K_SPACE:
			
			
			
				# fixing the change of direction of bullet
				if bullet_state is "rest":
					bullet_X = player_X
					bullet(bullet_X, bullet_Y)
		if event.type == pygame.KEYUP:
			player_Xchange = 0

	# adding the change in the player position
	player_X += player_Xchange
	for i in range(no_of_invaders):
		invader_X[i] += invader_Xchange[i]

	# bullet movement
	bullet_angle = 0
	bullet_speed = 5
	if bullet_Y <= 0:
		bullet_Y = 600
		bullet_state = "rest"
	if bullet_state is "fire":
		bullet(bullet_X, bullet_Y)
		bullet_Y -= bullet_Ychange
		# send the bullet to the mouse position
		angle = math.atan2(pygame.mouse.get_pos()[1] - bullet_Y, pygame.mouse.get_pos()[0] - bullet_X)
		bullet_X += bullet_speed * math.cos(angle)
		
		

	# movement of the invader - when the invader reaches the limits of the screen, reverse the speed and have the invader move the opposite direction
	for i in range(no_of_invaders):
		if invader_Y[i] >= 450:
			if abs(player_X-invader_X[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y[j] = 2000
				game_over()
				break

		if invader_X[i] >= 735 or invader_X[i] <= 0:
			invader_Xchange[i] *= -1
			invader_Y[i] += invader_Ychange[i]
		# Collision initialization
		collision = isCollision(bullet_X, invader_X[i],
								bullet_Y, invader_Y[i])
		# if the bullet collides with the invader ... (increase score_val by 1, delete invader)
		if collision:
			score_val += 1
			bullet_Y = 600
			bullet_state = "rest"
			invader_X[i] = random.randint(64, 736)
			invader_Y[i] = random.randint(30, 200)
			invader_Xchange[i] *= -1

		invader(invader_X[i], invader_Y[i], i)


	# setting restraints on the player so that they always stay on screen/cannot move off screen
	
	if player_X <= 16:
		player_X = 16;
	elif player_X >= 750:
		player_X = 750


	player(player_X, player_Y)
	show_score(scoreX, scoreY)
	pygame.display.update()
