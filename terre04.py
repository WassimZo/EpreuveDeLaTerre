import sys
import traceback

try :
   nbr = int(sys.argv[1])

   if nbr%2 == 0 :
       print("pair")
   else :
	   print("impair")

except Exception : 
   print("Tu ne me la mettras pas à l'envers.")


    