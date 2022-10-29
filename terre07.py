import sys
import traceback

if len(sys.argv) != 2 : 
	print("erreur.")
else :
	try:
		intTest = int(sys.argv[1])
		print("erreur.")
	except ValueError :
		print(len(sys.argv[1]))

