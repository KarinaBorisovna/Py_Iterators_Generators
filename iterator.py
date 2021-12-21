class FlatIterator:

    def __init__(self, list):
        self.list = [item for sub_list in list for item in sub_list]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list):
            raise StopIteration
        return self.list[self.cursor]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item) 


flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)