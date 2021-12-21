def item_list_generator(nested_list, res=[]):
    nested_list = [item for sub_list in nested_list for item in sub_list]
    x = 0
    while x < len(nested_list):
        if isinstance(list[x], list):
            item_list_generator(nested_list[x])
        else:
            yield  nested_list[x]
        x += 1

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in item_list_generator(nested_list):
    print(item) 