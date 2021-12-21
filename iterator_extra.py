class Nested:

    def __init__(self, list):
        self.list = [item for sub_list in list for item in sub_list]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list):
            raise StopIteration
        if isinstance(self.list[self.cursor], list):
            = self.list[self.cursor]
        else:
            return self.list[self.cursor]
        

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', ['h', False],
	[1, 2, None]],
]
for item in Nested(nested_list):
	print(item) 
