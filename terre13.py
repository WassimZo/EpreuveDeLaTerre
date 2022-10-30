import sys 
import math

def checkNbArgs() :
   return len(sys.argv) == 4

def createVariables() :
   global a 
   global b 
   global c
   global variables

   try :
      a = int(sys.argv[1])
      b = int(sys.argv[2])
      c = int(sys.argv[3])
      variables = [a, b, c]
      return True;
   except ValueError : 
      print("erreur")
      return False;

def max() :
   max = 0
   for nbr in variables :
      if nbr > max :
         max = nbr

   return max

def min() : 
   min = math.inf
   for nbr in variables :
      if nbr < min :
         min = nbr

   return min


if checkNbArgs() : 
   if createVariables() :
      for nbr in variables : 
         if nbr != max() and nbr != min() :
            print(nbr)
         elif max() == min() :
            print("erreur")
            break;
else : 
   print("erreur")	

