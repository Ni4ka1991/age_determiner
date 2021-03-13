#!/usr/bin/env Python3

#Data

year_of_birth = int(input("\nPlease, enter your date of birth:\n"))



#logic

if (1900 < year_of_birth <= 2021):            #Data checking
 
 age = 2021 - year_of_birth                   #Age calculation
 
 #Age-range classification
 if ( 1 <= age <= 3 ):
  print ( "Baby" )
 elif ( 4 <= age < 9 ):
  print ( "Kid" )
 elif (  10 <= age <= 15 ):
  print ( "Teen ")
 elif ( 16 <= age <= 18 ):
  print ( "Young" )
 elif ( 19 <= age <= 50 ):
  print ( "Adult" )
 elif ( age >= 51 ):
  print ("Old")
 
else:
 print("\nYour entered is outside the date range")



