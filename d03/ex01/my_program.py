from local_lib.path import Path

if __name__ == '__main__':
	folder = Path('./forex01')
	folder.mkdir_p()
	file = Path('./forex01/forex01.txt')
	file.touch()
	file.open()
	file.write_text("For ex01 text")
	print(file.text())

	