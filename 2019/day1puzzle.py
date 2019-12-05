import os

working_directory = os.path.dirname(__file__)
input_file_path = working_directory + '/day1input.txt'

totalFuel = 0
modTotFuel = 0
with open(input_file_path) as fp:
    for line in fp:
        weight = int(line)
        moduleFuel = (weight//3) - 2
        modTotFuel += moduleFuel
        while moduleFuel > 0: 
            totalFuel += moduleFuel
            moduleFuel = (moduleFuel//3) - 2

print("Fuel for Modules = " + str(modTotFuel))
print("Fuel for Modules and Fuel = " + str(totalFuel))