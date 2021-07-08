class Category:

	def __init__(self, name: str):
		self.name = name
		self.ledger = []
		self.funds = 0

	def deposit(self, amount: float, description: str = ''):
		self.ledger.append({'amount': amount, 'description': description})
		self.funds += amount

	def withdraw(self, amount: float, description: str = ''):
		if self.check_funds(amount):
			self.ledger.append({'amount' : - amount, 'description': description})
			self.funds -= amount
			return True
		return False

	def get_balance(self):
		return self.funds 

	def transfer(self,amount: float, other):
		if not self.check_funds(amount):
			return False
		self.ledger.append({'amount': - amount, 'description': 'Transfer to {}'.format(other.name)})
		self.funds -= amount
		other.ledger.append({'amount': amount, 'description': 'Transfer from {}'.format(self.name)})
		other.funds += amount
		return True

	def check_funds(self, amount: float):
		if self.funds >= amount:
			return True
		return False

	def __str__(self):
		s=''
		s += self.name.center(30, '*') + '\n'
		for x in self.ledger:
			if len(x['description']) > 23:
				s += x['description'][0:23]
			else:
				s += x['description'][0:23].ljust(23)
			s += '{0:.2f}'.format(x['amount']).rjust(7)
			s += '\n'
		s += 'Total: {}'.format(self.funds)
		return s



def create_spend_chart(categories):
	res = 'Percentage spent by category\n'
	sum = 0
	withdraws = {}
	for x in categories:
		withdraws[x.name] = 0
		for y in x.ledger:
			if y['amount'] < 0:
				withdraws[x.name] += y['amount']
		withdraws[x.name] = - withdraws[x.name]

	# get total sum	
	for x in withdraws:
		sum += withdraws[x]

	# get the percentages
	for x in withdraws:
		withdraws[x] = int(withdraws[x] / sum * 100)

	# create the percentage 'bar'
	for i in range(100, -10, -10):
		res += str(i).rjust(3) + '| '
		for x in categories:
			if withdraws[x.name] >= i:
				res += 'o  '
			else:
				res += '   '
		res += '\n'
	res += ' ' * 4 + '-' * (1 + len(categories) * 3) + '\n'

	# get max length of catecories for chart
	maxlen = 0
	for x in categories:
		if len(x.name) > maxlen:
			maxlen = len(x.name)

	#
	for i in range(maxlen):
		res += ' ' * 5
		for x in categories:
			if len(x.name) > i:
				res += x.name[i] + '  '
			else:
				res += ' ' * 3
		res += '\n'
	return res[0:-1]





















