import sys
import antigravity

def case_of_error():
	print("Usage: geohashing.py latitude longitude date‎‎ dow_opening")
	print("Example: geohashing.py 37.421542 -122.085589 2005-05-26 10458.68")
	sys.exit(1)

def check_float(latitude, longitude, date, dow_opening):
	try:
		lat = float(latitude)
		lon = float(longitude)
		dow = float(dow_opening)
	except ValueError :
		print("latitude,longitude and dow_opening have to be float")
		case_of_error()
	list = [lat, lon, date, dow]
	return list

def geohashing(params):
	date_dow = params[2] + "-" + str(params[3])
	antigravity.geohash(params[0], params[1], date_dow.encode('ascii'))
	sys.exit(0)


if __name__ == '__main__':
	if len(sys.argv) == 5:
		params = check_float(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		geohashing(params)
	else:
		case_of_error()