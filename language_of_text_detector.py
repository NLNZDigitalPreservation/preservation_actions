from langdetect import detect
import operator
import polyglot
from polyglot.text import Text, Word

with open ("internal.txt", encoding="utf8") as data:
	terms = data.read().split("\n")


tally = 0

hits = {}
for t in terms:

	text = Text(t)

	lang = text.language.name
	if lang not in hits:
		hits[lang] = 0

	hits[lang] += 1

	if lang == "Māori":

		tally += 1
		print (t)

	if lang == "English":
		tally += 1
