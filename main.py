nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:
	def __init__(self, _list):
		self._list = _list
		self.index = 0
		self.subindex = -1

	def __iter__(self):
		return self

	def __next__(self):

		while True:
			if self.index == len(self._list):
				raise StopIteration

			if self.subindex < len(self._list[self.index]) - 1:
				self.subindex += 1
				return self._list[self.index][self.subindex]
			else:
				self.index += 1
				self.subindex = -1


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def flat_generator(_list):
	index = 0
	subindex = -1
	while index < len(_list):

		if subindex < len(_list[index]) - 1:
			subindex += 1
			yield _list[index][subindex]
		else:
			index += 1
			subindex = -1


for item in flat_generator(nested_list):
	print(item)


