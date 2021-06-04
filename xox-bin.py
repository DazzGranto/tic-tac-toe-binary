
"""
>> Grid
---	123
--- -> 	456
---	789

>> How to play

λ python xox-bin.py

---
---
---
O: 1

O--
---
---
X: 5

O--
-X-
---
O: 2
"""	

# Code
import random

WIN_CASES = [
	229376, 28672, 3584, 149504, 74752, 37376, 139776, 43008,
	448, 56, 7, 292, 146, 73, 273, 84
]

POSITON = {
	'X': [131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512],
	'O': [256, 128, 64, 32, 16, 8, 4, 2, 1]
}

class XOX():
	def __init__(self):
		self.grid = 0
		self.current_player = random.choice(['X', 'O'])
		self.tick = 0

	def add(self, player, pos):
		opposite_player = 'O' if player == 'X' else 'X'

		if self.grid & POSITON.get(opposite_player)[pos] != POSITON.get(opposite_player)[pos] and self.grid & POSITON.get(player)[pos] != POSITON.get(player)[pos]:
			self.grid |= POSITON.get(player)[pos]
		else:
			return -1

	def turn(self):
		selected_pos = int(input(f'{self.current_player}: ')) - 1

		add_result = self.add(self.current_player, selected_pos)

		if add_result == -1:
			print('Select another square.')
			return -1
		else:
			print(self.humanize_numbers())

			win = self.check_win()

			if self.tick == 8:
				print('\nX O TIE!')
				exit()
			elif win:
				print(f'\n{self.current_player} WON!')
				exit()
			
			self.current_player = 'O' if self.current_player == 'X' else 'X'
		self.tick += 1

	def check_win(self):
		for win in WIN_CASES:
			if self.grid & win == win:
				return True
				break

	def humanize_numbers(self):
		text = ''
		for pos in range(9):
			if self.grid & POSITON.get('X')[pos] == POSITON.get('X')[pos] and self.grid & POSITON.get('O')[pos] != POSITON.get('O')[pos]:
				text += 'X'
			elif self.grid & POSITON.get('X')[pos] != POSITON.get('X')[pos] and self.grid & POSITON.get('O')[pos] == POSITON.get('O')[pos]:
				text += 'O'
			else:
				text += '-'

		return '\n' + '\n'.join([text[i:i + 3] for i in range(0, len(text), 3)])


game = XOX()

print(game.humanize_numbers())

while True:
	try:
		game.turn()
	except KeyboardInterrupt:
		print('\n\n - Exiting...')
		exit()
