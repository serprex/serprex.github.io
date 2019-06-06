#!/bin/python
def main():
	from collections import defaultdict
	import re
	import xml.etree.ElementTree as etree

	pages = { "ZOMG!": None, "Synava": None, "Nerquin": None, "To Mance a Mance": None, "k-means": None }
	for page in etree.parse('Novelas.xml').getroot():
		if page.tag.endswith('page'):
			title = ""
			text = ""
			for n in page:
				if n.tag.endswith('title'):
					title = n.text
				elif n.tag.endswith('revision'):
					for r in n:
						if r.tag.endswith('text'):
							text = r.text
			pages[title] = text

	def linkparse(m):
		m1 = m[1]
		m2 = m1
		if m1.startswith("Image:") or m1.startswith("File:"):
			return m[0]
		if "|" in m1:
			m1, m2 = m1.split("|")
		if m1.startswith('w:c:'):
			m1c = m1.find(':', 4)
			return "[%s](https://%s.wikia.com/wiki/%s)"%(m2, m1[4:m1c], m1[m1c+1:])
		elif m1.startswith('#'):
			return "[%s](#%s)"%(m2, m1.replace(' ', '-').lower())
		elif m1 in pages:
			return "[%s](%s.md)"%(m2, m1.replace(':', ' '))
		elif m1.startswith("User:"):
			return "[%s](https://fiction.wikia.com/wiki/%s)"%(m2.replace("User:", ""), m1)
		elif m1.startswith(":Category:"):
			return "[%s](%s)"%(m2.replace(':Category:', ''), m1.replace(':Category:', ''))
		else:
			return "[%s](https://fiction.wikia.com/wiki/%s)"%(m2, m1)

	def headingrep(m):
		if m[1] == m[3]:
			return "#" * len(m[1]) + " " + m[2]
		return None

	for title, s in pages.items():
		if not s or title.startswith('Category:') or title.startswith('User:'):continue
		s = re.sub("[ \t]$", "", s, flags=re.M)
		s = s.replace("''[[User:Serprex]] ", "''")
		s = s.replace("[[User:Serprex]]", '')
		s = re.sub("^(=+)([^=]+)(=+)$", headingrep, s, flags=re.M)
		s = re.sub(r"\[\[Category:(.*?)\]\]", '', s)
		s = re.sub(r"\[\[(.*?)\]\]", linkparse, s)
		s = re.sub(r"\[(https?://[^ ]+?) (.*?)\]", lambda m:"[%s](%s)"%(m[2], m[1]), s)
		while True:
			z = re.sub("'''(.*?)'''", r'**\1**', s)
			if s == z:break
			s = z
		s = re.sub("'''(.*?)(\||\n)", r'**\1**\2', s)
		while True:
			z = re.sub("''(.*?)''", r'*\1*', s)
			if s == z:break
			s = z
		s = re.sub("''(.*?)\n", r'*\1*\n', s)
		s = re.sub("\n{3,}", "\n\n", s)
		with open(title.replace(':', ' ') + '.md', 'w') as outf:outf.write(s)

main()
