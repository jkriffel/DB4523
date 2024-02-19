from Database import DB

def createNewDatabase():
    database = DB()
    database.createDatabase()

def openDatabase():
    database = DB()
    if (database.ocDatabase("open")):
        print("Database opened successfully.\n")
    else: 
         print("Database already opened, or file does not exist\n")

def closeDatabase():
    database = DB()
    if (database.ocDatabase("close")):
        print("Database closed successfully.\n")
    else: 
         print("Database already closed, or file does not exist\n")

def displayRecord(searchId,isOpen):
    database = DB()
    database.displayRecord(searchId,isOpen)

def createReport():
    database = DB()
    database.createReport()

def updateRecord(changeId,searchId,changedField):
   database = DB()
   database.updateRecord(changeId, searchId,changedField)

def deleteRecord(searchId):
    database = DB()
    database.deleteRecord(searchId)

def addRecord(ID, FN, LN, Age, TicketNumber, Fare, DOP):
    database = DB()
    database.addRecord(ID, FN, LN, Age, TicketNumber, Fare, DOP)    


def main():
    # while True:
    #     print("\nOptions:")
        print("Option 1: Create New Database")
        print("Option 2: Open Database")
        print("Option 3: Close Database")
        print("Option 4: Display Record")
        print("Option 5: Create Report")
        print("Option 6: Update Record")
        print("Option 7: Delete a Record")
        print("Option 8: Add a Record")
        print("Option 0: Exit Program\n")

    #     choice = input("Enter the number corresponding to your choice:\n")

    #     if choice == '1':
    #         createNewDatabase()
    #     elif choice == '2':
    #         openDatabase()
    #     elif choice == '3':
    #         closeDatabase()
    #     elif choice == '4':
    #         displayRecord()
    #     elif choice == '5':
    #         createReport()
    #     elif choice == '6':
    #         updateRecord()
    #     elif choice == '7':
    #         deleteRecord()
    #     elif choice == '8':
    #         addRecord()
    #     elif choice == '0':
    #         print("Exiting the program. Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please enter a number between 0 and 9.")

        # HW1 Part 1 test cases --> 
        # createNewDatabase()
        # openDatabase()
        # readRecord(0)
        # readRecord(19)
        # readRecord(6)
        # readRecord(-1)
        # readRecord(1000)
            
        # HW1 Part 2 test cases -->
        createNewDatabase()
        displayRecord(100,False)
        openDatabase()
        displayRecord(2,True)
        displayRecord(3,True)
        displayRecord(16,True)
        displayRecord(20,True)
        displayRecord(-1,True)

        # Update value -- SearchId, Change Value
        # 1 = FN   2 = LN  3 = Age  4 = Ticket Number  5 = Fare  6 = DOP
        displayRecord(2,True) # Display record 2
        updateRecord(3,2,"34") # Update Age on record 2 to 34
        displayRecord(2,True) # Display record 2 to see if it was updated
        displayRecord(3,True) # Display record 3 
        updateRecord(0,3,"10") # Update ID on record 3 to 10 -- Should fail
        displayRecord(3,True) # Display record 3
        displayRecord(20,True)
        updateRecord(6,20,"1/20/1912") # Update DOP on record 20 to 1/20/1912
        displayRecord(20,True) # Display record 20

        deleteRecord(2)
        displayRecord(2,True)

        deleteRecord(12)
        displayRecord(12,True)

        deleteRecord(100) # Should fail

        createReport()

        addRecord(100,"Sam","Gauch","44","PA 1012","43.33","2/5/1912")
        updateRecord(3,100,"56")

        closeDatabase()

        displayRecord(2,False)
 
main()