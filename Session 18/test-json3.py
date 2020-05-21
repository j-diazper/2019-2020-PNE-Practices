import json
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-3.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors

print("Name: ", end="")
print(person['Firstname'], person['Lastname'])
print("Age: ", end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements in the list
print("Phone numbers: ", end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    print("Phone {}:".format(i))

    # The element num contains 2 fields: number and type
    print("Type: ", end='')
    print(num['type'])
    print("Number: ", end='')
    print(num['number'])