import sys
import math

if len(sys.argv) != 2 : 
	print("Erreur")
else :
	try : 
		nbr = int(sys.argv[1])
		if nbr < 0 :
			print("Erreur")
		else :
		    print(math.sqrt(nbr))
	except ValueError :
		print("Erreur")