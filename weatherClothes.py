#Clothing vs weather - main 
#fileName format is itemName top/bottoms hot/cold location
import weatherClothes_files
import weather
import mood


def main():
    clothesList = weatherClothes_files.openFile()
    searchType = input("Select search (1 or 2)\n1. by weather\n2. by mood\n")
    if searchType=='1':
        finalChoice = weather.requestWeather(clothesList)
        print("Your outfit is", finalChoice[0][0], "and", finalChoice[1][0])
    elif searchType =='2':
        return
    return

main()
