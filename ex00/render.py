import inspect
import os
import sys
import settings


def main(argv):
	if len(argv) == 2:
		filename = argv[1]
		basename = os.path.splitext(filename)[0]
		with open(filename, 'r') as template, \
			open(f"{basename}.html", 'w') as file_html:
			data = template.read().split('style>')
			data[0] = data[0].format(**vars(settings))
			data[2] = data[2].format(**vars(settings))
			file_html.write('style>'.join(data))


if __name__ == '__main__':
	main(sys.argv)