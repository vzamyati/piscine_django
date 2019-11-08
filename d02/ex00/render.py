import sys
import settings
import re

def read_file():
	f = open("myCV.template","r")
	f1 = f.readlines()
	for x in f1:
		f1 = re.search(f1, '{*}')
		print(f1.group())

	# template_vars = []
	# for template_var in template_vars:
	# 	getattr(settings,template_var)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1].endswith('.template'):
			read_file()
		else:
			sys.exit(0)
	else:
		sys.exit(0)

	