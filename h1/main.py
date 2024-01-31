def createNewDatabase():
    print("Creating New Database")

def openDatabase():
    print("Open Database")

def closeDatabase():
    print("Close Database")

def readRecord():
    print("Read Record")

def displayRecord():
    print("Display Record")

def createReport():
    print("Create Report")

def updateRecord():
    print("Update Record")

def deleteRecord():
    print("Delete Record")

def addRecord():
    print("Add Record")


def main():
    while True:
        print("\nOptions:")
        print("Option 1: Create New Database")
        print("Option 2: Open Database")
        print("Option 3: Close Database")
        print("Option 4: Read Record")
        print("Option 5: Display Record")
        print("Option 6: Create Report")
        print("Option 7: Update Record")
        print("Option 8: Delete a Record")
        print("Option 9: Add a Record")
        print("Option 0: Exit Program")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            createNewDatabase()
        elif choice == '2':
            openDatabase()
        elif choice == '3':
            closeDatabase()
        elif choice == '4':
            readRecord()
        elif choice == '5':
            displayRecord()
        elif choice == '6':
            createReport()
        elif choice == '7':
            updateRecord()
        elif choice == '8':
            deleteRecord()
        elif choice == '9':
            addRecord()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

main()