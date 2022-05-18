# Final Project Part 1. 2348 python
# #Name: Victor Lopez
# Student ID: 1243931
# Date: 5/7/2022

from datetime import datetime      # Allows to access time
import csv                         # csv files use


# Begin output for classes
class InventoryReports:
    def __init__(self, item_list_1):
        self.item_list = item_list_1      # new file for list


    # Part A
    # Build a FullInventory.csv for inventory
    # Alphabetical & Sequential - ID, Manufacture, Item , Price, Service, Damaged (y/n)
    def fullInventory(self):
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])   # get key order based on manufacturer
            for item in keys:
                id = item
                file.write('{},{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate, damaged))

    # Section B
    # Make Inventorylist with specifications
    # 3 csv files: Phone, Tower, & Laptop Inventories
    # Sequence: ID, manufacture, price, service date, and damaged (y/n)
    def inventoryList(self):
        items = self.item_list(types = [])
        keys = sorted(items.keys())                 # sort by ID
        for item in items:
            item_sort = items[item]['item_sort']
            if item_sort not in types:
                types.append(item_sort)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('D:\v-Docs\UH Spring 2021\Python 2348\Homeworks pdfs':'Inventorylist' + '-' + file_name, 'w') as file:
            #line 40 error, is this not where I show where on my computer where i want the new file made?
            for item in keys:
                id = item
                today = datetime.now().date()
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                damaged = items[item]['damaged']
                    if type == itemType:
                        file.write('{},{},{},{},{}\n'.format(ID, Manufacture, Price, Service_Date, Damaged))

    #Part C
    #Create PastServiceDateInventory.csv
    def pastService(self):
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date())
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                today = datetime.now().date()
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                damaged = items[item]['damaged']
                serviceDate = items[item]['service_date']
                service_expiration = datetime.strptime(serviceDate, "%m/%d/%Y").date()
                expired = service_expiration < today

    # Part D
    # Make DamagedInventory.csv
    def damagedInventory(self):
        items = self.item_list
        #order to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'])
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                today = datetime.now().date()
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                damaged = items[item]['damaged']
                if damaged:                                      # write damaged items
                    file.write('{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate))
                    # copy from section a, b


if __name__ == '__main__':           #main program
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']        #create list of input files and read every files
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacture = line[1]
                    itemType = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacture.strip()
                    items[item_id]['item_type'] = itemType.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    serviceDate = line[1]
                    items[item_id]['service_date'] = serviceDate

    inventory = InventoryReports(items)
    # Create all the output files
    inventory.fullInventory()
    inventory.pastService()
    inventory.damagedInventory()
    inventory.inventoryList()

    # Part 2
# data dictionary

data = {"id" : [1167234, 2347800, 2390112, 9034210, 7346234, 1009453, 3001265],

"manufacturer":["Apple", "Apple", "Dell", "Dell", "Lenovo", "Lenovo", "Samsung"],

"type" : ["phone", "laptop", "laptop", "tower", "laptop", "tower", "phone"],

"price": [534, 999, 799, 345, 239, 599, 1200],

"date": [2/1/2022, 7/3/2020, 7/2/2020, 5/27/2020, 9/1/2021, 10/1/2021, 12/1/2023],

"condition": [' ', ' ', ' ', ' ', ' ', 'damaged', ' ', ' ']}

# while loop
# contiue loop unless q
while True:
    user_input = input("Enter item or q to quit: ")
    if user_input == "q":
        break
    item = ""
    types = ""
    for i in data["manufacturer"]:
        if i in user_input:
            item = i
    for i in data["type"]:
        if i in user_input:
            types = i
    if(item == "" or types == ""):                             #check input
        print("No such item in inventory")
    else:
        details = ["", "", "", 0]
        for i in range(len(data["id"])):
            if(data["manufacturer"][i] == item and data["type"][i] == types):
                if(details[2] < data["price"][i]):
                    details[0] = data["id"][i]
                    details[1] = data["manufacturer"][i]
                    details[2] = data["type"][i]
                    details[3] = data["price"][i]
        print("Your item is " + str(details[0]) + " " + str(details[1]) + " " + str(details[2]) + " " + str(details[3]))
