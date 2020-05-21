import json
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-2.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print("Name: ", end="")
print(person['Firstname'], person['Lastname'])
print("Age: ",end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
print("Phone numbers: ", end='')
print(len(phoneNumbers))

# Print all the phone numbers
for i, num in enumerate(phoneNumbers):
    print("Phone {}:".format(i), end='')
    print(num)