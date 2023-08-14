import readSongs, addSongs, updateSongs, deleteSongs, reports

# function to read respective files and their options to create a working menu

def menuFiles():
    with open(r"Pt9_10DB\songsMenu.txt") as mainMenu:
        userMenu = mainMenu.read()
    with open(r"Pt9_10DB\reportOptions.txt") as reportsMenu:
        userReport = reportsMenu.read()
    return userMenu, userReport

def songsMenu():
    options = 0 # create option variable and initialise it with integer value 0
    optionsList = ["1","2","3","4","5","6"] # create a list with string values
    # call/invoke the menuFiles function and assign/initialise with the userChoice variable
    userChoices = menuFiles()

    # while 0 not in ["1","2","3","4","5","6"] 
    while options not in optionsList: # execute the indented code
        print(userChoices[0])

        # re-assign the options variable with the input function(which has a default string data type)
        options = input("Enter an option from the songs main menu choices above: ") # "1"/"2"

        # check to see if the reassigned options variable(value) is not in the optionsList(list) 
        if options not in optionsList:
            print(f"{options} is not a valid choice in the songs menu! ")
    return options

# create a boolean variable and assign with a True value 
mainProgram = True
while mainProgram: # same as While True
    
    mainMenu = songsMenu() # assign songsMenu function to the mainMenu variable
    #call/invoke the respective modules with their function

    if mainMenu == "1":
        readSongs.read_data()
    elif mainMenu == "2":
        addSongs.insert_data()
    elif mainMenu == "3":
        updateSongs.updateData()
    elif mainMenu == "4":
        deleteSongs.deleteData()
    elif mainMenu == "5":
        #call reports
        print("This is the reports menu")
    else:
        # reassign the mainProgram boolean variable with a False value
        mainProgram = False
input("Press Enter to quit the songs app")

def reportsMenu():
    options = 0
    optionsList = ["1","2","3"]
    reportChoices = menuFiles() # calling the menuFiles() function and assigning it to a variable

    while options not in optionsList:
        print(reportChoices[1]) # menuFiles returns 2 variables, we want the second one
        options = input("Enter an option from the reports sub menu above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports sub menu!")
        return options # returns a value 1,2 or 3






