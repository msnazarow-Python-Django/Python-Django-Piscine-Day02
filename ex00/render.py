import os
import sys
import settings


def main(argv):
	if len(argv) == 2:
		filename = argv[1]
		basename = os.path.splitext(filename)[0]
		with open(filename, 'r') as template, \
			open(f"{basename}.html", 'w') as file_html:
			file_html.write(f"f'{template.read()}'")


if __name__ == '__main__':
	main(sys.argv)