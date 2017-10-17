'''
This is a English dictionary that loads definitions based on user word input
	-allow for user input
	-check to see if that word is valid/exists in the dictionary
		-return error if this word cannot be found
		-or return prompt, suggesting a close word.
	-return definition
'''
import xml.etree.cElementTree as ET
import json
from urllib.request import urlopen
from difflib import SequenceMatcher
from difflib import get_close_matches



def define():
	definitions = json.load(open("data.json"))
	word = input("Word: ").lower()
	closeMatches = get_close_matches(word,definitions.keys())

	if word in definitions: return definitions[closeMatches[0]]
	elif len(closeMatches) > 0:
		yn = input("Did you mean %s? Please enter Y for yes or N for no: " % closeMatches[0] )
		if yn.lower() == "y": return definitions[closeMatches[0]]
		elif yn.lower() == "n": return "Are you saying you are smarter than a robot?"
	else: return "Sorry, that word cannot be found."


def getWords():
	url = " http://www.dictionaryapi.com/api/v1/references/collegiate/xml/test?key=b630c0fe-49f9-40ac-8ee4-6d74318f4dc1"
	urlData = urlopen(url)
	if (urlData.getcode()==200):
		data = urlData.read()
		root = ET.fromstring(data)
		#data.write("webster.xml")
		with open('webster.xml','w+') as file:
			file.write(data)

	else: print("Could not connect to API.")


output = define()

if type(output)==list:
	for i in output:
		print(str(output.index(i)+1)+": %s" % i)
else: print(output)

