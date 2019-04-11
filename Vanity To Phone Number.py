# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:39:26 2019

@author: School
"""
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Makes a list of letters
numbers = ['2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','7','7','7','8','8','8','9','9','9','9'] #Makes a list of numbers
area_code = input("Enter the area code of the vanity number: " )
vanity_number = input("Enter a vanity phone number: ").lower().replace("-","")[:7] #Declaring an input variable, trimming input to 7 characters, changing string to all lower case letters, and replacing hypens if user inputs any
phone_number = ""

for index in range(len(vanity_number)): #For loop that ends when the letters given by user ends
   if vanity_number[index].isalpha(): #.isalpha() ensures that the user inputs letters and no special characters.
       phone_number = phone_number + str(numbers[letters.index(vanity_number[index])])
       
   else: #If a user enters special charcters then it ends the program and asks them to try again
       print("Please enter only numbers, then run the program again")
             
print(area_code + phone_number)