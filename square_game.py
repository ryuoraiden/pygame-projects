import pygame
import random
import sys

pygame.init()

width,height = 1700,1000

screen = pygame.display.set_mode((width,height))
goal = pygame.Rect(random.randint(30,width-30), random.randint(30,height-30), 30, 30)
player = pygame.Rect(800,500,70,70)
font = pygame.font.SysFont(None, 36)

enemy = pygame.Rect(random.randint(30,width-30), random.randint(30,height-30), 70, 70)
enemy_dx = random.choice([-5,5])
enemy_dy = random.choice([-5,5])

running = True

clock = pygame.time.Clock()
speed = 20

white = (250,250,250)
red = (250,0,0)
green = (0,250,0)
blue = (0,0,250)
black = (0,0,0)

pygame.display.set_caption('Square Game')

score = 0
game_over = False

while running:
	clock.tick(60)

	screen.fill(black)

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	if not game_over:
		pygame.draw.rect(screen, blue, player)
		pygame.draw.rect(screen, green, goal)
		pygame.draw.rect(screen, red, enemy)

		key = pygame.key.get_pressed()
		if key[pygame.K_a] and player.left > 0:
			player.x -= speed
		elif key[pygame.K_d] and player.right < width:
			player.x += speed
		elif key[pygame.K_w] and player.top > 0:
			player.y -= speed
		elif key[pygame.K_s] and player.bottom < height:
			player.y += speed

		enemy.x += enemy_dx*2
		enemy.y += enemy_dy*2

		if enemy.left <= 0 or enemy.right >= width:
			enemy_dx *= -1
		if enemy.top <=0 or enemy.bottom >= height:
			enemy_dy *= -1

		if player.colliderect(enemy):
			game_over = True

		if player.colliderect(goal):
			score += 1
			goal.x = (random.randint(0,width-100))
			goal.y = (random.randint(0,height-100))
		score_text = font.render(f"Score: {score} ", True, white)
		screen.blit(score_text, (10,10))

	else:
		game_over_text = font.render("Game Over!", True, white)
		final_score = font.render(f"Final Score: {score}", True, white)
		screen.blit(game_over_text, (width//2 - 80, height//2 - 30))	
		screen.blit(final_score, (width//2 - 100, height//2 + 10))

	pygame.display.update()


pygame.quit()
sys.exit()	