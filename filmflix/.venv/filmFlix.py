import addFilms, deleteFilms, updateFilms, readFilms, reports

def menuFiles():
    with open(r"filmflix\.venv\optionsMenu.txt") as mainMenu:
        userMenu = mainMenu.read()
    with open(r"filmflix\.venv\reportsMenuOptions.txt") as reportsMenu:
        userReport = reportsMenu.read()
    return userMenu, userReport

def filmsMenu():
    options = 0
    optionsList = ["1", "2", "3", "4", "5", "6"]
    userChoices = menuFiles()
    
    while options not in optionsList:
        print(userChoices[0])
        options = input("Enter an option from the film menu choices above: ")
        
        if options not in optionsList:
            print(f"{options} is not a valid choice in the film menu! ")
    return options

def reportsMenu():
    options = 0
    optionsList = ["1", "2", "3", "4", "5"]
    userChoices = menuFiles()
    
    while options not in optionsList:
        print(userChoices[1])
        options = input("Enter an option from the reports menu choices above: ")
        
        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports menu! ")
    return options

mainProgram = True
while mainProgram:
    mainMenu = filmsMenu()

    if mainMenu == "1":
        addFilms.insertData()
    elif mainMenu == "2":
        deleteFilms.deleteData()
    elif mainMenu == "3":
        updateFilms.updateData()
    elif mainMenu == "4":
        readFilms.readData()
    elif mainMenu == "5":
        reportsProgram = True
        while reportsProgram:
            reportMenu = reportsMenu()

            if reportMenu == "1":
                reports.reportAll()
            elif reportMenu == "2":
                reports.reportGenre()
            elif reportMenu == "3":
                reports.reportYear()
            elif reportMenu == "4":
                reports.reportRating()
            else:
                reportsProgram = False
    else:
        mainProgram = False

input("Press Enter to quit the film app")
