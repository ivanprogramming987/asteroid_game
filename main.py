import pygame
import sys
from constants import *
from logger import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
	print("Starting Asteroids with pygame version: " + pygame.version.ver)
	print("Screen width: " + str(SCREEN_WIDTH))
	print("Screen height: " + str(SCREEN_HEIGHT))
	# INITIALIZE
	pygame.init()
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	dt = 0
	score = 0
	time_survived = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	# GAME LOOP
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for a in asteroids:
			if a.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				print("Score: " + str(score))
				print("Survived for " + str(time_survived) + " seconds")
				sys.exit()
			for s in shots:
				if a.collides_with(s):
					log_event("asteroid_shot")
					a.split()
					s.kill()
					score += 1
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()
		r_val = clock.tick(60)
		dt = r_val / 1000
		time_survived += dt

if __name__ == "__main__":
	main()
