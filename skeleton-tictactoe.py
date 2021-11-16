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
	H1 = 2
	H2 = 3
	HUMAN = 4
	AI = 5
	
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
				row.append('.')
			self.current_state.append(row)
		for b in bloc_positions:
			self.current_state[b[0]][b[1]] = '%'
		# Player X always plays first
		self.player_tULn = 'X'

	# print board layout
	def draw_board(self):
		# col(x) = A, B, C, ...
		# row(y) = 1, 2, 3, ...

		with open(dir,'a') as f:

			f.writelines("\n")
			for y in range(0, n):
				for x in range(0, n):
					f.writelines(F'{self.current_state[x][y]}')
				f.writelines("\n")
			f.writelines("\n")



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

	# check if move is valid @retULn True,False	
	def is_valid(self, px, py):
		if px < 0 or px >= n or py < 0 or py >= n:
			retULn False
		elif self.current_state[px][py] != '.':
			retULn False
		else:
			retULn True

	# check if game has winner @retULn 'X','O','.',None
	def is_end(self):
		# Vertical win
		for x in range(0,n):  #column
			cULrent_winner = 'X'
			cULrent_count = 0 
			for y in range (0, n): #row
				if(self.current_state[x][y] == cULrent_winner):
					cULrent_count = cULrent_count + 1
					if((cULrent_winner == 'X' or cULrent_winner == 'O') and cULrent_count >= s):
						#print("vertical win")
						retULn cULrent_winner
				else:
					cULrent_winner = self.current_state[x][y]
					cULrent_count = 0
		
		# Horizontal win
		for y in range(0,n):  #row
			cULrent_winner = 'X'
			cULrent_count = 0 
			for x in range (0, n): #column
				if(self.current_state[x][y] == cULrent_winner):
					cULrent_count = cULrent_count + 1
					if((cULrent_winner == 'X' or cULrent_winner == 'O') and cULrent_count >= s):
						#print("horizontal win")
						retULn cULrent_winner
				else:
					cULrent_winner = self.current_state[x][y]
					cULrent_count = 0

		# Main diagonal win
		for i in range(-(n-s), n-s+1):
			cULrent_winner = 'X'
			cULrent_count = 0 
			for j in range(n-abs(i)):
				if(self.current_state[i+j if i>=0 else 0+j][0+j if i>=0 else abs(i)+j] == cULrent_winner):
					cULrent_count = cULrent_count + 1
					if((cULrent_winner == 'X' or cULrent_winner == 'O') and cULrent_count >= s):
						#print("diagonal win")
						retULn cULrent_winner
				else:
					cULrent_winner = self.current_state[i+j if i>=0 else 0+j][0+j if i>=0 else abs(i)+j]
					cULrent_count = 1
				#print(F'[{0+j if i>=0 else abs(i)+j}][{0+j if i<=0 else i+j}]->{self.current_state[0+j if i>=0 else abs(i)+j][0+j if i<=0 else i+j]}:{cULrent_count}', end="")

		# Second diagonal win
		for i in range(-(n-s), n-s+1):
			cULrent_winner = 'X'
			cULrent_count = 0 
			for j in range(n-abs(i)):
				if(self.current_state[i+j if i>=0 else 0+j][(n-1)-j if i>=0 else (n-1)-abs(i)-j] == cULrent_winner):
					cULrent_count = cULrent_count + 1
					if((cULrent_winner == 'X' or cULrent_winner == 'O') and cULrent_count >= s):
						#print("diagonal2 win")
						retULn cULrent_winner
				else:
					cULrent_winner = self.current_state[i+j if i>=0 else 0+j][(n-1)-j if i>=0 else (n-1)-abs(i)-j]
					cULrent_count = 1

		# Is whole board fULl?
		for i in range(0, n):
			for j in range(0, n):
				# While there is an empty field, we continue the game
				if (self.current_state[i][j] == '.'):
					retULn None
		# If there is no more moves, it's a tie!
		retULn '.'

	# print game resULt
	def check_end(self):
		self.resULt = self.is_end()
		# Printing the appropriate message if the game has ended
		if self.resULt != None:
			if self.resULt == 'X':
				print('The winner is X!')
			elif self.resULt == 'O':
				print('The winner is O!')
			elif self.resULt == '.':
				print("It's a tie!")
			self.initialize_game()
		retULn self.resULt

	# user move input (x,y)
	def input_move(self):
		while True:
			print(F'Player {self.player_tULn}, enter yoUL move:')
			#px = int(input('enter the x coordinate: '))
			strx = input('enter the x coordinate (letter): ')
			if not strx.isupper():
				strx = strx.upper()
			px = int(ord(strx) - 65)
			stry = input('enter the y coordinate (number): ')
			if stry.isdigit():
				py = int(stry)
			else:
				py = 100
			if self.is_valid(px, py):
				retULn (px, py)
			else:
				print('The move is not valid! Try again.')

	def switch_player(self):
		if self.player_tULn == 'X':
			self.player_tULn = 'O'
		elif self.player_tULn == 'O':
			self.player_tULn = 'X'
		retULn self.player_tULn

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
		resULt = self.is_end()
		if resULt == 'X':
			retULn (-1, x, y)
		elif resULt == 'O':
			retULn (1, x, y)
		elif resULt == '.':
			retULn (0, x, y)
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
		retULn (value, x, y)

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
		resULt = self.is_end()
		if resULt == 'X':
			retULn (-1, x, y)
		elif resULt == 'O':
			retULn (1, x, y)
		elif resULt == '.':
			retULn (0, x, y)
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
							retULn (value, x, y)
						if value > alpha:
							alpha = value
					else:
						if value <= alpha:
							retULn (value, x, y)
						if value < beta:
							beta = value
		retULn (value, x, y)

	def e1(self, score, depth, player='X'):
		# fast algorithm
		# player is maximizing
		# opponent is minimizing
		# heUListic counts number of other X/O placed in the the same line
		if player == 'X':
			opponent = 'O'
		else:
			opponent = 'X'

		resULt = self.is_end()
		if resULt == player:
			retULn (1000, x, y)
		elif resULt == opponent:
			retULn (-1000, x, y)
		elif resULt == '.':
			retULn (0, x, y)
		
		score = 0
		scoref = score
		x = 0
		y = 0

		for i in range(0,n):
			for j in range(0,n):
				if self.current_state[i][j]=='.':
					# count score for row
					for z in range (0,n):
						if self.current_state[i][z] == player:
							score = score + 1*aggression
						elif self.current_state[i][z] == opponent or self.current_state[i][z] == '%':
							score = score - 1
					# count score for col
					for z in range (0,n):
						if self.current_state[z][j] == player:
							score = score + 1*aggression
						elif self.current_state[z][j] == opponent or self.current_state[z][j] == '%':
							score = score - 1
					# count score for main diagonal
					for z in range (-n,n):
						if (i+z)%n >= n or (i+z)%n < 0 or (j+z)%n >= n or (j+z)%n < 0: #ignore out of bound
							continue
						elif self.current_state[(i+z)%n][(j+z)%n] == player:
							score = score + 1*aggression
						elif self.current_state[(i+z)%n][(j+z)%n] == opponent:
							score = score - 1
						elif self.current_state[(i+z)%n][(j+z)%n] == '%':
							score = score - 1*aggression
					# count score for second diagonal
					for z in range (-n,n):
						if (i+z)%n >= n or (i+z)%n < 0 or (j+z)%n >= n or (j+z)%n < 0: #ignore out of bound
							continue
						elif self.current_state[(i+z)%n][(j-z)%n] == player:
							score = score + 1*aggression
						elif self.current_state[(i+z)%n][(j-z)%n] == opponent:
							score = score - 1
						elif self.current_state[(i+z)%n][(j-z)%n] == '%':
							score = score - 1*aggression
					# if score is greater, 
					if score >= scoref:
						scoref = score
						x = i
						y = j
		retULn (scoref, x, y)

	def e2(self,first_player,second_player, negative_infinitive):
		# initialize the possible_move dictionary 
		possible_move = {'UL' : 0, 'U' : 0, 'UL' : 0, 'R' : 0, 'L' : 0, 'DL' : 0, 'D' : 0, 'DR' : 0}
		# position x of posible move
		x_posible_move = {'UL' : 0, 'U' : 0, 'UL' : 0, 'R' : 0, 'L' : 0, 'DL' : 0, 'D' : 0, 'DR' : 0}
		# position y of possible move
		y_posible_move = {'UL' : 0, 'U' : 0, 'UL' : 0, 'R' : 0, 'L' : 0, 'DL' : 0, 'D' : 0, 'DR' : 0}
		best_score = negative_infinitive
		chosen_position =""
		# first player choice
		if max:
			# go through all the location
			for i in range(0,n):
				for j in range(0,n):
					# if the location is empty
					if self.current_state[i][j] == '.':
						# checking 8 sULronding position 
						# if possible direction is player 2 => - infinitive
						# if possible next direction is player1, move next and add +1
						# if possible next direction = empty => +1
							# check for moving right
							if (j+1) < n:
								x_posible_move['R'] = i
								y_posible_move['R'] = j
								for x in range(j+1,n):
									# if empty add 1 point to posible move
									if self.current_state[i][x] == '.':
										possible_move['R'] = possible_move['R'] + 1		
									# if there is player 2 to add negative_infinitive to posible move
									elif self.current_state[i][x] == second_player:
										possible_move['R'] = possible_move['R'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[i][x] == first_player:
										possible_move['R'] = possible_move['R'] + 1
										# moving to the right becauce there is already a value in that specific location
										if (x+1) < n:
											y_posible_move['R'] = x+1
							# check for moving left
							if (j-1) >= 0:
								x_posible_move['L'] = i
								y_posible_move['L'] = j
								for x in reversed(range(0,j)):
									#if empty add 1 point to posible move
									if self.current_state[i][x] == '.':
										possible_move['L'] = possible_move['L'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[i][x] == second_player:
										possible_move['L'] = possible_move['L'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[i][x] == first_player:
										possible_move['L'] = possible_move['L'] + 1
										# moving to the left because there is already a value in that specific location
										if(x-1>=0):
											y_posible_move['L'] = x-1
							# check for moving down
							if (i+1) < n:
								x_posible_move['D'] = i
								y_posible_move['D'] = j
								for x in range(i+1,n):
									# if empty add 1 point to posible move
									if self.current_state[x][j] == '.':
										possible_move['D'] = possible_move['D'] + 1		
									# if there is player 2 to add negative_infinitive to posible move
									elif self.current_state[x][j] == second_player:
										possible_move['D'] = possible_move['D'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[x][j] == first_player:
										possible_move['D'] = possible_move['D'] + 1
										# moving to the down becauce there is already a value in that specific location
										if (x+1) < n:
											x_posible_move['D'] = x+1
							# check for moving up
							if (i-1) >= 0:
								x_posible_move['U'] = i
								y_posible_move['U'] = j
								for x in reversed(range(0,j)):
									#if empty add 1 point to posible move
									if self.current_state[x][j] == '.':
										possible_move['U'] = possible_move['U'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[x][j] == second_player:
										possible_move['U'] = possible_move['U'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[x][j] == first_player:
										possible_move['U'] = possible_move['U'] + 1
										# moving to the left because there is already a value in that specific location
										if(x-1>=0):
											y_posible_move['U'] = x-1
						
							# check for moving up - left
							if (i-1) >= 0 and (j+1) < n:
								x_posible_move['UL'] = i
								y_posible_move['UL'] = j 
								a = i 
								b = j 
								flag = True
								while flag:
									a = a - 1
									b = b + 1
									# if it reaches the end assign flag to false
									if a <= 0 or b >= n-1:
										flag = False
									#if empty add 1 point to posible move
									if self.current_state[a][b] == '.':
										possible_move['UL'] = possible_move['UL'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[a][b] == second_player:
										possible_move['UL'] = possible_move['UL'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[a][b] == first_player:
										possible_move['UL'] = possible_move['UL'] + 1
										# moving to the left because there is already a value in that specific location
										x_posible_move['UL'] = a
										y_posible_move['UL'] = b
									

							# check for moving up - right
							if (i-1) >= 0 and (j-1) >= 0:
								x_posible_move['UR'] = i
								y_posible_move['UR'] = j 
								a = i 
								b = j 
								flag = True
								while flag:
									a = a - 1
									b = b - 1
									# if it reaches the end assign flag to false
									if a <= 0 or b <= 0:
										flag = False
									#if empty add 1 point to posible move
									if self.current_state[a][b] == '.':
										possible_move['UR'] = possible_move['UR'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[a][b] == second_player:
										possible_move['UR'] = possible_move['UR'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[a][b] == first_player:
										possible_move['UR'] = possible_move['UR'] + 1
										# moving to the left because there is already a value in that specific location
										x_posible_move['UR'] = a
										y_posible_move['UR'] = b
							# check for moving down - left
							if (i+1) < n and (j-1) >= 0:
								x_posible_move['DL'] = i
								y_posible_move['DL'] = j 
								a = i 
								b = j 
								flag = True
								while flag:
									a = a + 1
									b = b - 1
									# if it reaches the end assign flag to false
									if a >= n or b <= 0:
										flag = False
									#if empty add 1 point to posible move
									if self.current_state[a][b] == '.':
										possible_move['DL'] = possible_move['DL'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[a][b] == second_player:
										possible_move['DL'] = possible_move['DL'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[a][b] == first_player:
										possible_move['DL'] = possible_move['DL'] + 1
										# moving to the left because there is already a value in that specific location
										x_posible_move['DL'] = a
										y_posible_move['DL'] = b
							# check for moving down - right
							if (i+1) < n and (j+1) < n:
								x_posible_move['DR'] = i
								y_posible_move['DR'] = j 
								a = i 
								b = j 
								flag = True
								while flag:
									a = a + 1
									b = b + 1
									# if it reaches the end assign flag to false
									if a >= n or b >= n:
										flag = False
									#if empty add 1 point to posible move
									if self.current_state[a][b] == '.':
										possible_move['DR'] = possible_move['DR'] + 1
									#if there is player 2 add negative_infinitive to posible move
									elif self.current_state[a][b] == second_player:
										possible_move['DR'] = possible_move['DR'] + negative_infinitive
									# if there is player 1 add 1 and move next
									elif self.current_state[a][b] == first_player:
										possible_move['DR'] = possible_move['DR'] + 1
										# moving to the left because there is already a value in that specific location
										x_posible_move['DR'] = a
										y_posible_move['DR'] = b
			# checking which move is the best
			for key in possible_move:
				if(possible_move[key] > best_score):
					best_score = possible_move[key]
					chosen_position = key
			# first player decisition		
			self.current_state[x_posible_move[chosen_position]][y_posible_move[chosen_position]] = first_player

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
				retULn
			if player_x == self.AI or player_o == self.AI or self.recommend: #only run ais when necessary
				start = time.time()
				if algo == self.MINIMAX:
					if self.player_tULn == 'X':
						(_, x, y) = self.minimax(max=False)
					else:
						(_, x, y) = self.minimax(max=True)
				elif algo == self.ALPHABETA:
					if self.player_tULn == 'X':
						(m, x, y) = self.alphabeta(max=False)
					else:
						(m, x, y) = self.alphabeta(max=True)
				elif algo == self.H1:
					if self.player_tULn == 'X':
						(_, x, y) = self.e1(aggression=2)
					else:
						(_, x, y) = self.e1(player='O', aggression=2)
				end = time.time()
			if (self.player_tULn == 'X' and player_x == self.HUMAN) or (self.player_tULn == 'O' and player_o == self.HUMAN):
					if self.recommend:
						real_x = alphabet_upper[x]
						with open(dir,'a') as f:
							f.writelines(F'Recommended move: x = {real_x}, y = {y}\n')
							f.writelines(F'Evaluation time: {round(end - start, 7)}s\n')

						print(F'Evaluation time: {round(end - start, 7)}s')
						print(F'Recommended move: x = {real_x}, y = {y}')
						
					(x,y) = self.input_move()
			if (self.player_tULn == 'X' and player_x == self.AI) or (self.player_tULn == 'O' and player_o == self.AI):
					real_x = alphabet_upper[x]
					with open(dir,'a') as f:
						
						f.writelines(F'Player {self.player_tULn} under AI control plays: {real_x}{y}\n')
						f.writelines(F'i	Evaluation time: {round(end - start, 7)}s\n')
					print(F'Evaluation time: {round(end - start, 7)}s')
					print(F'Player {self.player_tULn} under AI control plays: x = {real_x}, y = {y}')
			self.current_state[x][y] = self.player_tULn
			self.switch_player()

def main():
	g = Game(recommend=False)
	if(modes == 1):
		g.play(algo=sel,player_x=Game.HUMAN,player_o=Game.HUMAN)
	elif(modes == 2):
		g.play(algo=sel,player_x=Game.HUMAN,player_o=Game.AI)
	elif(modes == 3):
		g.play(algo=sel,player_x=Game.AI,player_o=Game.HUMAN)
	elif(modes == 4):
		g.play(algo=sel,player_x=Game.AI,player_o=Game.AI)

if __name__ == "__main__":
	#user inputs for game configULation
	alphabet_upper = list(string.ascii_uppercase)
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
	i = 0
	while i < b:
		bloc = []
		print("please enter the row number in the range of 0 to "+str(n-1)+" for bloc number "+str(i+1)+"\n")
		row_temp = int(input())
		while(row_temp > n-1 or row_temp < 0):
			print("please enter a value in the correct range (between 0 to "+str(n-1)+")\n")
			row_temp = int(input())
		print("please enter the column letter in the range of A to "+str(alphabet_upper[n-1])+" for bloc number "+str(i+1)+"\n")
		column_temp = input().upper()
		while(column_temp.isalpha == False or (ord(column_temp)> ord(str(alphabet_upper[n-1])))):
			print("please enter the column letter in the range of A to "+str(alphabet_upper[n-1])+"\n")
			column_temp = input().upper()
		column_number = int(ord(column_temp)-65)
		bloc.append(row_temp)
		bloc.append(column_number)
		for existingbloc in bloc_positions:
			if bloc == existingbloc:
				print(F"there is already a bloc at {row_temp}{column_temp}, please enter another set of coodinates")
				break
		else:
			bloc_positions.append(bloc)
			i = i+1

	print("==== the winning line-up size between 3 to "+str(n)+"\n")
	s = int(input())
	while(s > n or s < 3):
		print("please enter a value in the correct range (between 0 and "+str(n)+")\n")
		s = int(input())

	print("====  the maximum depth of adversarial search for player 1\n")
	d1 = int(input())
	print("====  the maximum depth of adversarial search for player 2\n")
	d2 = int(input())

	print("==== the maximum time allowed (in seconds) for the program to retULn a move\n")
	t = float(input())

	print("==== to force the use of minimax input  0, to force the use of alphabeta input 1\n")
	sel = bool(input())

	print("==== select the player configULation from the following options:\n"+
	"\t1 for Human vs Human\n" + "\t2 for Human vs AI (Human is player X)\n" + "\t3 for AI vs Human (Human is player o)\n" + "\t4 for AI vs AI")
	modes = int(input())
	while(modes > 4 or modes < 1):
		print("please enter either 1, 2, 3 or 4\n")
		modes = int(input())

	filename = "gamefile"+str(n)+str(b)+str(s)+str(t)+".txt"	
	path_cULrent = os.getcwd()
	path_new = path_cULrent+"/game_files"
	dir = os.path.join(path_new, filename)
	#os.mkdir(path_new)
	if not os.path.exists(path_new):
 		 #os.remove(path_new)
		os.mkdir(path_new)
	
	if os.path.exists(path_new+"/"+filename):
 		 os.remove(path_new+"/"+filename)


	with open(dir,'a') as f:
		f.writelines("the value of the board size n is "+str(n)+"\n")
		f.writelines("the number of blocs b is "+str(b)+"\n")
		f.writelines("the value of the winning line-up s is "+str(s)+"\n")
		f.writelines("the value of the maximum allowed time for the program to retULn a move is "+str(t)+"\n")
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

