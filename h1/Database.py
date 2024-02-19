import csv
import os.path
#import configparser
# Homework 1 part 1 by Zachary Anderson and James Riffel
# bytes long for titanic.csv == 200 (records plus spaces) * 25 = 5000 bytes
# bytes long for smallTitatnic.csv == 20 (records plus spaces) * 25 = 500 bytes

class DB:   
    #default constructor
    def __init__(self):
        self.record_size = 20
        # save as 74 for windows // 73 for linux --> SmallTitanic
        self.rec_size = 74
        self.idSize = 7
        self.fnSize = 10
        self.lnSize = 20
        self.ageSize = 5
        self.ticketSize = 10
        self.fareSize = 10
        self.dopSize = 10


    def printRecord(self, record):
        print("ID:", record["ID"])
        print("First Name:", record["firstName"])
        print("Last Name:", record["lastName"])
        print("Age:", record["age"])
        print("Ticket Number:", record["ticketNum"])
        print("Fare:", record["fare"])
        print("Date of Purchase:", record["DOP"],"\n")

    # create database
    def createDatabase(self):
        # filename = input("\nWhat CSV file are you creating from?\n")
        filename = "SmallTitanic"
        #Generate file names
        csv_filename = filename + ".csv"
        text_filename = filename + ".data"
        config_filename = filename + ".config"

        # Read the CSV file and write into data files
        with open(csv_filename, "r") as csv_file:
            data_list = list(csv.DictReader(csv_file,fieldnames=('ID','firstName','lastName','age','ticketNum','fare','DOP')))

		# Formatting files with spaces so each field is fixed length, i.e. ID field has a fixed length of 10 
        def writeRecord(filestream, dict):
            filestream.write("{:{width}.{width}}".format(dict["ID"],width=self.idSize))
            filestream.write("{:{width}.{width}}".format(dict["firstName"],width=self.fnSize))
            filestream.write("{:{width}.{width}}".format(dict["lastName"],width=self.lnSize))
            filestream.write("{:{width}.{width}}".format(dict["age"],width=self.ageSize))
            filestream.write("{:{width}.{width}}".format(dict["ticketNum"],width=self.ticketSize))
            filestream.write("{:{width}.{width}}".format(dict["fare"],width=self.fareSize))
            filestream.write("{:{width}.{width}}".format(dict["DOP"],width=self.dopSize))
            filestream.write("\n")

        with open(text_filename,"w") as outfile:
            for dict in data_list:
                writeRecord(outfile,dict)
                emptyRecord = {"ID": "0", "firstName": "Null", "lastName": "Null", "age": "0", "ticketNum": "s", "fare": "0", "DOP": "Null"}
                writeRecord(outfile, emptyRecord)

        # Opening a config file for writing details
        config_fileptr = open(config_filename, "w")
        config_fileptr.write(str(self.rec_size) + "\n")
        config_fileptr.write(str(self.record_size) + "\n")
        config_fileptr.close()
      
        print("Database created successfully\n")

    def getRecord(self, recordNum):
            text_filename = open("SmallTitanic.data", 'r+')
            self.flag = False
            id = firstName = lastName = age = ticket = fare = dop = "None"

            if recordNum >= 0 and recordNum <= self.record_size:
                text_filename.seek(0,0)
                text_filename.seek(recordNum*self.rec_size)
                line = text_filename.readline().rstrip('\n')
                self.flag = True
            else:
                self.flag = False
                self.record = dict({"ID": "0", "firstName": "Null", "lastName": "Null", "age": "0", "ticketNum": "0", "fare": "0", "DOP": "Null"})
        
            if self.flag:
                id = line[0:7]
                firstName = line[7:17]
                lastName = line[17:37]
                age = line[37:42]
                ticket = line[42:52]
                fare = line[52:62]
                dop = line[62:72]
                self.record = dict({"ID":id,"firstName":firstName,"lastName":lastName,"age":age,"ticketNum":ticket,"fare":fare,"DOP":dop})


    def ocDatabase(self, oc):
        config_filename = "SmallTitanic.config"
        if oc == 'open':
            try:
                with open(config_filename, "r") as config_file:
                    isOpened = False
                    for line in config_file:
                        if line.strip() == 'is_opened = True':
                            isOpened = True
                            break
                if not isOpened:
                    with open(config_filename, "a") as config_file:
                        config_file.write("is_opened = True\n")
                    return True
            except FileNotFoundError:
                with open(config_filename, "w") as config_file:
                    config_file.write("is_opened = True\n")
                return True
        elif oc == 'close':
            try:
                with open(config_filename, "r") as config_file:
                    lines = config_file.readlines()
                with open(config_filename, "w") as config_file:
                    for line in lines:
                        if line.strip() != 'is_opened = True':
                            config_file.write(line)
                    config_file.write("is_opened = False\n")  # Add this line to set is_opened to False
                    return True
            except FileNotFoundError:
                return False
        else:
            return False


    # Binary Search by record id
    def binarySearch (self, input_ID):
        low = 0
        high = self.record_size - 1
        regularfound = False
        emptyFound = False
        outOfBounds = False
        if (input_ID > self.record_size):
            outOfBounds = True

        while not regularfound or not emptyFound and high >= low:
            if (low > high) : 
                break
            self.middle = (low+high)//2
            # Will update the fields in record dict automatically
            self.getRecord(self.middle)
            mid_id = self.record["ID"]
            #  ------------------------------------------------------------------------- #
            if mid_id != "0      ":
                if int(mid_id) == int(input_ID):
                    regularfound = True
                    break
                elif int(mid_id) > int(input_ID):
                    high = self.middle - 1
                elif int(mid_id) < int(input_ID):
                    low = self.middle + 1
            # #  ------------------------------------------------------------------------- #
            else: 
            # Middle was a ID of 0, therefore we need a new mid
            # If we - 1 to OG mid, we always find a value, and never will go out of bounds as the first and last records exist
                self.getRecord(self.middle -1)
                mid_id = self.record["ID"]
                if int(mid_id) == int(input_ID):
                    emptyFound = True
                    break
                elif int(mid_id) > int(input_ID):
                    high = self.middle - 1
                elif int(mid_id) < int(input_ID):
                    low = self.middle + 1

        if regularfound: 
            self.getRecord(self.middle)
            # self.printRecord(self.record)
            return self.middle
        # ("\nRecord found at position: " + str(self.middle))
        elif emptyFound:
            self.getRecord(self.middle - 1)
            # self.printRecord(self.record)
            return (self.middle - 1) 
        # "\nRecord found at position: " + str(self.middle - 1)
        else:
            if outOfBounds:
                return "Out of Bounds"
            else:
                return "Not Found"
        # "\nCould not find record with ID " + str(input_ID)
    
    def displayRecord(self, searchId):
        searchResult = self.binarySearch(searchId)
        if (searchResult != "Not Found" and searchResult != "Out of Bounds"):
            self.getRecord(searchResult)
            self.printRecord(self.record)
        else:
            if (searchResult == "Not Found"):
                print({"ID": "0", "firstName": "Null", "lastName": "Null", "age": "0", "ticketNum": "0", "fare": "0", "DOP": "Null"},"\n")
            else:
                print("Record out of bounds\n")

    def createReport(self):
        with open("SmallTitanic.data", "r") as file:
            for i in range(0, 20, 1):
                self.getRecord(i)
                if (self.record["ID"] != "0      "):
                    self.printRecord(self.record)
                

    def updateRecord(self, changeId, searchId, changedField):
        searchResult = self.binarySearch(searchId)
        # 1 = FN   2 = LN  3 = Age  4 = Ticket Number  5 = Fare  6 = DOP
        if changeId == 0:
            print("Can not modify ID field\n")
        if changeId == 1:
            changedRecord = {"ID":self.record["ID"],"firstName":changedField,"lastName":self.record["lastName"],"age":self.record["age"],"ticketNum":self.record["ticketNum"],"fare":self.record["fare"],"DOP":self.record["DOP"]}
            self.writeRecord(searchResult,changedRecord)
        if changeId == 2:
            changedRecord = {"ID":self.record["ID"],"firstName":self.record["firstName"],"lastName":changedField,"age":self.record["age"],"ticketNum":self.record["ticketNum"],"fare":self.record["fare"],"DOP":self.record["DOP"]}
            self.writeRecord(searchResult,changedRecord)
        if changeId == 3:
            changedRecord = {"ID":self.record["ID"],"firstName":self.record["firstName"],"lastName":self.record["lastName"],"age":changedField,"ticketNum":self.record["ticketNum"],"fare":self.record["fare"],"DOP":self.record["DOP"]}
            self.writeRecord(searchResult,changedRecord)
        if changeId == 4:
            changedRecord = {"ID":self.record["ID"],"firstName":self.record["firstName"],"lastName":self.record["lastName"],"age":self.record["age"],"ticketNum":changedField,"fare":self.record["fare"],"DOP":self.record["DOP"]}
            self.writeRecord(searchResult,changedRecord)
        if changeId == 5:
            changedRecord = {"ID":self.record["ID"],"firstName":self.record["firstName"],"lastName":self.record["lastName"],"age":self.record["age"],"ticketNum":self.record["ticketNum"],"fare":changedField,"DOP":self.record["DOP"]}
            self.writeRecord(searchResult,changedRecord)
        if changeId == 6:
            changedRecord = {"ID":self.record["ID"],"firstName":self.record["firstName"],"lastName":self.record["lastName"],"age":self.record["age"],"ticketNum":self.record["ticketNum"],"fare":self.record["fare"],"DOP":changedField}
            self.writeRecord(searchResult,changedRecord)
            
    def writeRecord(self, position, dict):
        text_filename = open("SmallTitanic.data", 'r+')
        text_filename.seek(0,0)
        text_filename.seek(position*self.rec_size)
        text_filename.write(str(dict["ID"]).ljust(self.idSize))
        text_filename.write(str(dict["firstName"]).ljust(self.fnSize))
        text_filename.write(str(dict["lastName"]).ljust(self.lnSize))
        text_filename.write(str(dict["age"]).ljust(self.ageSize))
        text_filename.write(str(dict["ticketNum"]).ljust(self.ticketSize))
        text_filename.write(str(dict["fare"]).ljust(self.fareSize))
        text_filename.write(str(dict["DOP"]).ljust(self.dopSize))
        text_filename.write('\n')
    
    def deleteRecord(self, searchId):
        searchResult = self.binarySearch(searchId)
        if (searchResult != "Not Found" and searchResult != "Out of Bounds"):
            emptyRecord = {"ID": "0", "firstName": "Null", "lastName": "Null", "age": "0", "ticketNum": "s", "fare": "0", "DOP": "Null"}
            self.writeRecord(searchResult, emptyRecord)
        else:
            print("No record found\n")

    # def findNearestNonEmpty(self, start, low_limit, high_limit):
    #     step = 1  # Initialize step size

    #     while True:
    #         # Check backward
    #         if start - step >= low_limit:
    #             self.getRecord(start - step)
    #             if self.record["ID"].strip() != "_empty_":
    #                 #print(self.record)
    #                 return start - step

    #         # Check forward
    #         if start + step <= high_limit:
    #             self.getRecord(start + step)
    #             if self.record["ID"].strip() != "_empty_":
    #                 #print(self.record)
    #                 return start + step

    #         # Increase step size and repeat
    #         step += 1

    #         # Terminate if beyond the search range
    #         if start - step < low_limit and start + step > high_limit:
    #             break

    #     return -1  # No non-empty record found

    #close the database
    def CloseDB(self):

        self.text_filename.close()
