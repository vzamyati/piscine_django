import sys

def look_for_state(trim_param, states, capital_cities):

	trim_param = trim_param.lower()
	trim_param = trim_param.title()

	if not states.get(trim_param):
		return 0
	elif capital_cities.get(states[trim_param]):
		return(capital_cities[states[trim_param]])
	else:
		return 0

def look_for_capital(trim_param, states, capital_cities):

	trim_param = trim_param.lower()
	trim_param = trim_param.title()

	for key, value in capital_cities.items():
			if trim_param == value:
				for k, v in states.items():
					if v == key:
						return(k)

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

	params = sys.argv[1].split(",")

	for i in params:
		trim_param = i.strip()
		if trim_param:
			capital = look_for_state(trim_param, states, capital_cities)
			state = look_for_capital(trim_param, states, capital_cities)
			if capital:
				state = look_for_capital(capital, states, capital_cities)
				print("{} is the capital of {}".format(capital, state))
			elif state:
				capital = look_for_state(state, states, capital_cities)
				print("{} is the capital of {}".format(capital, state))
			else:
				print("{} is neither a capital city nor a state".format(trim_param))



if __name__ == '__main__':

	if len(sys.argv) == 2:
		main()
	else:
		sys.exit(0)