import pygame
from constants import *
from circleshape import *
from shot import *
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.shot_time = 0
		self.rotation = 0
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
	def rotate(self, dt):
		self.rotation = self.rotation + PLAYER_TURN_SPEED * dt
	def move(self, dt):
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		moving_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += moving_vector
	def shoot(self):
		if self.shot_time > 0:
			return
		x = self.position.x
		y = self.position.y
		shot = Shot(x, y, SHOT_RADIUS)
		shot_vector = pygame.Vector2(0, 1)
		rotated_shot_vector = shot_vector.rotate(self.rotation)
		moving_shot_vector = rotated_shot_vector * PLAYER_SHOOT_SPEED
		shot.velocity = moving_shot_vector
		self.shot_time = PLAYER_SHOOT_COOLDOWN_SECONDS
	def update(self, dt):
		self.shot_time -= dt
		keys = pygame.key.get_pressed()
		neg_dt = 0 - dt
		if keys[pygame.K_a]:
			self.rotate(neg_dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(neg_dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
