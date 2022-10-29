import sys 

if len(sys.argv) != 2 :
   print("erreur")
else:
   time = sys.argv[1].split(':')
   if len(time) != 2 : 
      print("erreur")
   else : 
      try:
         hours = int(time[0])
         minutes = int(time[1])
         if hours >= 24 or minutes >= 60 :
            print("erreur")
         else :
            if minutes < 10 :
         	   minutes = "0"+str(minutes)
            else:
               minutes = str(minutes)
            if hours >= 12 :
               if hours != 12 :
                  hours = hours - 12
               print("%i:%sPM" %(hours, minutes))
            else:
               if hours == 0 :
                  hours = hours+12
               print("%i:%sAM" %(hours, minutes))
      except ValueError:
         print("erreur")
