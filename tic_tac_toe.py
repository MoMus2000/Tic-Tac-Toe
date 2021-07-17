import pygame



WIDTH = 600
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)

class Board:

	def __init__(self):
		self.turn = "x"
		self.game_win = False
		self.game_draw = False
		self.counter = 1
		self.quadrants = ["","","",
						  "","","",
						  "","",""]
		self.changed = []

	def draw(self):
		#Horizontal lines
		pygame.draw.line(screen,BLACK,(0,0),(600,0),4)
		pygame.draw.line(screen,BLACK,(0,200),(600,200),4)
		pygame.draw.line(screen,BLACK,(0,400),(600,400),4)
		pygame.draw.line(screen,BLACK,(0,600),(600,600),4)

		#Vertical lines
		pygame.draw.line(screen,BLACK,(0,0),(0,600),4)
		pygame.draw.line(screen,BLACK,(200,0),(200,600),4)
		pygame.draw.line(screen,BLACK,(400,0),(400,600),4)
		pygame.draw.line(screen,BLACK,(600,0),(600,600),4)

		if pygame.mouse.get_pressed() != (0,0,0):
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 0 and mouse_y <= 200):
				turn = self.place_piece(0)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(0,0),(200,200),5)
					pygame.draw.line(screen,BLACK,(200,0),(0,200),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(100,100),50,width = 5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 0 and mouse_y <= 200):
				turn = self.place_piece(1)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(200,0),(400,200),5)
					pygame.draw.line(screen,BLACK,(400,0),(200,200),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(300,100),50,width = 5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 0 and mouse_y <= 200):
				turn = self.place_piece(2)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(400,0),(600,200),5)
					pygame.draw.line(screen,BLACK,(600,0),(400,200),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(500,100),50,width = 5)
			elif(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece(3)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(0,200),(200,400),5)
					pygame.draw.line(screen,BLACK,(200,200),(0,400),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(100,300),50,width = 5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece(4)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(200,200),(400,400),5)
					pygame.draw.line(screen,BLACK,(400,200),(200,400),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(300,300),50,width = 5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece(5)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(400,200),(600,400),5)
					pygame.draw.line(screen,BLACK,(600,200),(400,400),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(500,300),50,width = 5)
			elif(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece(6)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(0,400),(200,600),5)
					pygame.draw.line(screen,BLACK,(200,400),(0,600),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(100,500),50,width = 5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece(7)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(200,400),(400,600),5)
					pygame.draw.line(screen,BLACK,(400,400),(200,600),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(300,500),50,width = 5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece(8)
				if turn == "x":
					pygame.draw.line(screen,BLACK,(400,400),(600,600),5)
					pygame.draw.line(screen,BLACK,(600,400),(400,600),5)
				elif turn == "o":
					pygame.draw.circle(screen,BLACK,(500,500),50,width = 5)





	def place_piece(self,index):
		if index not in self.changed:
			turn = self.turn
			self.quadrants[index] = self.turn
			if self.turn == "x":
				self.turn = "o"
			elif self.turn == "o":
				self.turn = "x"
			self.changed.append(index)
			return turn
		return


	def check_win(self):
		first_row = self.quadrants[0:3]
		second_row = self.quadrants[3:6]
		third_row = self.quadrants[6:9]

		if first_row[0] == "o" and first_row[1] == "o" and first_row[2] == "o": return True
		if first_row[0] == "x" and first_row[1] == "x" and first_row[2] == "x": return True
		if second_row[0] == "o" and second_row[1] == "o" and second_row[2] == "o": return True
		if second_row[0] == "x" and second_row[1] == "x" and second_row[2] == "x": return True 
		if third_row[0] == "o" and third_row[1] == "o" and third_row[2] == "o": return True
		if third_row[0] == "x" and third_row[1] == "x" and third_row[2] == "x": return True 

		if first_row[0] == "o" and second_row[0] == "o" and third_row[0] == "o": return True
		if first_row[0] == "x" and second_row[0] == "x" and third_row[0] == "x": return True

		if first_row[1] == "o" and second_row[1] == "o" and third_row[1] == "o": return True
		if first_row[1] == "x" and second_row[1] == "x" and third_row[1] == "x": return True

		if first_row[2] == "o" and second_row[2] == "o" and third_row[2] == "o": return True
		if first_row[2] == "x" and second_row[2] == "x" and third_row[2] == "x": return True

		if first_row[0] == "o" and second_row[1] == "o" and third_row[2] == "o": return True
		if first_row[0] == "x" and second_row[1] == "x" and third_row[2] == "x": return True

		if first_row[2] == "o" and second_row[1] == "o" and third_row[0] == "o": return True
		if first_row[2] == "x" and second_row[1] == "x" and third_row[0] == "x": return True
		return False


	def minimax(self):
		pass
			




def main():
	FPS = 30
	clock = pygame.time.Clock()
	running = True
	board = Board()
	screen.fill(WHITE)
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if not board.check_win():
			board.draw()
			
		clock.tick(FPS)
		pygame.display.update()




if __name__ == '__main__':
	main()