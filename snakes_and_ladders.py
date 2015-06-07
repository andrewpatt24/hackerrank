## Board is always 10x10
from random import random
## given the biased die probabilities

#file = sys.stdin
n_games = int(raw_input())

def parse_game_data():
	dict_temp = {}

	dict_temp['game'] = i

	dict_temp['dice_prob'] = [float(x) for x in raw_input().strip().split(',')]

	s_l = raw_input().strip().split(',')

	snakes_ladders = raw_input() + " " + raw_input()
	snakes_ladders = snakes_ladders.strip().split(' ')
	sl_array = []
	for sl in snakes_ladders:
		sl_array.append(sl.split(','))
	
	dict_temp['snakes_and_ladders'] = [[int(x),int(y)] for x,y in sl_array]
	#print dict_temp['snakes_and_ladders']
	return dict_temp

def roll_dice(dice_prob):
	rval = random()
	#print rval

	for i in range(len(dice_prob)):
		if i==0:
			if rval < dice_prob[0]:
				#print dice_prob[0]
				return i+1
		else:
			if rval < sum(dice_prob[0:(i+1)]):
				#print sum(dice_prob[0:(i+1)])
				return i+1

def is_snake_or_ladder(num,array_pairs):
	for x, y in array_pairs:
		if x == num:
			return y

def one_go(start_point, game_dict):
	roll_end = start_point + roll_dice(game_dict['dice_prob'])
	test = is_snake_or_ladder(roll_end,game_dict['snakes_and_ladders'])
	if test is not None:
		return test
	return roll_end

def one_game(game_dict,nstop=100):
	start_point = 1
	for i in range(nstop):
		next_point = one_go(start_point,game_dict)
		if next_point == 100:
			return i+1
		elif next_point < 100:
			start_point = next_point

def simulate_game(game_dict,sims=5000,nstop=1000):
	output = []
	while len(output) < (sims-1):
		game_moves = one_game(game_dict,nstop=nstop)
		if game_moves is not None:
			output.append(game_moves)
	return output

def simulate_over_games(game_dict):
	game_moves_sim =  simulate_game(game_dict)
	return sum(game_moves_sim)/len(game_moves_sim)

for i in range(n_games):
	print simulate_over_games(parse_game_data())









