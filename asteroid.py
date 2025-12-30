import random
from circleshape import *
from constants import *
from logger import *
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		colors = ["red", "orange", "yellow", "green", "blue", "purple"]
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		log_event("asteroid_split")
		angle = random.uniform(20, 50)
		a_one_vector = self.velocity.rotate(angle)
		a_two_vector = self.velocity.rotate(0-angle)
		a_new_radius = self.radius - ASTEROID_MIN_RADIUS
		a_one = Asteroid(self.position.x, self.position.y, a_new_radius)
		a_two = Asteroid(self.position.x, self.position.y, a_new_radius)
		a_one.velocity = a_one_vector * 1.2
		a_two.velocity = a_two_vector * 1.2
