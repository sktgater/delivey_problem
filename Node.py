# Class Node that saves previous path in a list and the current point

class Node(object):
	def __init__(self, prev, cur):
		# type prev: List[Tuple]
		# type cur: Tuple
		self.prev = prev
		self.cur = cur