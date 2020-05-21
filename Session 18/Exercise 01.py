import json
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-exercise01.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

print(f"Total people in the Database: {len(people)}")

for person in people:
    print("Name: ", end="")
    print(person['Firstname'], person['Lastname'])
    print("Age: ", end="")
    print(person['age'])
    phoneNumbers = person['phoneNumber']
    print("Phone numbers: ", end='')
    print(len(phoneNumbers))
    for i, number in enumerate(phoneNumbers):
        print(" Phone {}:".format(i))
        print("Type: ", end='')
        print(number['type'])
        print("Number: ", end='')
        print(number['number'])