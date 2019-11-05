
def print_var(var):
	print("{} est de type {}".format(var, type(var)))

def my_var():
	integer = 42
	print_var(integer)
	string = "42"
	print_var(string)
	string2 = "quarante-deux"
	print_var(string2)
	float_num = 42.0
	print_var(float_num)
	bool_type = True
	print_var(bool_type)
	list_type = [42]
	print_var(list_type)
	dict_type = {42: 42}
	print_var(dict_type)
	tuple_type = ((42,))
	print_var(tuple_type)
	set_type = set()
	print_var(set_type)

if __name__ == '__main__':
	my_var()