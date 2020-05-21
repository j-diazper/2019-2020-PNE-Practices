import json
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# -- Read the First name
firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']

# Print the information on the console, in colors
print()
print("Name: ", end="")
print(firstname, lastname)
print("Age: ", end="")
print(age)