#!/usr/bin/env python3
from elem import *


class DotDict(dict):
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


class Doctype(Elem):
	def __init__(self):
		super().__init__(tag='!DOCTYPE html', tag_type='simple')


class Html(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='html', attr=attr, content=content)


class Head(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='head', attr=attr, content=content)


class Body(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='body', attr=attr, content=content)


class Title(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='title', attr=attr, content=content)


class Meta(Elem):
	def __init__(self, attr=None):
		super().__init__(tag='meta', attr=attr, tag_type='simple')


class Style(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='style', attr=attr, content=content)


class Img(Elem):
	def __init__(self, attr=None):
		super().__init__(tag='html', attr=attr, tag_type='simple')


class Table(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='table', attr=attr, content=content)


class Th(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='th', attr=attr, content=content)


class Tr(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='tr', attr=attr, content=content)


class Td(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='td', attr=attr, content=content)


class Ul(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='ul', attr=attr, content=content)


class Ol(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='ol', attr=attr, content=content)


class Li(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='li', attr=attr, content=content)


class H1(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='h1', attr=attr, content=content)


class H2(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='h2', attr=attr, content=content)


class H3(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='h3', attr=attr, content=content)


class H4(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='h4', attr=attr, content=content)


class P(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='p', attr=attr, content=content)


class Div(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='div', attr=attr, content=content)


class Span(Elem):
	def __init__(self, content=None, attr=None):
		super().__init__(tag='span', attr=attr, content=content)


class Hr(Elem):
	def __init__(self, attr=None):
		super().__init__(tag='ol', attr=attr, tag_type='simple')


class Br(Elem):
	def __init__(self, attr=None):
		super().__init__(tag='ol', attr=attr, tag_type='simple')


def get_elem_class(periodic_elem):
	element_class = ""
	if periodic_elem.number in (1, 6, 7, 8, 15, 16, 34):
		element_class = "gas1"
	elif periodic_elem.number in (5, 14, 32, 33, 51, 52, 84):
		element_class = "metal5"
	elif periodic_elem.number in (13, 31, 49, 50, 82, 83, 81):
		element_class = "metal4"
	elif periodic_elem.number in (113, 115, 117, 118):
		element_class = "rare1"
	elif periodic_elem.position == 0:
		element_class = "metal1"
	elif periodic_elem.position == 1:
		element_class = "metal2"
	elif 2 <= periodic_elem.position <= 11:
		element_class = "metal3"
	elif periodic_elem.position == 16:
		element_class = "gas2"
	elif periodic_elem.position == 17:
		element_class = "gas3"
	elif periodic_elem.number in (114, 116):
		element_class = "rare2"
	return element_class


def generate_element(periodic_elem, last_number):
	span_length = periodic_elem.position - last_number

	if span_length > 2:
		fake_elem = Td(attr={'colspan': f'{span_length - 1}', 'style': 'border:0'})
	elif span_length > 1:
		if periodic_elem.number == 72:
			fake_elem = generate_element(
				DotDict({'position': 2, 'number': 71, 'small': 'Lu', 'full': 'Lutetium', 'molar': 174.9668}),
				last_number)
		elif periodic_elem.number == 104:
			fake_elem = generate_element(
				DotDict({'position': 2, 'number': 103, 'small': 'Lr', 'full': 'Lawrencium', 'molar': 262}), last_number)
	element_class = get_elem_class(periodic_elem)
	elem = Td(attr={'class': f'{element_class}'}, content=
	Ul([
		Li(Text(periodic_elem.small)),
		Li(Text(periodic_elem.number)),
		Li(Text(periodic_elem.molar))
	])
	          )
	if 'fake_elem' in locals():
		return [fake_elem, elem]
	else:
		return elem


def create_periodic_elem(elem_name, temp_array):
	periodic_elem = {}
	for elem in temp_array:
		key, value = map(lambda x: x.strip(), elem.split(':'))
		periodic_elem[key] = value
	periodic_elem['full'] = elem_name
	periodic_elem = DotDict(periodic_elem)
	periodic_elem.number = int(periodic_elem.number)
	periodic_elem.position = int(periodic_elem.position)
	periodic_elem.molar = float(periodic_elem.molar)
	return periodic_elem


def main():
	elements = """Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1
Helium = position:17, number:2, small: He, molar:4.002602, electron:2
Lithium = position:0, number:3, small: Li, molar:6.941, electron:2 1
Beryllium = position:1, number:4, small: Be, molar:9.012182, electron:2 2
Boron = position:12, number:5, small: B, molar:10.811, electron:2 3
Carbon = position:13, number:6, small: C, molar:12.0107, electron:2 4
Nitrogen = position:14, number:7, small: N, molar:14.0067, electron:2 5
Oxygen = position:15, number:8, small: O, molar:15.9994, electron:2 6
Fluorine = position:16, number:9, small: F, molar:18.998404, electron:2 7
Neon = position:17, number:10, small: Ne, molar:20.1797, electron:2 8
Sodium = position:0, number:11, small: Na, molar:22.989769, electron:2 8 1
Magnesium = position:1, number:12, small: Mg, molar:24.305, electron:2 8 2
Aluminium = position:12, number:13, small: Al, molar:26.981539, electron:2 8 3
Silicon = position:13, number:14, small: Si, molar:28.0855, electron:2 8 4
Phosphorus = position:14, number:15, small: P, molar:30.973763, electron:2 8 5
Sulfur = position:15, number:16, small: S, molar:32.065, electron:2 8 6
Chlorine = position:16, number:17, small: Cl, molar:35.453, electron:2 8 7
Argon = position:17, number:18, small: Ar, molar:39.948, electron:2 8 8
Potassium = position:0, number:19, small: K, molar:39.0983, electron:2 8 8 1
Calcium = position:1, number:20, small: Ca, molar:40.078, electron:2 8 8 2
Scandium = position:2, number:21, small: Sc, molar:44.955914, electron:2 8 9 2
Titanium = position:3, number:22, small: Ti, molar:47.867, electron:2 8 10 2
Vanadium = position:4, number:23, small: V, molar:50.9415, electron:2 8 11 2
Chromium = position:5, number:24, small: Cr, molar:51.9961, electron:2 8 13 1
Manganese = position:6, number:25, small: Mn, molar:54.938046, electron:2 8 13 2
Iron = position:7, number:26, small: Fe, molar:55.845, electron:2 8 14 2
Cobalt = position:8, number:27, small: Co, molar:58.933193, electron:2 8 15 2
Nickel = position:9, number:28, small: Ni, molar:58.6934, electron:2 8 16 2
Copper = position:10, number:29, small: Cu, molar:63.546, electron:2 8 18 1
Zinc = position:11, number:30, small: Zn, molar:65.38, electron:2 8 18 2
Gallium = position:12, number:31, small: Ga, molar:69.723, electron:2 8 18 3
Germanium = position:13, number:32, small: Ge, molar:72.63, electron:2 8 18 4
Arsenic = position:14, number:33, small: As, molar:74.9216, electron:2 8 18 5
Selenium = position:15, number:34, small: Se, molar:78.96, electron:2 8 18 6
Bromine = position:16, number:35, small: Br, molar:79.904, electron:2 8 18 7
Krypton = position:17, number:36, small: Kr, molar:83.798, electron:2 8 18 8
Rubidium = position:0, number:37, small: Rb, molar:85.4678, electron:2 8 18 8 1
Strontium = position:1, number:38, small: Sr, molar:87.62, electron:2 8 18 8 2
Yttrium = position:2, number:39, small: Y, molar:88.90585, electron:2 8 18 9 2
Zirconium = position:3, number:40, small: Zr, molar:91.224, electron:2 8 18 10 2
Niobium = position:4, number:41, small: Nb, molar:92.90638, electron:2 8 18 12 1
Molybdenum = position:5, number:42, small: Mo, molar:95.96, electron:2 8 18 13 1
Technetium = position:6, number:43, small: Tc, molar:98, electron:2 8 18 13 2
Ruthenium = position:7, number:44, small: Ru, molar:101.07, electron:2 8 18 15 1
Rhodium = position:8, number:45, small: Rh, molar:102.9055, electron:2 8 18 16 1
Palladium = position:9, number:46, small: Pd, molar:106.42, electron:2 8 18 18
Silver = position:10, number:47, small: Ag, molar:107.8682, electron:2 8 18 18 1
Cadmium = position:11, number:48, small: Cd, molar:112.411, electron:2 8 18 18 2
Indium = position:12, number:49, small: In, molar:114.818, electron:2 8 18 18 3
Tin = position:13, number:50, small: Sn, molar:118.71, electron:2 8 18 18 4
Antimony = position:14, number:51, small: Sb, molar:121.76, electron:2 8 18 18 5
Tellurium = position:15, number:52, small: Te, molar:127.6, electron:2 8 18 18 6
Iodine = position:16, number:53, small: I, molar:126.90447, electron:2 8 18 18 7
Xenon = position:17, number:54, small: Xe, molar:131.293, electron:2 8 18 18 8
Caesium = position:0, number:55, small: Cs, molar:132.90546, electron:2 8 18 18 8 1
Barium = position:1, number:56, small: Ba, molar:137.327, electron:2 8 18 18 8 2
Hafnium = position:3, number:72, small: Hf, molar:178.49, electron:2 8 18 32 10 2
Tantalum = position:4, number:73, small: Ta, molar:180.94788, electron:2 8 18 32 11 2
Tungsten = position:5, number:74, small: W, molar:183.84, electron:2 8 18 32 12 2
Rhenium = position:6, number:75, small: Re, molar:186.207, electron:2 8 18 32 13 2
Osmium = position:7, number:76, small: Os, molar:190.23, electron:2 8 18 32 14 2
Iridium = position:8, number:77, small: Ir, molar:192.217, electron:2 8 18 32 15 2
Platinum = position:9, number:78, small: Pt, molar:195.084, electron:2 8 18 32 17 1
Gold = position:10, number:79, small: Au, molar:196.96657, electron:2 8 18 32 18 1
Mercury = position:11, number:80, small: Hg, molar:200.59, electron:2 8 18 32 18 2
Thallium = position:12, number:81, small: Tl, molar:204.3833, electron:2 8 18 32 18 3
Lead = position:13, number:82, small: Pb, molar:207.2, electron:2 8 18 32 18 4
Bismuth = position:14, number:83, small: Bi, molar:208.9804, electron:2 8 18 32 18 5
Polonium = position:15, number:84, small: Po, molar:209, electron:2 8 18 32 18 6
Astatine = position:16, number:85, small: At, molar:210, electron:2 8 18 32 18 7
Radon = position:17, number:86, small: Rn, molar:222, electron:2 8 18 32 18 8
Francium = position:0, number:87, small: Fr, molar:223, electron:2 8 18 32 18 8 1
Radium = position:1, number:88, small: Ra, molar:226, electron:2 8 18 32 18 8 2
Rutherfordium = position:3, number:104, small: Rf, molar:267, electron:2 8 18 32 32 10 2
Dubnium = position:4, number:105, small: Db, molar:268, electron:2 8 18 32 32 11 2
Seaborgium = position:5, number:106, small: Sg, molar:271, electron:2 8 18 32 32 12 2
Bohrium = position:6, number:107, small: Bh, molar:272, electron:2 8 18 32 32 13 2
Hassium = position:7, number:108, small: Hs, molar:270, electron:2 8 18 32 32 14 2
Meitnerium = position:8, number:109, small: Mt, molar:276, electron:2 8 18 32 32 15 2
Darmstadtium = position:9, number:110, small: Ds, molar:281, electron:2 8 18 32 32 17 1
Roentgenium = position:10, number:111, small: Rg, molar:280, electron:2 8 18 32 32 18 1
Copernicium = position:11, number:112, small: Cn, molar:285, electron:2 8 18 32 32 18 2
Ununtrium = position:12, number:113, small: Uut, molar:284, electron:2 8 18 32 32 18 3
Flerovium = position:13, number:114, small: Fl, molar:289, electron:2 8 18 32 32 18 4
Ununpentium = position:14, number:115, small: Uup, molar:288, electron:2 8 18 32 32 18 5
Livermorium = position:15, number:116, small: Lv, molar:293, electron:2 8 18 32 32 18 6
Ununseptium = position:16, number:117, small: Uus, molar:294, electron:2 8 18 32 32 18 7
Ununoctium = position:17, number:118, small: Uuo, molar:294, electron:2 8 18 32 32 18 8"""
	css = '''*{
		margin: 0px;
		padding: 0;
		width: 80px;
		align-content: end;
		border-collapse: collapse;
	}
	td {
		border: 1px solid #000000;
	}
	ul{
		margin: 1px;
		list-style: none;
		font-size: small;
		position: relative;
	}
	h4{
		font: 0.8em normal;
	}
	li:nth-child(1){
		position:relative;
		top: 7px;
		font-size: 2.5em;
		margin-bottom: 0.1em;
	}
	li:nth-child(2) {
		position: absolute;
		top: -5px;
		text-align: right;
		font-size: 2em;
	}
	li:nth-child(3) {
		position: absolute;
		top: 0;
		font: 0.9em;
	}
	.gas1 {
		background-color: cornflowerblue;
	}
	.gas2 {
		background-color: plum;
	}
	.gas3 {
		background-color: darkturquoise;
	}
	.metal1 {
		background-color: burlywood;
	}
	.metal2 {
		background-color: wheat;
	}
	.metal3 {
		background-color: darkkhaki;
	}
	.metal4 {
		background-color: bisque;
	}
	.metal5 {
		background-color: lightgreen;
	}
	.rare1 {
		background-color: red;
	}
	.rare2 {
		background-color: gray;
	}
	'''
	table = Table()
	tr = Tr()
	last_number = 0
	for line in elements.split('\n'):
		elem_name, elem_string = map(lambda x: x.strip(), line.split('='))
		temp_array = elem_string.split(',')
		periodic_elem = create_periodic_elem(elem_name, temp_array)
		if periodic_elem.position == 0:
			tr = Tr()
		tr.add_content(generate_element(periodic_elem, last_number))
		if periodic_elem.position == 17:
			table.add_content(tr)
		last_number = periodic_elem.position
	try:
		with open("periodic.table.html", 'w') as file:
			file.write(
				Doctype().__str__() + '\n' +
				Html(attr={'lang': 'en'},
				     content=[
					     Head([
						     Meta({'charset': 'UTF-8'}),
						     Title(Text('Periodic Table')),
						     Style(Text(css, formatted=False))
					     ]),
					     Body(table)
				     ]).__str__()
			)
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()
