#from sklearn import linear_model
from scipy.stats.stats import pearsonr 

#clf = linear_model.LinearRegression()
#clf.fit([[getattr(t, 'x%d' % i) for i in range(1, 8)] for t in texts],
#        [t.y for t in texts])

#f = file('the_best_aptitude_test')

n_tests = int(raw_input())

def parse():
	n_cases = int(raw_input())
	#print n_cases

	final_data = {}

	final_data['gpa'] = [float(x) for x in raw_input().strip().split(' ')]

	data = []

	for i in range(5):
		data.append([float(x) for x in raw_input().strip().split(' ')])

	final_data['tests'] = data
	final_data['n_cases'] = n_cases
	#print final_data
	return final_data

def calculate_correlation(data):
	select = 1
	win_coef = 0

	for i in range(5):
		coef = pearsonr(data['gpa'],data['tests'][i])[0]
		if coef > win_coef or -coef > win_coef:
			win_coef = coef
			select = i+1
	return select

for i in range(n_tests):
	print calculate_correlation(parse())