#Python3.8

""" This script will be used to parse information from a csv file called
device_list.csv that I built in Libre Office. It's a very short csv file
but it will allow me to play with the information within to grasp the concept.
Wish me luck! """

import csv

datafile = open("device_list.csv") # File opened

# Here we have to read the data again, similar to a text file.
# Remember --> OPEN, READ, Close
readdata = csv.reader(datafile) # File read
data = list(readdata) # Add data to a list

print(data) # printing the information shows a nested list:

#   [
#   ['LAB_ASR_1', '10.0.0.1', 'ASR1001-X'],
#   ['LAB_ASR_2', '10.0.0.2', 'ASR1001-X'],
#   ['DIS_SW1', '10.0.0.10', 'C9300-48'],
#   ['DIS_SW2', '10.0.0.11', 'C9300-48'],
#   ['ACC_SW1', '10.0.0.12', 'C9200-24'],
#   ['ACC_SW2', '10.0.0.13', 'C9200-24'],
#   ['ACC_SW3', '10.0.0.14', 'C9200-24'],
#   ['ACC_SW4', '10.0.0.15', 'C9200-24']
#   ]

# Each row is separated by a comma. The columns are signified by the values in
# the list. Now we have this data and it works, we can start to play with it.

print(data[0]) # will print the first row of data from the CSV
print(data[1]) # will print the next row of data from the CSV

print("\n=================================================================")
print("\n=================================================================")

# an alternative way to do this is with the 'with' feature as before with text

with open("device_list.csv") as data:
    datafile = csv.reader(data)
    for row in datafile:
        device = row[2]
        ip = row[1]
        name = row[0]
        print(f"{name} has IP address {ip} and is a {device.rstrip()}")
