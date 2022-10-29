import sys 

if len(sys.argv) != 3 :
   print("erreur.")
else :
   try : 
      nbr = int(sys.argv[1])
      expo = int(sys.argv[2])
   except ValueError :
   	  print("error")

   print(nbr**expo)
