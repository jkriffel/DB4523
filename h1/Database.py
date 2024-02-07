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
        self.rec_size = 73
        self.idSize = 7
        self.fnSize = 10
        self.lnSize = 20
        self.ageSize = 5
        self.ticketSize = 10
        self.fareSize = 10
        self.dopSize = 10

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

            #write an empty records
            filestream.write("{:{width}.{width}}".format('_empty_',width=self.idSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.fnSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.lnSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.ageSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.ticketSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.fareSize))
            filestream.write("{:{width}.{width}}".format(' ',width=self.dopSize))
            filestream.write("\n")

        with open(text_filename,"w") as outfile:
            for dict in data_list:
                writeRecord(outfile,dict)

        # Write the config file
        # try:
        #     with open(config_filename, "x") as config_file:
        #         config = configparser.ConfigParser()        
        #         config.add_section('ConfigNumRecords') 
        #         config.add_section('ConfigRecordSize')      
        #         config.add_section('isOpened')                
        #         config.set('ConfigNumRecords','num_records','20')                          
        #         config.set('ConfigRecordSize','record_size','74')
        #         config.set('isOpened','is_opened','False')                               
        #         config.write(config_file)     
        # except FileExistsError:
        #     print("Config file already exists")           
        
        try:
            with open(config_filename, "x") as config_file:
                config_data = {
                    'ConfigNumRecords': {'num_records': '20'},
                    'ConfigRecordSize': {'record_size': '74'},
                    'isOpened': {'is_opened': 'False'}
                }
                config_file.write(config_data)
                # config_file.write("[ConfigNumRecords]\n")
                # config_file.write(f"num_records = {config_data['ConfigNumRecords']['num_records']}\n\n")
                # config_file.write("[ConfigRecordSize]\n")
                # config_file.write(f"record_size = {config_data['ConfigRecordSize']['record_size']}\n\n")
                # config_file.write("[isOpened]\n")
                # config_file.write(f"is_opened = {config_data['isOpened']['is_opened']}\n")

        except FileExistsError:
            print("Config file already exists")           

    def ocDatabase(self, oc):
        # # filename = input("\nWhat DB file do you want to open?\n")
        # # config_filename = filename + ".config"
        # config_filename = "SmallTitanic.config"
        # if (config_filename):
        #     config = configparser.ConfigParser()
        #     config.read(config_filename)
        #     isOpened = config.get('isOpened','is_opened')
        #     if isOpened == 'False' and oc == 'open':
        #         config.set('isOpened','is_opened','True')
        #         with open(config_filename, "w") as config_file:
        #             config.write(config_file)
        #         return True
        #     elif isOpened == 'True' and oc == 'close':
        #         config.set('isOpened','is_opened','False')
        #         with open(config_filename, "w") as config_file:
        #             config.write(config_file)
        #         return True
        # else:
        #     return False
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

    # read record method
        # self.record_size = 20
        # self.rec_size = 74
    def readRecord(self):
        try:
            recordNum = int(input("\nWhat record number do you want to read?\n"))
        except ValueError:
            return {"status": -1, "message": "Invalid Input"}
        
        text_filename = open("SmallTitanic.data", 'r+')
        self.flag = False

        id = firstName = lastName = age = ticket = fare = dop = "None"

        if recordNum >= 0 and recordNum <= self.record_size:
            text_filename.seek(0,0)
            text_filename.seek(recordNum*self.rec_size)
            line = text_filename.readline().rstrip('\n')
            self.flag = True
            print(line)
            return {"status": 1,"message": "Record Found"}
        
        if self.flag:
            id = line[0:7]
            firstName = line[7:17]
            lastName = line[17:37]
            age = line[37:42]
            ticket = line[42:52]
            fare = line[52:62]
            dop = line[62:72]
            
            self.record = dict({"ID":id,"firstName":firstName,"lastName":lastName,"age":age,"ticketNum":ticket,"fare":fare,"DOP":dop})
            return {"status": 0, "message": "Record Blank"}
        else:
            return {"status": -1, "message": "Record not found"}

    # def createDB(self, filename): 
    #     csv_filename = filename + ".csv"
    #     # Read the CSV file and write into data files
    #     with open(csv_filename, "r") as csv_file:
    #         data_list = list(csv.DictReader(csv_file,fieldnames=('ID','firstName','lastName','age','ticketNum','fare','DOP')))
    #         return data_list
        
    #     print(data_list)

        # def writeRecord(self, data_list):
        #     text_filename = filename + ".data"

        #     def writeDB(filestream, dict):
        #       filestream.write("{:{width}.{width}}".format(dict["ID"],width=self.idSize))
        #       filestream.write("{:{width}.{width}}".format(dict["firstName"],width=self.fnSize))
        #       filestream.write("{:{width}.{width}}".format(dict["lastName"],width=self.lnSize))
        #       filestream.write("{:{width}.{width}}".format(dict["age"],width=self.ageSize))
        #       filestream.write("{:{width}.{width}}".format(dict["ticketNum"],width=self.ticketSize))
        #       filestream.write("{:{width}.{width}}".format(dict["fare"],width=self.fareSize))
        #       filestream.write("{:{width}.{width}}".format(dict["DOP"],width=self.dopSize))
        #       filestream.write("\n")
              
        #     with open(text_filename,"w") as outfile:
        #         for dict in data_list:
        #             writeDB(outfile,dict)

        # data = readCSV(DB)
        # writeRecord(DB,data)


    #read the database
    def readDB(self, filename, DBsize, rec_size):
        self.filestream = filename + ".data"
        self.record_size = DBsize
        self.rec_size = rec_size
        
        if not os.path.isfile(self.filestream):
            print(str(self.filestream)+" not found")
        else:
            self.text_filename = open(self.filestream, 'r+')

    # #read record method
    # def getRecord(self, recordNum):

    #     self.flag = False
    #     id = experience = marriage = wage = industry = "None"

    #     if recordNum >=0 and recordNum < self.record_size:
    #         self.text_filename.seek(0,0)
    #         self.text_filename.seek(recordNum*self.rec_size)
    #         line= self.text_filename.readline().rstrip('\n')
    #         self.flag = True
        
    #     if self.flag:
    #         id = line[0:10]
    #         experience = line[10:15]
    #         marriage = line[15:20]
    #         wage = line[20:40]
    #         industry = line[40:70]
    #         self.record = dict({"ID":id,"experience":experience,"marriage":marriage,"wages":wage,"industry":industry})

    #Binary Search by record id
    def binarySearch(self, input_ID):
        low = 0
        high = self.record_size - 1
        found = False
        self.recordNum = None  # Initialize the insertion point

        while not found and high >= low:
            self.middle = (low + high) // 2
            self.getRecord(self.middle)
            mid_id = self.record["ID"]

            if mid_id.strip() == "_empty_":
                non_empty_record = self.findNearestNonEmpty(self.middle, low, high)
                if non_empty_record == -1:
                    # If no non-empty record found, set recordNum for potential insertion
                    self.recordNum = high 
                    print("Could not find record with ID..", input_ID)
                    return False

                self.middle = non_empty_record
                self.getRecord(self.middle)
                mid_id = self.record["ID"]
                if int(mid_id) > int(input_ID):
                    self.recordNum = self.middle - 1
                else:
                    self.recordNum = self.middle + 1

            if mid_id != "_empty_":
                try:
                    if int(mid_id) == int(input_ID):
                        found = True
                        self.recordNum = self.middle
                    elif int(mid_id) > int(input_ID):
                        high = self.middle - 1
                    elif int(mid_id) < int(input_ID):
                        low = self.middle + 1
                except ValueError:
                    # Handle non-integer IDs
                    high = self.middle - 1

        if not found and self.recordNum is None:
            # Set recordNum to high + 1 if no suitable spot is found
            self.recordNum = high 
            print("Could not find record with ID", input_ID)

        return found

    def findNearestNonEmpty(self, start, low_limit, high_limit):
        step = 1  # Initialize step size

        while True:
            # Check backward
            if start - step >= low_limit:
                self.getRecord(start - step)
                if self.record["ID"].strip() != "_empty_":
                    #print(self.record)
                    return start - step

            # Check forward
            if start + step <= high_limit:
                self.getRecord(start + step)
                if self.record["ID"].strip() != "_empty_":
                    #print(self.record)
                    return start + step

            # Increase step size and repeat
            step += 1

            # Terminate if beyond the search range
            if start - step < low_limit and start + step > high_limit:
                break

        return -1  # No non-empty record found

    #close the database
    def CloseDB(self):

        self.text_filename.close()
