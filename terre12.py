import sys


def checkNbArgs() :
   if len(sys.argv) != 2 :
      return False
   else :
      return True

def createTime() :
      global time 
      time = sys.argv[1].split(':')

def cehckTime() : 
   if len(time) != 2 :
      return False
      print(len(time[1][1]))
   else : 
      return True

def createHours() :
   try : 
      global hours
      hours = int(time[0])
   except ValueError :
      print("Erreur")

def createMinutes() : 
   global minutes
   minutes = time[1][0]+time[1][1]
   try : 
      minutes = int(minutes)
   except ValueError :
      print("Erreur")

def createAmPm() : 
   global amPm
   amPm = time[1][2]+time[1][3] 

def checkFormat() : 
   if len(time[1]) != 4 :
      return False
   elif hours >= 13 or minutes >= 60 :
      return False
   else :
      return True

def checkAmPm() :
   if amPm == "am" or amPm == "AM" :
      return "am"
   elif amPm == "pm" or amPm == "PM" :
      return "pm"
   else :
      return "Erreur" 

def correctDisplay() :
   global hours
   global minutes
   if hours > 10 :
      hours = str(hours)
   else :
      hours = "0"+str(hours)

   if minutes > 10 : 
      minutes = str(minutes)
   else : 
      minutes = "0"+str(minutes)

if checkNbArgs() :
   createTime()
   print(time)
   if cehckTime() : 
      createHours()
      createMinutes()
      createAmPm()
      if checkFormat() : 
         if checkAmPm() == "am" :
            if hours == 12 :
               hours = hours -12
            correctDisplay()
            print("%s:%s" %(hours, minutes))
         elif checkAmPm() == "pm" :
            if hours != 12 :
               hours = hours + 12
            correctDisplay()   
            print("%s:%s" %(hours, minutes))
         else :
            print(checkAmPm())
      else:
         print("Erreur")
   else:
      print("Erreur")   
else :
   print("Erreur")