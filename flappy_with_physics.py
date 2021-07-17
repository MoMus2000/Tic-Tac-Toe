import pygame
import pymunk
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)	

space = pymunk.Space()

space.gravity = 0, -100

FPS = 30

ball_radius = 10


def convert_coordinates(position):
	return int(position[0]), int(HEIGHT - position[1])

class Ball:
	def __init__(self):
		self.body = pymunk.Body()
		self.body.position = 200, 400
		self.shape = pymunk.Circle(self.body, ball_radius)
		self.shape.density = 1
		self.shape.elasticity = 1
		space.add(self.body,self.shape)


	def draw(self):
		pygame.draw.circle(screen,BLACK, convert_coordinates(self.body.position),ball_radius)


class Floor:
	def __init__(self):
		self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
		self.segment = pymunk.Segment(self.body,(0,100),(600,100),4)
		self.segment.elasticity = 0.5
		space.add(self.body, self.segment)

	def draw(self):
		pygame.draw.line(screen,BLACK,convert_coordinates((0,100)),convert_coordinates((600,100)),4)



class Pipe:
	def __init__(self, pos):
		self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
		self.body.position = pos
		self.shape = pymunk.Poly.create_box(self.body, (100, 200))
		space.add(self.body, self.shape)

	def draw(self):
		x, y = convert_coordinates(self.body.position)
		pygame.draw.rect(screen,(BLACK),(x,y,100,200))



def main():
	running = True
	clock = pygame.time.Clock()
	ball = Ball()
	floor = Floor()
	pipe = Pipe((400,400))
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill(WHITE)


		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			ball.body.velocity = 100,10

		if keys[pygame.K_LEFT]:
			ball.body.velocity = -100,10

		if keys[pygame.K_UP]:
			ball.body.velocity = 0,100



		ball.draw()
		floor.draw()
		pipe.draw()

		clock.tick(FPS)
		space.step(1/FPS)
		pygame.display.update()



if __name__ == '__main__':
	main()
