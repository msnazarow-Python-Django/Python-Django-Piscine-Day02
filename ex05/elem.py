#!/usr/bin/python3
class Text(str):
	"""
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

	def __new__(cls, content='', formatted=True):
		obj = str.__new__(cls, content)
		obj.formatted = formatted
		return obj

	def __str__(self, formatted=True):
		"""
        Do you really need a comment to understand this method?..
        """
		if self.formatted:
			return self.escape().replace('\n', '\n<br />\n')
		else:
			return self

	def escape(self, quote=True):
		"""
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.
        """
		s = self.replace("&", "&amp;")  # Must be done first!
		s = s.replace("<", "&lt;")
		s = s.replace(">", "&gt;")
		if len(s) < 2:
			s = s.replace('"', "&quot;")
			s = s.replace('\'', "&#x27;")
		elif s[0] == s[-1] == '"' or s[0] == s[-1] == "'":
			s = s[0] + s[1:-1].replace('"', "&quot;") + s[-1]
			s = s[0] + s[1:-1].replace('\'', "&#x27;") + s[-1]
		return s


class Elem:
	"""
    Elem will permit us to represent our HTML elements.
    """

	class ValidationError(Exception):
		def __init__(self, msg="This content is not Text or Elem"):
			super().__init__(msg)

	def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
		"""
        __init__() method.

        Obviously.
        """
		self.tag = tag
		self.attr = attr if attr is not None else {}
		self.tag_type = tag_type
		self.content = []
		if content is not None:
			self.add_content(content)

	def __str__(self):
		"""
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

		attr = self.__make_attr()
		result = f"<{self.tag}{attr}>"
		if self.content:
			result += self.__make_content()
		if self.tag_type == 'double':
			result += f"</{self.tag}>"
		return result

	def __make_attr(self):
		"""
        Here is a function to render our elements attributes.
        """
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		"""
        Here is a method to render the content, including embedded elements.
        """

		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			item = elem.__str__().replace('\n', '\n  ')
			result += f"  {item}\n"
		return result

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		"""
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
		return (isinstance(content, Elem) or
		        type(content) == Text or
		        (type(content) == list and
		         all(
			         [type(elem) == Text or isinstance(elem, Elem) for elem in content]
		         )))


if __name__ == '__main__':
	doc = Elem(tag='!DOCTYPE html', tag_type='simple')
	html = Elem(tag='html', attr={'lang': 'en'})
	head = Elem(tag='head')
	body = Elem(tag='body')
	title = Elem(tag='title', content=Text('"Hello ground"'))
	text = Elem(tag='h1', content=Text('"Oh no, not again!"'))
	img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg', 'alt': 'Some image'}, tag_type='simple')
	meta = Elem(tag='meta', attr={'charset': 'UTF-8'}, tag_type='simple')
	body.add_content(text)
	body.add_content(img)
	head.add_content(title)
	head.add_content(meta)
	html.add_content(head)
	html.add_content(body)
	print(doc, html, sep='\n')
