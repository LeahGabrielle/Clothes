#Clothing vs weather - main 
#fileName format is itemName top/bottoms hot/cold location
import clothesFile
import sortByWeather
import mood


def main():
    clothesList = clothesFile.openFile()
    valid = False
    while (valid != True) :
        searchType = input("How would you like to search?\n1.By Weather\n2.By Mood\n...\n")
        if searchType=='1':
            valid = True
            finalChoice = sortByWeather.requestWeather(clothesList)
            print("Your outfit is", finalChoice[0][0], "and", finalChoice[1][0])
        elif searchType =='2':
            valid = True
            return
        else:
            print("Not a valid option. Please enter 1 or 2")
    return
main()
