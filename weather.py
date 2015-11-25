#clothes by weather

import random

def pickTop(clothesList):
    return random.choice(clothesList[0])

def pickBottoms(clothesList):
    return random.choice(clothesList[1])

#sorts clothes into weather type and returns a list of clothes of the correct weather
def sortWeather(clothesList, weather):
    #eventually combine the two loops
    '''
    for i in range(0,len(clothesList)):
        for j in range(0, len(clothesList[i]):
            '''
    #change to switch later
    #go through tops
    i=0
    for top in clothesList[0]:
        if top[2] != weather:
            clothesList[0].pop(i)
        i+=1  
    #go through bottoms
    i=0
    for bottom in clothesList[1]:
        if bottom[2] != weather:
            clothesList[1].pop(i)
        i+=1        
    return clothesList

#Asks user for their weather choice
def requestWeather(clothesList):
    weather = input("Is the weather hot or cold?\n")
    clothesList = sortWeather(clothesList, weather)
    finalChoice = []
    finalChoice.append(pickTop(clothesList))
    finalChoice.append(pickBottoms(clothesList))
    return finalChoice