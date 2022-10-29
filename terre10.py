import sys

prime = True

if len(sys.argv) != 2 :
   print("erreur")
else :
   try : 
      nbr = int(sys.argv[1])

      if nbr < 0 : 
         print("erreur")
      else :
         if nbr == 1 or nbr == 0 : 
            prime = False
         else :
            for divisor in range(2, nbr-1) :
               if nbr % divisor == 0 : 
                  prime = False

         if prime : 
            print("Oui, %i est un nombre premier." %nbr)
         else :
            print("Non, %i n'est pas un nombre premier" %nbr)
   except ValueError :
      print("erreur") 




