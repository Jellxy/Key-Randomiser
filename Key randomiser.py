import os, json, keyboard, random

with open('dictionary_by_letter.json', 'r') as dictfile:
	Dictionary = json.load(dictfile)
	dictfile.close()

def Stenograph(keyboardevent):
	key = keyboardevent.name.lower()
	if key in Dictionary:
		word = Dictionary[key][random.randint(0,len(Dictionary[key]) - 1)]
		keyboard.write('{} '.format(word[1:]))
		print('{} pressed, typing {}'.format(key, word))

keyboard.on_press(callback = Stenograph)
keyboard.wait()