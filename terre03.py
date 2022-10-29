import sys
import string

alphabet = list(string.ascii_lowercase)
alphabet.append('\n')

display = ""
indexOfStart = alphabet.index(sys.argv[1])

for index in range(len(alphabet)) : 
	if index >= indexOfStart : 
		display = display + alphabet[index];
	else :
	     continue

print(display)