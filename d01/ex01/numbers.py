if __name__ == '__main__':
	f = open("numbers.txt", "r")
	print(f.read().replace(",", "\n").strip())