
class DotDict(dict):
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__

profile_image = ''
profile_fio_short = ''
profile_fio_full = ''
position = ''
location = ''
phone_number = ''
email = ''
github = ''
skills = [
	DotDict({'name': 'C', 'progress': '100'}),
	DotDict({'name': 'C', 'progress': '100'}),
	DotDict({'name': 'C', 'progress': '100'}),
	DotDict({'name': 'C', 'progress': '100'}),
	DotDict({'name': 'C', 'progress': '100'}),
	DotDict({'name': 'C', 'progress': '100'})
]
vk = ''
instagram = ''
telegram = ''

projects = [
	DotDict({'name': 'C', 'description': '<b>Minishell</b> - alter shell for UNIX system.'}),
	DotDict({'name': 'C', 'description': '<b>Minishell</b> - alter shell for UNIX system.'}),
	DotDict({'name': 'C', 'description': '<b>Minishell</b> - alter shell for UNIX system.'}),
	DotDict({'name': 'C', 'description': '<b>Minishell</b> - alter shell for UNIX system.'}),
]

works = [
	DotDict({'time': '2021-Present', 'position': 'Private Teacher', 'description' : 'From 18 years old i teach math pythics and computer scince. Last several years I help others to learn programing languages, such as C, C++, Python, Swift and others.'}),
	DotDict({'time': '2021-Present', 'position': 'Private Teacher', 'description' : 'From 18 years old i teach math pythics and computer scince. Last several years I help others to learn programing languages, such as C, C++, Python, Swift and others.'}),
]

educations = [
	DotDict({'time': '2019-Present', 'place': 'School 21 (Ecole 42)', 'description' : 'I studied shell, C, C++, Swift, Python, Docker and many other things here'}),
	DotDict({'time': '2019-Present', 'place': 'School 21 (Ecole 42)', 'description' : 'I studied shell, C, C++, Swift, Python, Docker and many other things here'}),
]

about_me = ''
