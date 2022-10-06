#----------IMPORTS----------#
import requests



#----------VARIABLES----------#
global url



#----------FUNCTIONS----------#
#Set url to his default value
def RestartUrl():    
    return "https://rickandmortyapi.com/api/"


#Adds extra url to the current url
def AddUrl(url_):
    global url
    
    return url + url_


#Request to the API using the current url and return the JSON
def SendRequest():
    global url
    
    request = requests.get(url)
    request = request.json()
    return request


#Main menu print, restart url and selection funccionality
def MainMenu():
    global url
    
    url = RestartUrl()
    selection = int(input("""
RICK AND MORTY DATABASE
-----------------------

1 - Character
2 - Location
3 - Exit

Select a topic to research or exit: """))
    if selection in list(mainMenuDic.keys()):
        mainMenuDic[selection]()
    else:
        while True:
            selection = int(input("This is not an option, try again: "))
            if selection <= 3 and selection >= 1:
                break
        mainMenuDic[selection]()


#Character menu print, update url and selection funccionality
def CharacterMenu():
    global url
    
    url = AddUrl("character/")
    selection = int(input("""\n\n
CHARACTERS
----------

1 - Find characters by ID
2 - Find characters by filter

Select an option to find characters: """))
    if selection in list(characterMenuDic.keys()):
        characterMenuDic[selection]()
    else:
        while True:
            selection = int(input("This is not an option, try again: "))
            if selection == 1 or selection == 2:
                break
        characterMenuDic[selection]()
    


#Input of IDs and send request to the API
def CharacterId():
    global url
    
    print("""\n\n
FIND CHARACTER BY ID
--------------------
""")
    idToAdd = ""
    multiple = False
    while True:
        
        idToAdd += input("Insert the ID of the character you want to find: ")
        if input("Do you want to add another character ID to the search? (Yes / No) ").lower() == "yes":
            idToAdd += ","
            print("")
            multiple = True
        else:
            url = AddUrl(idToAdd)
            print("\n------------------------------\n")
            if multiple:
                PrintMultipleCharactersData(SendRequest())
                break
            else:
                PrintOneCharacterData(SendRequest())
                break


#Filter selection menu, update url and selection funcctionality
def CharacterFilter():
    global url
    
    url = AddUrl("?")
    print("""\n\n
FIND CHARACTER BY FILTER
--------------------""")
    while True:
        filter = int(input("""
1 - Name
2 - Status
3 - Species
4 - Gender

Select a filter to find characters: """))
        if filter in list(characterFilterMenuDic.keys()):
            characterFilterMenuDic[filter]()
        else:
            while True:
                filter = int(input("This is not an option, try again: "))
                if filter >= 1 and filter <= 4:
                    break
                characterFilterMenuDic[filter]()
        if input("Do you want to add another filter to the search? (Yes / No) ").lower() == "yes":
            url = AddUrl("&")
        else:
            charactersJson = SendRequest()
            print("\n------------------------------\n")
            if len(charactersJson["results"]) != 1:
                PrintMultipleCharactersData(charactersJson["results"])
                break
            else:
                PrintOneCharacterData(charactersJson["results"])
                break


#Add the name filter and the value to the url
def CharacterName():
    global url
    
    print("")
    urlToAdd = "name="
    urlToAdd += input("Write the name you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Add the status filter and the value to the url
def CharacterStatus():
    global url
    
    print("")
    urlToAdd = "status="
    urlToAdd += input("Write the status you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Add the species filter and the value to the url
def CharacterSpecies():
    global url
    
    print("")
    urlToAdd = "species="
    urlToAdd += input("Write the specie you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Add the gender filter and the value to the url
def CharacterGender():
    global url
    
    print("")
    urlToAdd = "gender="
    urlToAdd += input("Write the gender you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Print the data of the character searched when there is only one character
def PrintOneCharacterData(characterJson_):
    print("llego")
    if list(characterJson_.keys())[0] == "error":
        print("Can't find any data that match with your search\n\n")
        return
    else:
        print("ID: ", characterJson_["id"])
        print("Name: ", characterJson_["name"])
        print("Status: ", characterJson_["status"])
        print("Species: "), characterJson_["species"]
        if characterJson_["type"] != "":
            print("Type: ", characterJson_["type"])
        print("Gender: ", characterJson_["gender"])
        print("Origin: ", characterJson_["origin"]["name"])
        print("Location: ", characterJson_["location"]["name"])
        print("\n------------------------------\n")


#Print the data of the characters searched when there are multiple characters
def PrintMultipleCharactersData(characterJson_):
    if len(characterJson_) != 0:
        for character in characterJson_:
            PrintOneCharacterData(character)
    else:
        print("Can't find any data that match with your search\n\n")
        return

#Character menu print, update url and selection funccionality
def LocationMenu():
    global url
    
    url = AddUrl("location/")
    selection = int(input("""\n\n
LOCATION
--------

1 - Find locations by ID
2 - Find locations by filter

Select an option to find locations: """))
    if selection in list(locationsMenuDic.keys()):
        locationsMenuDic[selection]()
    else:
        while True:
            selection = int(input("This is not an option, try again: "))
            if selection == 1 or selection == 2:
                break
        locationsMenuDic[selection]()


#Input of IDs and send request to the API
def LocationId():
    global url
    
    print("""\n\n
FIND LOCATION BY ID
--------------------
""")
    idToAdd = ""
    multiple = False
    while True:
        
        idToAdd += input("Insert the ID of the location you want to find: ")
        if input("Do you want to add another location ID to the search? (Yes / No) ").lower() == "yes":
            idToAdd += ","
            print("")
            multiple = True
        else:
            url = AddUrl(idToAdd)
            print("\n------------------------------\n")
            if multiple:
                PrintMultipleLocationsData(SendRequest())
                break
            else:
                PrintOneLocationData(SendRequest())
                break


#Filter selection menu, update url and selection funcctionality
def LocationFilter():
    global url
    
    url = AddUrl("?")
    print("""\n\n
FIND LOCATION BY FILTER
--------------------""")
    while True:
        filter = int(input("""
1 - Name
2 - Type
3 - Dimension

Select a filter to find locations: """))
        if filter in list(locationFilterMenuDic.keys()):
            locationFilterMenuDic[filter]()
        else:
            while True:
                filter = int(input("This is not an option, try again: "))
                if filter >= 1 and filter <= 3:
                    break
            locationFilterMenuDic[filter]()
        if input("Do you want to add another filter to the search? (Yes / No) ").lower() == "yes":
            url = AddUrl("&")
        else:
            charactersJson = SendRequest()
            if len(charactersJson["results"]) != 1:
                PrintMultipleLocationsData(charactersJson["results"])
                break
            else:
                PrintOneLocationData(charactersJson["results"])
                break


#Add the name filter and the value to the url
def LocationName():
    global url
    
    print("")
    urlToAdd = "name="
    urlToAdd += input("Write the name you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Add the type filter and the value to the url
def LocationType():
    global url
    
    print("")
    urlToAdd = "type="
    urlToAdd += input("Write the type you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Add the dimension filter and the value to the url
def LocationDimension():
    global url
    
    print("")
    urlToAdd = "dimension="
    urlToAdd += input("Write the dimension you want to sort by: ").lower()
    url = AddUrl(urlToAdd)


#Print the data of the location searched when there is only one location
def PrintOneLocationData(locationJson_):
    if list(locationJson_.keys())[0] == "error":
        print("Can't find any data that match with your search\n\n")
        return
    else:
        print("ID: ", locationJson_["id"])
        print("Name: ", locationJson_["name"])
        print("Type: ", locationJson_["type"])
        print("Dimension: ", locationJson_["dimension"])
        print("\n------------------------------\n")


#Print the data of the locations searched when there are multiple locationsw
def PrintMultipleLocationsData(locationJson_):
    if len(locationJson_) != 0:
        for location in locationJson_:
            PrintOneLocationData(location)
    else:
        print("Can't find any data that match with your search\n\n")
        return


#Function to exit the app
def Exit():
    print("\nClosing database...")
    exit()



#----------MENU DICCIONARIES----------#
mainMenuDic = {
    1 : CharacterMenu,
    2 : LocationMenu,
    3 : Exit
}

characterMenuDic = {
    1 : CharacterId,
    2 : CharacterFilter,
}

characterFilterMenuDic = {
    1 : CharacterName,
    2 : CharacterStatus,
    3 : CharacterSpecies,
    4 : CharacterGender 
}

locationsMenuDic = {
    1 : LocationId,
    2 : LocationFilter
}

locationFilterMenuDic = {
    1 : LocationName,
    2 : LocationType,
    3 : LocationDimension
}



#----------CODE----------#
url = RestartUrl()
while True:
    MainMenu()