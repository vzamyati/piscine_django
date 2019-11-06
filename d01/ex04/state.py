import sys

def main():

	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}
	
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for key, value in capital_cities.items():
		if sys.argv[1] == value:
			for k, v in states.items():
				if v == key:
					print(k)
					sys.exit(0)
		elif sys.argv[1] != value:
			print("Unknown capital city")
			sys.exit(0)

if __name__ == '__main__':

	if len(sys.argv) == 2:
		main()
	else:
		sys.exit(0)