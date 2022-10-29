import sys

if len(sys.argv) > 1:
  string = str(sys.argv[1])
  inverse = ""
  index = len(string)-1

  while index >= 0 :
  	inverse = inverse+(string[index])
  	index = index -1 

  print(inverse)
else :
	print("Erreur.")