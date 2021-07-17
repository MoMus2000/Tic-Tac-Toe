import pygame
import random


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

		self.score = {
			'o':+100,
			"x":-100,
			'draw':0
		}
		self.total_depth = 0

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

		if pygame.mouse.get_pressed() != (0,0,0) and self.turn == "x":
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 0 and mouse_y <= 200):
				self.place_piece_human(0)
				pygame.draw.line(screen,BLACK,(0,0),(200,200),5)
				pygame.draw.line(screen,BLACK,(200,0),(0,200),5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 0 and mouse_y <= 200):
				self.place_piece_human(1)
				pygame.draw.line(screen,BLACK,(200,0),(400,200),5)
				pygame.draw.line(screen,BLACK,(400,0),(200,200),5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 0 and mouse_y <= 200):
				turn = self.place_piece_human(2)
				pygame.draw.line(screen,BLACK,(400,0),(600,200),5)
				pygame.draw.line(screen,BLACK,(600,0),(400,200),5)
			elif(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece_human(3)
				pygame.draw.line(screen,BLACK,(0,200),(200,400),5)
				pygame.draw.line(screen,BLACK,(200,200),(0,400),5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece_human(4)
				pygame.draw.line(screen,BLACK,(200,200),(400,400),5)
				pygame.draw.line(screen,BLACK,(400,200),(200,400),5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 200 and mouse_y <= 400):
				turn = self.place_piece_human(5)
				pygame.draw.line(screen,BLACK,(400,200),(600,400),5)
				pygame.draw.line(screen,BLACK,(600,200),(400,400),5)
			elif(mouse_x >= 0 and mouse_x <= 200 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece_human(6)
				pygame.draw.line(screen,BLACK,(0,400),(200,600),5)
				pygame.draw.line(screen,BLACK,(200,400),(0,600),5)
			elif(mouse_x >= 200 and mouse_x <= 400 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece_human(7)
				pygame.draw.line(screen,BLACK,(200,400),(400,600),5)
				pygame.draw.line(screen,BLACK,(400,400),(200,600),5)
			elif(mouse_x >= 400 and mouse_x <= 600 and mouse_y >= 400 and mouse_y <= 600):
				turn = self.place_piece_human(8)
				pygame.draw.line(screen,BLACK,(400,400),(600,600),5)
				pygame.draw.line(screen,BLACK,(600,400),(400,600),5)

		if self.turn == "o":
			index = self.best_move()
			print(index)
			if index == 0:
				pygame.draw.circle(screen,BLACK,(100,100),50,width = 5)
			elif index == 1:
				pygame.draw.circle(screen,BLACK,(300,100),50,width = 5)
			elif index == 2:
				pygame.draw.circle(screen,BLACK,(500,100),50,width = 5)
			elif index == 3:
				pygame.draw.circle(screen,BLACK,(100,300),50,width = 5)
			elif index == 4:
				pygame.draw.circle(screen,BLACK,(300,300),50,width = 5)
			elif index == 5:
				pygame.draw.circle(screen,BLACK,(500,300),50,width = 5)
			elif index == 6:
				pygame.draw.circle(screen,BLACK,(100,500),50,width = 5)
			elif index == 7:
				pygame.draw.circle(screen,BLACK,(300,500),50,width = 5)
			elif index == 8:
				pygame.draw.circle(screen,BLACK,(500,500),50,width = 5)

			return




	def place_piece_ai(self):
		possible_pos = []
		for i in range(0, len(self.quadrants)):
			if self.quadrants[i] == "":
				possible_pos.append(i)

		if len(possible_pos) != 0:
			index = random.choice(possible_pos)
			if index not in self.changed:
				self.quadrants[index] = "o"
				self.turn = "x"
				return index
		return -1


	def best_move(self):
		move = -1
		best_score = float('-inf')
		for i in range(0, len(self.quadrants)):
			if self.quadrants[i] == "":
				self.quadrants[i] = "o"
				score = self.minimax(0,False)
				self.quadrants[i] = ""
				if score > best_score:
					best_score = score
					move = i

		self.turn = "x"
		self.quadrants[move] = "o"
		print(f"{self.total_depth} possibilities analyzed")
		self.total_depth = 0
		return move


	def place_piece_human(self,index):
		if index not in self.changed:
			self.quadrants[index] = "x"
			self.changed.append(index)
			self.turn = "o"
		return


	

	def minimax(self, depth, is_maximizing):
		self.total_depth+=1
		result = self.check_win()
		if result != None:
			return self.score[result]

		if is_maximizing:
			best_score = float('-inf')
			for i in range(0,len(self.quadrants)):
				if self.quadrants[i] == "":
					self.quadrants[i] = "o"
					score = self.minimax(depth+1, False)
					self.quadrants[i] = ""
					best_score = max(score,best_score)

			return best_score

		else:
			best_score = float('inf')
			for i in range(0,len(self.quadrants)):
				if self.quadrants[i] == "":
					self.quadrants[i] = "x"
					score = self.minimax(depth+1, True)
					self.quadrants[i] = ""
					best_score = min(score,best_score)

			return best_score



	def check_win(self):
		first_row = self.quadrants[0:3]
		second_row = self.quadrants[3:6]
		third_row = self.quadrants[6:9]

		if first_row[0] == "o" and first_row[1] == "o" and first_row[2] == "o": return "o"
		if first_row[0] == "x" and first_row[1] == "x" and first_row[2] == "x": return "x"
		if second_row[0] == "o" and second_row[1] == "o" and second_row[2] == "o": return "o"
		if second_row[0] == "x" and second_row[1] == "x" and second_row[2] == "x": return "x" 
		if third_row[0] == "o" and third_row[1] == "o" and third_row[2] == "o": return "o"
		if third_row[0] == "x" and third_row[1] == "x" and third_row[2] == "x": return "x" 

		if first_row[0] == "o" and second_row[0] == "o" and third_row[0] == "o": return "o"
		if first_row[0] == "x" and second_row[0] == "x" and third_row[0] == "x": return "x"

		if first_row[1] == "o" and second_row[1] == "o" and third_row[1] == "o": return "o"
		if first_row[1] == "x" and second_row[1] == "x" and third_row[1] == "x": return "x"

		if first_row[2] == "o" and second_row[2] == "o" and third_row[2] == "o": return "o"
		if first_row[2] == "x" and second_row[2] == "x" and third_row[2] == "x": return "x"

		if first_row[0] == "o" and second_row[1] == "o" and third_row[2] == "o": return "o"
		if first_row[0] == "x" and second_row[1] == "x" and third_row[2] == "x": return "x"

		if first_row[2] == "o" and second_row[1] == "o" and third_row[0] == "o": return "o"
		if first_row[2] == "x" and second_row[1] == "x" and third_row[0] == "x": return "x"
		
		draw = [val != "" for val in self.quadrants]

		if all(draw):
			return "draw"

		return 

			




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

		if board.check_win() == None:
			board.draw()	


			
		clock.tick(FPS)
		pygame.display.update()




if __name__ == '__main__':
	main()