from Database import DB

def createNewDatabase():
    database = DB()
    database.createDatabase()

def openDatabase():
    database = DB()
    if (database.ocDatabase("open")):
        print("Database opened successfully.")
    else: 
         print("Database already opened, or file does not exist")

def closeDatabase():
    database = DB()
    if (database.ocDatabase("close")):
        print("Database closed successfully.")
    else: 
         print("Database already closed, or file does not exist")

def readRecord():
    database = DB()
    response = database.getRecord(3)
    print(response)
    # if (response['status'] == 1):
    #     print(response['message'])
    # if (response['status'] == 0):
    #     print(response['message'])
    # if (response['status'] == -1):
    #     print(response['message'])
       

def displayRecord():
    database = DB()
    database.binarySearch(2)

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
        print("Option 0: Exit Program\n")

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

        # HW1 test cases --> 
        # createNewDatabase()
        # openDatabase()
        # readRecord(0)
        # readRecord(19)
        # readRecord(6)
        # readRecord(-1)
        # readRecord(1000)
        

main()
