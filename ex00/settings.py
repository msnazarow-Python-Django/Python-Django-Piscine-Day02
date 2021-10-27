
class DotDict(dict):
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__

profile_image = 'https://sun9-60.userapi.com/impg/i9KqjREfoRylwenNMT2onjxLDnqH1djImk2x3w/gv2dMUtv6ZA.jpg?size=1044x1080&quality=96&sign=bddca72b4352805bce5710ff0821fb7c&type=album'
profile_fio_short = 'Filippova O.V.'
profile_fio_full = 'Filippova Oksana'
position = 'Artist'
location = 'Moscow'
phone_number = '+88003553535'
email = 'example@mail.com'
github = 'example@github.com'
skills = [
	DotDict({'name': 'Drawing', 'progress': '100'}),
	DotDict({'name': 'Teaching', 'progress': '100'}),
	DotDict({'name': 'Oil', 'progress': '100'}),
	DotDict({'name': 'Grafics', 'progress': '100'}),
	DotDict({'name': 'Portrait', 'progress': '100'}),
	DotDict({'name': 'Naturemort', 'progress': '100'})
]
vk = 'example'
instagram = 'example'
telegram = 'example'

projects = [
	DotDict({'name': 'Ofi School', 'description': 'Online Art School for everyone'}),
	DotDict({'name': 'Ofi Life', 'description': 'Blog of my life'}),
	DotDict({'name': 'Flowers in Art', 'description': 'My Diploma work about colors in Naturemort'}),
	DotDict({'name': 'OFI', 'description': 'Youtube channel about art, drawing and lifestyle'}),
]

works = [
	DotDict({'time': '2019-Present', 'position': 'Private Teacher', 'description' : 'Individual classes in drawing mostly online.'}),
	DotDict({'time': '2019', 'position': 'Teacher', 'description' : 'Education center for children.'}),
]

educations = [
	DotDict({'time': '2015-2019', 'place': 'OmGPU', 'description' : 'Art and Pedagogy, mostly studing teaching'}),
	DotDict({'time': '2011-2015', 'place': 'College of Arts', 'description' : 'Artist-Teacher, Mostly studing drawing'}),
]

about_me = 'Professional of my business, responsible, adorable, and just really wonderful person'
