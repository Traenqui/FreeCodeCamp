import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **balls):
		self.contents = []
		for ball in balls:
			for i in range(balls[ball]):
				self.contents.append(ball)

	def draw(self, num):
		if num >= len(self.contents):
			tmp = self.contents.copy()
			self.contents.clear()
			return tmp
		tmp = []
		for i in range(num):
			n = random.choice(range(0, len(self.contents)))
			tmp.append(self.contents[n])
			self.contents.pop(n)
		return tmp


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	counter = 0
	for i in range(num_experiments):
		tmp = copy.deepcopy(hat)
		drawn = tmp.draw(num_balls_drawn)
		for j in expected_balls:
			if expected_balls[j] > drawn.count(j):
				counter -= 1
				break
		counter += 1
	return counter/num_experiments