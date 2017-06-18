import csv


# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for key in inventory:
        print(str(inventory[key]) + " " + str(key)) 
    print("Total number of items: " + str(sum(inv.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for loot_item in added_items:
        if loot_item in inventory:
            inventory[loot_item] += 1
        else:
            inventory[loot_item] = 1


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    for key in inventory:
        if "\t" in key:
            inventory[key.replace("\t", "    ")] = inventory[key]
            inventory.pop(key)

    INDENTATION = 2
    COUNT_HEADER = "count"
    ITEM_NAME_HEADER = "item name"

    inventoryList = []

    for key in inventory:
        inventoryList.append((key, inventory[key]))

    if order is not None:
        orderInListForm = order.split(",")
        sortBy = orderInListForm[0]
        sortDirection = orderInListForm[1]

        if sortBy == "count":
            secondElement = lambda t: t[1]
            inventoryList = sorted(inventoryList, key = secondElement, reverse = (sortDirection == "desc"))

    numberOfDigits = lambda n: len(str(n))

    longestNumberLength = 0
    longestNameLength = 0

    for item in inventoryList:

        longestNameLength = max(longestNameLength, len(item[0]))

        longestNumberLength = max(longestNumberLength, numberOfDigits(item[1]))

    longestNumberLength = max(longestNumberLength, len(COUNT_HEADER))
    longestNameLength = max(longestNameLength, len(ITEM_NAME_HEADER))

    print("Inventory:")

    headerText = \
        (" " * INDENTATION) \
        + (" " * (longestNumberLength - len(COUNT_HEADER))) \
        + COUNT_HEADER \
        + (" " * INDENTATION) \
        + (" " * (longestNameLength - len(ITEM_NAME_HEADER))) \
        + ITEM_NAME_HEADER

    print(headerText)
    print("-" * len(headerText))

    for item in inventoryList:

        print( \
                (" " * INDENTATION) \
                + (" " * (longestNumberLength - numberOfDigits(item[1]))) \
                + str(item[1]) \
                + (" " * INDENTATION) \
                + (" " * (longestNameLength - len(item[0]))) \
                + item[0] \
            )

    print("-" * len(headerText))

    totalNumberOfItems = 0

    for item in inventoryList:
        totalNumberOfItems += item[1]

    print("Total number of items: " + str(totalNumberOfItems))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    csvFile = open(filename, "r")
    for line in csvFile:
        if line[-1] == "\n":
            line = line[:-1]

        lineItems = line.split(",")

        add_to_inventory(inventory, lineItems)

    csvFile.close()

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    inventoryString = ""

    for item in inventory:

        itemString = (item + ",") * inventory[item]

        inventoryString += itemString

    csvFile = open(filename, "w")

    csvFile.write(inventoryString[:-1])

    csvFile.close()
