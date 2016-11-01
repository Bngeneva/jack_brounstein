# Part 1

students = [ 
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'},
]

for student in students:
	print(student["first_name"] + " " + student["last_name"])

# Part 2

users = {
	'Students': [ 
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'},
	],
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'},
	]
}

# Option 1
# This uses basic for-loops over the dictionary and string addition.  In terms of syntax, it's very similar to what the code would look like in JavaScript.

for user_type in users:
	print(user_type)
	for i in range(len(users[user_type])):
		print(str(i+1) + " - " + users[user_type][i]["first_name"].upper() + " " + users[user_type][i]["last_name"].upper() + " - " + str(len(users[user_type][i]["first_name"]+users[user_type][i]["last_name"])))

# ...but that's not especially readable, and Python has some built-in methods and functions we can use to clean it up.

for user_type, user_list in users.items(): # Python 2 users should replace this with "users.iteritems()" -- but do you know why?
	print(user_type)
	for idx, user in enumerate(user_list):
		name = (user["first_name"] + " " + user["last_name"]).upper()
		print("{} - {} - {}".format(idx+1, name, len(name)-1))