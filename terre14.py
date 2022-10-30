import sys

def createList() : 
   global variables
   variables = []
   for index in range(1, len(sys.argv)) :
      try : 
         var = int(sys.argv[index])
         variables.append(var)
      except ValueError :
         return False
   return True


def checkSort() : 
   for index in range(0, len(variables)-1) :
      if variables[index] > variables[index+1] : 
         return "Pas triée !"
   return "Triée !"

if createList() : 
   print(checkSort())
else : 
   print("erreur")