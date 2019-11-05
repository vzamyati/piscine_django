import sys

if __name__ == '__main__':

	if len(sys.argv) == 2:
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
	
		if not states.get(sys.argv[1]):
			print("Unknown state")
			sys.exit(0)
		elif capital_cities.get(states[sys.argv[1]]):
			print(capital_cities[states[sys.argv[1]]])
		else:
			sys.exit(0)
	