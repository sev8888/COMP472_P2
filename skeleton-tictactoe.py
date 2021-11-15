# based on code from https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python

import time
import string
import array
from array import *
import os
import os.path as ospath

class Game:

 

	MINIMAX = 0
	ALPHABETA = 1
	HUMAN = 2
	AI = 3
	
	# init
	def __init__(self, recommend = True):
		self.initialize_game()
		self.recommend = recommend
	
	# build game board
	def initialize_game(self):
		#makes n by n matrix, n is defined in inputs before main (size of board)
		#fills with '.' for blank, '%' for bloc
		self.current_state = []
		for i in range(n):
			row = []
			for j in range(n):
				if(b>0):
					for k in range(0,b):
						if(bloc_positions[k][0] == i and bloc_positions[k][1] ==  j):
							print(str(i))
							print(str(j))
							print(str(bloc_positions[k][0]))
							print(str(bloc_positions[k][1]))
							print("\n")
							row.append('%')
						else:
							row.append('.')
				else:
					row.append('.')
			self.current_state.append(row)

		# Player X always plays first
		self.player_turn = 'X'

	# print board layout
	def draw_board(self):
		# col(x) = A, B, C, ...
		# row(y) = 1, 2, 3, ...
		print()
		print("   ", end="")
		for x in range(0, n):
			print(F'{chr(65+x)}', end=" ")
		print("\n ■", end="")
		for x in range(0, 2*n+1):
			print(F'-', end="")
		print("■")
		for y in range(0, n):
			print(F'{y}| ', end="")
			for x in range(0, n):
				print(F'{self.current_state[x][y]}', end=" ")
			print("|")
		print(" ■", end="")
		for x in range(0, 2*n+1):
			print(F'-', end="")
		print("■")
		print()

	# check if move is valid @return True,False	
	def is_valid(self, px, py):
		if px < 0 or px >= n or py < 0 or py >= n:
			return False
		elif self.current_state[px][py] != '.':
			return False
		else:
			return True

	# check if game has winner @return 'X','O','.',None
	def is_end(self):
		# Vertical win
		for x in range(0,n):  #column
			current_winner = 'X'
			current_count = 0 
			for y in range (0, n): #row
				if(self.current_state[x][y] == current_winner):
					current_count = current_count + 1
					if((current_winner == 'X' or current_winner == 'O') and current_count >= s):
						#print("vertical win")
						return current_winner
				else:
					current_winner = self.current_state[x][y]
					current_count = 0
		
		# Horizontal win
		for y in range(0,n):  #row
			current_winner = 'X'
			current_count = 0 
			for x in range (0, n): #column
				if(self.current_state[x][y] == current_winner):
					current_count = current_count + 1
					if((current_winner == 'X' or current_winner == 'O') and current_count >= s):
						#print("horizontal win")
						return current_winner
				else:
					current_winner = self.current_state[x][y]
					current_count = 0

		# Main diagonal win
		for i in range(-(n-s), n-s+1):
			current_winner = 'X'
			current_count = 0 
			for j in range(n-abs(i)):
				if(self.current_state[i+j if i>=0 else 0+j][0+j if i>=0 else abs(i)+j] == current_winner):
					current_count = current_count + 1
					if((current_winner == 'X' or current_winner == 'O') and current_count >= s):
						#print("diagonal win")
						return current_winner
				else:
					current_winner = self.current_state[i+j if i>=0 else 0+j][0+j if i>=0 else abs(i)+j]
					current_count = 1
				#print(F'[{0+j if i>=0 else abs(i)+j}][{0+j if i<=0 else i+j}]->{self.current_state[0+j if i>=0 else abs(i)+j][0+j if i<=0 else i+j]}:{current_count}', end="")

		# Second diagonal win
		for i in range(-(n-s), n-s+1):
			current_winner = 'X'
			current_count = 0 
			for j in range(n-abs(i)):
				if(self.current_state[i+j if i>=0 else 0+j][(n-1)-j if i>=0 else (n-1)-abs(i)-j] == current_winner):
					current_count = current_count + 1
					if((current_winner == 'X' or current_winner == 'O') and current_count >= s):
						#print("diagonal2 win")
						return current_winner
				else:
					current_winner = self.current_state[i+j if i>=0 else 0+j][(n-1)-j if i>=0 else (n-1)-abs(i)-j]
					current_count = 1

		# Is whole board full?
		for i in range(0, n):
			for j in range(0, n):
				# While there is an empty field, we continue the game
				if (self.current_state[i][j] == '.'):
					return None
		# If there is no more moves, it's a tie!
		return '.'

	# print game result
	def check_end(self):
		self.result = self.is_end()
		# Printing the appropriate message if the game has ended
		if self.result != None:
			if self.result == 'X':
				print('The winner is X!')
			elif self.result == 'O':
				print('The winner is O!')
			elif self.result == '.':
				print("It's a tie!")
			self.initialize_game()
		return self.result

	# user move input (x,y)
	def input_move(self):
		while True:
			print(F'Player {self.player_turn}, enter your move:')
			#px = int(input('enter the x coordinate: '))
			strx = input('enter the x coordinate (char): ')
			px = int(ord(strx.upper()) - 65)
			stry = input('enter the y coordinate (num): ')
			if stry.isdigit():
				py = int(stry)
			else:
				py = 100
			if self.is_valid(px, py):
				return (px, py)
			else:
				print('The move is not valid! Try again.')

	def switch_player(self):
		if self.player_turn == 'X':
			self.player_turn = 'O'
		elif self.player_turn == 'O':
			self.player_turn = 'X'
		return self.player_turn

	def minimax(self, max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		value = 2
		if max:
			value = -2
		x = None
		y = None
		result = self.is_end()
		if result == 'X':
			return (-1, x, y)
		elif result == 'O':
			return (1, x, y)
		elif result == '.':
			return (0, x, y)
		for i in range(0, n):
			for j in range(0, n):
				if self.current_state[i][j] == '.':
					if max:
						self.current_state[i][j] = 'O'
						(v, _, _) = self.minimax(max=False)
						if v > value:
							value = v
							x = i
							y = j
					else:
						self.current_state[i][j] = 'X'
						(v, _, _) = self.minimax(max=True)
						if v < value:
							value = v
							x = i
							y = j
					self.current_state[i][j] = '.'
		return (value, x, y)

	def alphabeta(self, alpha=-2, beta=2, max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		value = 2
		if max:
			value = -2
		x = None
		y = None
		result = self.is_end()
		if result == 'X':
			return (-1, x, y)
		elif result == 'O':
			return (1, x, y)
		elif result == '.':
			return (0, x, y)
		for i in range(0, n):
			for j in range(0, n):
				if self.current_state[i][j] == '.':
					if max:
						self.current_state[i][j] = 'O'
						(v, _, _) = self.alphabeta(alpha, beta, max=False)
						if v > value:
							value = v
							x = i
							y = j
					else:
						self.current_state[i][j] = 'X'
						(v, _, _) = self.alphabeta(alpha, beta, max=True)
						if v < value:
							value = v
							x = i
							y = j
					self.current_state[i][j] = '.'
					if max: 
						if value >= beta:
							return (value, x, y)
						if value > alpha:
							alpha = value
					else:
						if value <= alpha:
							return (value, x, y)
						if value < beta:
							beta = value
		return (value, x, y)

	def e1(self,MaxScore,MinScore,first_player,second_player):
		# Maximizing for 'X' and minimizing for 'O'
		# first player will add 1, second player will minus 1 and blank will return 0
		calculation_score = 0
		for i in range(0,n):
			for j in range(0,n):
				if self.current_state[i][j]=='.':
					# if it is player1 turn
						if max:
							#calculate the value of its score
							# calculate score base on row
							for x in range (0,n):
								if self.current_state[i][x] == first_player:
									calculation_score = calculation_score + 1
								elif self.current_state[i][x] == second_player:
									calculation_score = calculation_score - 1
								elif self.current_state[i][x] == '.':
									calculation_score = calculation_score + 0
							# calculate score base on column
							for x in range (0,n):
								if self.current_state[x][i] == first_player:
									calculation_score = calculation_score + 1
								elif self.current_state[x][i] == second_player:
									calculation_score = calculation_score - 1
								elif self.current_state[x][i] == '.':
									calculation_score = calculation_score + 0
							# compare the calculation_score with the previous score
							if calculation_score > MaxScore:
								MaxScore = calculation_score
								self.current_state[i][j] = first_player
					# if it is player2 turn
						else:
							#calculate the value of its score
							# calculate score base on row
							for x in range (0,n):
								if self.current_state[i][x] == first_player:
									calculation_score = calculation_score + 1
								elif self.current_state[i][x] == second_player:
									calculation_score = calculation_score - 1
								elif self.current_state[i][x] == '.':
									calculation_score = calculation_score + 0
							# calculate score base on column
							for x in range (0,n):
								if self.current_state[x][i] == first_player:
									calculation_score = calculation_score + 1
								elif self.current_state[x][i] == second_player:
									calculation_score = calculation_score - 1
								elif self.current_state[x][i] == '.':
									calculation_score = calculation_score + 0
							
							# compare the calculation_score with the previous score
							if calculation_score < MinScore:
								MinScore = calculation_score
								self.current_state[i][j] = second_player

	def e2():
		return True

	def play(self,algo=None,player_x=None,player_o=None):
		if algo == None:
			algo = self.ALPHABETA
		if player_x == None:
			player_x = self.HUMAN
		if player_o == None:
			player_o = self.HUMAN
		while True:
			self.draw_board()
			if self.check_end():
				return
			if player_x == self.AI or player_o == self.AI or self.recommend: #only run ais when necessary
				start = time.time()
				if algo == self.MINIMAX:
					if self.player_turn == 'X':
						(_, x, y) = self.minimax(max=False)
					else:
						(_, x, y) = self.minimax(max=True)
				elif algo == self.ALPHABETA:
					if self.player_turn == 'X':
						(m, x, y) = self.alphabeta(max=False)
					else:
						(m, x, y) = self.alphabeta(max=True)
				end = time.time()
			if (self.player_turn == 'X' and player_x == self.HUMAN) or (self.player_turn == 'O' and player_o == self.HUMAN):
					if self.recommend:
						print(F'Evaluation time: {round(end - start, 7)}s')
						print(F'Recommended move: x = {x}, y = {y}')
					(x,y) = self.input_move()
			if (self.player_turn == 'X' and player_x == self.AI) or (self.player_turn == 'O' and player_o == self.AI):
						print(F'Evaluation time: {round(end - start, 7)}s')
						print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
			self.current_state[x][y] = self.player_turn
			self.switch_player()

def main():
	g = Game(recommend=False)
	if(modes == 1):
		g.play(algo=sel,player_x=Game.HUMAN,player_o=Game.HUMAN)
	elif(modes == 2):
		g.play(algo=sel,player_x=Game.HUMAN,player_o=Game.AI)
	elif(modes == 3):
		g.play(algo=sel,player_x=Game.AI,player_o=Game.HUMAN)
	else:
		g.play(algo=sel,player_x=Game.AI,player_o=Game.AI)

if __name__ == "__main__":
	#user inputs for game configuration
	alphabet_upper = list(string.ascii_uppercase)	#TODO change this shit
	alphabet_lower = list(string.ascii_lowercase)
	bloc_positions=[]
	print("Hello, welcome to the CLI\n")
	print("Please enter the following information:\n")

	print("==== the size of the board between 3 and 10\n")
	n = int(input())
	while(n > 10 or n < 3):
		print("please enter a value in the correct range (between 3 and 10")
		n = int(input())

	print("==== the number of blocs between 0 to "+str((2*n))+"\n")
	b = int(input())
	while(b > (2*n) or b < 0):
		print("please enter a value in the correct range (between 0 and "+str(2*n)+")\n")
		b = int(input())
	if(b>0):
		for i in range(b):
			bloc = []
			print("please enter the row number in the range of 0 to "+str(n-1)+" for bloc number "+str(i+1))
			row_temp = int(input())
			while(row_temp > n-1 or row_temp < 0):
				print("please enter a value in the correct range (between 0 to "+str(n-1)+")")
				row_temp = int(input())
			print("please enter the column letter in the range of A to "+str(alphabet_upper[n-1])+" for bloc number "+str(i+1))
			column_temp = input()
			column_tester = column_temp.upper()
			column_lower = column_temp.lower()
			while(column_temp.isalpha == False or (ord(column_tester)> ord(str(alphabet_upper[n-1])))):
				print("please enter the column letter in the range of A to "+str(alphabet_upper[n-1]))
				column_temp = input()
				column_tester = column_temp.upper()
				column_lower = column_temp.lower()
			bloc.insert(0,row_temp)
			column_number = int(ord(column_lower)-96-1)
			bloc.insert(1, column_number)
			bloc_positions.append(bloc)
		print(bloc_positions)
		#print(bloc_positions[0][0])

	print("==== the winning line-up size between 3 to "+str(n)+"\n")
	s = int(input())
	while(s > n or s < 3):
		print("please enter a value in the correct range (between 0 and "+str(n)+")\n")
		s = int(input())
	print("====  the maximum depth of adversarial search for player 1\n")
	d1 = int(input())
	print("====  the maximum depth of adversarial search for player 2\n")
	d2 = int(input())
	print("==== the maximum time allowed (in seconds) for the program to return a move\n")
	t = float(input())
	print("==== to force the use of minimax input  0, to force the use of alphabeta input 1\n")
	sel = bool(input())
	print("==== select the player configuration from the following options:\n"+
	"	1 for Human vs Human\n" + "	2 for Human vs AI (Human is player X)\n" + "	3 for AI vs Human (Human is player o)\n" + "	4 for AI vs AI")
	modes = int(input())
	while(modes > 4 or modes < 1):
		print("please enter either 1, 2, 3 or 4\n")
		modes = int(input())

	filename = "gamefile"+str(n)+str(b)+str(s)+str(t)+".txt"	
	#f=open(filename,'a' )

	if os.path.exists(filename):
 		 os.remove(filename)
	with open(filename,'a') as f:
		f.writelines("the value of the board size n is "+str(n)+"\n")
		f.writelines("the number of blocs b is "+str(b)+"\n")
		f.writelines("the value of the winning line-up s is "+str(s)+"\n")
		f.writelines("the value of the maximum allowed time for the program to return a move is "+str(t)+"\n")
		f.writelines("\nposition of blocs:\n")
		if(b>0):
			for i in bloc_positions:
				f.writelines(str(i) + '\n')
			f.writelines("\n")
		else:
			f.writelines("	N/A - there are no blocs\n"+"\n")
		if(sel == 1):
			f.writelines("Player 1: Human, "+"d is "+str(d1)+", a is " + str(sel)+"\n")
			f.writelines("Player 2: Human, "+"d is "+str(d2)+", a is " + str(sel)+"\n")
		elif(sel == 2):
			f.writelines("Player 1: Human, "+"d is "+str(d1)+", a is " + str(sel)+"\n")
			f.writelines("Player 2: AI, "+"d is "+str(d2)+", a is " + str(sel)+"\n")
		elif(sel == 3):
			f.writelines("Player 1: Human, "+"d is "+str(d1)+", a is " + str(sel)+"\n")
			f.writelines("Player 2: AI, "+"d is "+str(d2)+", a is " + str(sel)+"\n")
		else:
			f.writelines("Player 1: AI, "+"d is "+str(d1)+", a is " + str(sel)+"\n")
			f.writelines("Player 2: AI, "+"d is "+str(d2)+", a is " + str(sel)+"\n")

	main()

	f.close()

