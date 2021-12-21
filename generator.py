def item_list_generator(list):
    list = [item for sub_list in list for item in sub_list]
    x = 0
    while x < len(list):
        yield list[x]
        x += 1
               
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in item_list_generator(nested_list):
    print(item) 
