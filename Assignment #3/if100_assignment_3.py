# -*- coding: utf-8 -*-
"""IF100 - Take-Home Exam 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wERSTFdSxQZyA-k5froZomNkfnI7T8Nu
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:38:45 2021

@author: Serhan
"""

food_list = input("Please enter the dataset you have: ")
foods_eaten = input("PLease enter the food(s) you ate during the day: ").split(",")
calories_allowed = int(input("Please enter the amount of calories you can take in a day: "))
wanted_food = input("Please enter the food you want to eat: ").split(",")

food_list_sep = food_list.split(",")

samegroupcalories = []

def inspector(a):
  to_be_splitted = food_list_sep[a]
  return to_be_splitted.split(":")

def checker1(entered_food_name): #checks whether or not the given food is in the food list. either false or true.
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if entered_food_name == name:
      return True
  return False

def checker2(wanted_food): #checks whether or not the wanted food is in the food list
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name_wanted = b[0]
    if wanted_food[0] == name_wanted:
      return True
  return False

def indexer1(entered_food_name): #finds the index of the food. in the food_list_sep, food_list_sep[i].split(":")[2] has the calorie
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if entered_food_name == name:
      return i
  return False
def indexer2(wanted_food): #finds the index of the food. in the food_list_sep, food_list_sep[i].split(":")[2] has the calorie
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if wanted_food[0] == name:
      return i
def enteredfoodcaloriefinder(foods_eaten): #calculates and returns the sum of the calories of the foods eaten
  calorie_sum = 0
  for j in range(len(foods_eaten)):
    idx = indexer1(foods_eaten[j])
    b = inspector(idx)
    calorie_str = b[2]
    calorie_str = calorie_str[:-4]
    calorie_sum += int(calorie_str)
  return calorie_sum

def wantedfoodcaloriecalc(wanted_food):
    wantedfoodcalorie = inspector(indexer2(wanted_food))[2]
    wantedfoodcalorie = wantedfoodcalorie[:-4]
    wantedfoodcalorie = int(wantedfoodcalorie)
    return wantedfoodcalorie

def allfoodschecker(foods_eaten): # even if there is one value that doesn't exist in the food list this outputs False and also prints an error for EACH non-existing element.
  for j in range(len(foods_eaten)):
    if checker1(foods_eaten[j]) == False:
      return False
  return True

def allfoodscheckerprinter(foods_eaten): # even if there is one value that doesn't exist in the food list this outputs False and also prints an error for EACH non-existing element.
  check = True
  for j in range(len(foods_eaten)):
    if checker1(foods_eaten[j]) == False:
      print(foods_eaten[j], "is not in the dataset.")
      check == False
  return check

def wantedfoodchecker(wanted_food):
    for j in range(len(wanted_food)):
        if checker2(wanted_food[j]) == False:
            return False
    return True

def wantedfoodcheckerprinter(wanted_food):
    check = True
    for j in range(len(wanted_food)):
        if checker2(wanted_food) == False:
            print(wanted_food[j], "does not exist in the dataset.")
            check == False
    return check

def groupcreator(wanted_food):
    samegroupelements = []
    wantedfoodgroup = inspector(indexer2(wanted_food))[1]
    for j in range(len(food_list_sep)):
        b = inspector(j)
        if b[1] == wantedfoodgroup:
            samegroupelements.append(b[0])
        else:
            continue
    return samegroupelements

def caloriegroupcreator(wanted_food):
    samegroupcalories = []
    wantedfoodgroup = inspector(indexer2(wanted_food))[1]
    for j in range(len(food_list_sep)):
        b = inspector(j)
        if b[1] == wantedfoodgroup:
            calorie_str = b[2]
            calorie_str = calorie_str[:-4]
            calorie = int(calorie_str)
            samegroupcalories.append(calorie)
        else:
            continue
    return samegroupcalories

def calorieindexer(wanted_food):
  if wantedfoodchecker(wanted_food):
    calories_to_be_indexed = caloriegroupcreator(wanted_food)
  else:
    calories_to_be_indexed = []
  return calories_to_be_indexed

def caloriesorted(wanted_food):
  if wantedfoodchecker(wanted_food):
    calories_to_be_sorted = caloriegroupcreator(wanted_food)
  else:
    calories_to_be_sorted = []
  return calories_to_be_sorted.sort()

def grouplister(wanted_food):
  if wantedfoodchecker(wanted_food):
    groupelements = groupcreator(wanted_food)
  else:
    groupelements = []
  return groupelements

remaining_calories = calories_allowed - enteredfoodcaloriefinder(foods_eaten)
groupelements = grouplister(wanted_food)
calories_to_be_indexed = calorieindexer(wanted_food)
calories_to_be_sorted = caloriesorted(wanted_food)
lowestcalorieingroup = calories_to_be_sorted[0]
lowestcalorieidx = calories_to_be_indexed.index(lowestcalorieingroup)
lowestcaloriename = groupelements[lowestcalorieidx]
finalcalorie = enteredfoodcaloriefinder(foods_eaten) + wantedfoodcaloriecalc(wanted_food)

if __name__ == '__main__':
  if allfoodschecker(foods_eaten) == True:
    if wantedfoodchecker(wanted_food) == True:
      if remaining_calories > wantedfoodcaloriecalc(wanted_food):
        print("You can eat", wanted_food[0], "that you will get", finalcalorie , "calories.")
      else:
        if lowestcalorieingroup >= remaining_calories:
          print("There is no food you can eat from", inspector(indexer2(wanted_food))[1], "group.")
        else:
          print("You cannot eat " + str(wanted_food[0]) + ". However, we are suggesting you to eat " + str(lowestcaloriename) + ".")
    else:
      wantedfoodcheckerprinter(wanted_food)
  else:
    allfoodscheckerprinter(foods_eaten)

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:53:11 2021

@author: Serhan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:38:45 2021

@author: Serhan
"""

food_list = input("Please enter the dataset you have: ")
foods_eaten = input("PLease enter the food(s) you ate during the day: ").split(",")
calories_allowed = int(input("Please enter the amount of calories you can take in a day: "))
wanted_food = input("Please enter the food you want to eat: ").split(",")

food_list_sep = food_list.split(",")

samegroupcalories = []

def inspector(a):
  to_be_splitted = food_list_sep[a]
  return to_be_splitted.split(":")

def checker1(entered_food_name): #checks whether or not the given food is in the food list. either false or true.
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if entered_food_name == name:
      return True
  return False

def checker2(wanted_food): #checks whether or not the wanted food is in the food list
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name_wanted = b[0]
    if wanted_food[0] == name_wanted:
      return True
  return False

def indexer1(entered_food_name): #finds the index of the food. in the food_list_sep, food_list_sep[i].split(":")[2] has the calorie
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if entered_food_name == name:
      return i
  return False
def indexer2(wanted_food): #finds the index of the food. in the food_list_sep, food_list_sep[i].split(":")[2] has the calorie
  for i in range(len(food_list_sep)):
    b = inspector(i)
    name = b[0]
    if wanted_food[0] == name:
      return i
def enteredfoodcaloriefinder(foods_eaten): #calculates and returns the sum of the calories of the foods eaten
  calorie_sum = 0
  for j in range(len(foods_eaten)):
    idx = indexer1(foods_eaten[j])
    b = inspector(idx)
    calorie_str = b[2]
    calorie_str = calorie_str[:-4]
    calorie_sum += int(calorie_str)
  return calorie_sum

def wantedfoodcaloriecalc(wanted_food):
    if wantedfoodchecker(wanted_food):
      wantedfoodcalorie = inspector(indexer2(wanted_food))[2]
      wantedfoodcalorie = wantedfoodcalorie[:-4]
      wantedfoodcalorie = int(wantedfoodcalorie)
      return wantedfoodcalorie
    else:
      return 5

def allfoodschecker(foods_eaten): # even if there is one value that doesn't exist in the food list this outputs False and also prints an error for EACH non-existing element.
  for j in range(len(foods_eaten)):
    if checker1(foods_eaten[j]) == False:
      return False
  return True

def allfoodscheckerprinter(foods_eaten): # even if there is one value that doesn't exist in the food list this outputs False and also prints an error for EACH non-existing element.
  check = True
  for j in range(len(foods_eaten)):
    if checker1(foods_eaten[j]) == False:
      print(foods_eaten[j], "is not in the dataset.")
      check == False
  return check

def wantedfoodchecker(wanted_food):
    for j in range(len(wanted_food)):
        if checker2(wanted_food[j]) == False:
            return False
    return True

def wantedfoodcheckerprinter(wanted_food):
    check = True
    for j in range(len(wanted_food)):
        if checker2(wanted_food) == False:
            print(wanted_food[j], "does not exist in the dataset.")
            check == False
    return check

def groupcreator(wanted_food):
    samegroupelements = []
    wantedfoodgroup = inspector(indexer2(wanted_food))[1]
    for j in range(len(food_list_sep)):
        b = inspector(j)
        if b[1] == wantedfoodgroup:
            samegroupelements.append(b[0])
        else:
            continue
    return samegroupelements

def caloriegroupcreator(wanted_food):
    samegroupcalories = []
    wantedfoodgroup = inspector(indexer2(wanted_food))[1]
    for j in range(len(food_list_sep)):
        b = inspector(j)
        if b[1] == wantedfoodgroup:
            calorie_str = b[2]
            calorie_str = calorie_str[:-4]
            calorie = int(calorie_str)
            samegroupcalories.append(calorie)
        else:
            continue
    return samegroupcalories

def calorieindexer(wanted_food):
  calories_to_be_indexed = []  
  if wantedfoodchecker(wanted_food):
    calories_to_be_indexed = caloriegroupcreator(wanted_food)
  else:
    calories_to_be_indexed.append(5)
  return calories_to_be_indexed

def grouplister(wanted_food):
  groupelements = []  
  if wantedfoodchecker(wanted_food):
    groupelements = groupcreator(wanted_food)
  else:
    groupelements.append(5)
  return groupelements

groupelements = grouplister(wanted_food)
calories_to_be_indexed = calorieindexer(wanted_food)
calories_to_be_sorted = calorieindexer(wanted_food)
calories_to_be_sorted.sort()
lowestcalorieingroup = calories_to_be_sorted[0]
lowestcalorieidx = calories_to_be_indexed.index(lowestcalorieingroup)
lowestcaloriename = groupelements[lowestcalorieidx]
finalcalorie = enteredfoodcaloriefinder(foods_eaten) + wantedfoodcaloriecalc(wanted_food)

if allfoodschecker(foods_eaten) == True:
  remaining_calories = calories_allowed - enteredfoodcaloriefinder(foods_eaten)  
  if wantedfoodchecker(wanted_food) == True:
    if remaining_calories > wantedfoodcaloriecalc(wanted_food):
      print("You can eat", wanted_food[0], "that you will get", finalcalorie , "calories.")
    else:
      if lowestcalorieingroup >= remaining_calories:
        print("There is no food you can eat from", inspector(indexer2(wanted_food))[1], "group.")
      else:
        print("You cannot eat " + str(wanted_food[0]) + ". However, we are suggesting you to eat " + str(lowestcaloriename) + ".")
  else:
    wantedfoodcheckerprinter(wanted_food)
else:
  allfoodscheckerprinter(foods_eaten)