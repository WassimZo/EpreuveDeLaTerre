import string
alphabet = list(string.ascii_lowercase)
alphabet.append('\n')
display = ""

for lettre in alphabet : 
	display = display+lettre

print(display)