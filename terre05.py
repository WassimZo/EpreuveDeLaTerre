import sys 

dividend = int(sys.argv[1])
divisor = int(sys.argv[2])

if divisor > 0 and dividend >= divisor:
	quotient = int(dividend/divisor)
	remainder = dividend-(quotient*divisor)
	print("résultat: %i" % quotient)
	print("reste: %i" % remainder)
else :
	print('erreur.')
