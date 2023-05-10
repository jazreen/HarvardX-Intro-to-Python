#LISTS
students = ["Hermione", "Harry", "Ron"]

for student in students: 
#fun fact: for loops can be used for string too in python!!
#student (not students) is just a random variable that now corresponds to 
#each item in the list and gets "incremented" till the end of list is reached
#we could've used 's' or anything else instead of 'student'
    print(student)

#if you wanted to use numbers instead of string for for loop
for i in range(len(students)):
    print(students[i]) #similar to array notation in C
    print(i + 1, students[i]) #if we wanted to list the number as well as the names

print()  #just prints empty new line
#DICTIONARIES
studs = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
#to print the houses (the names here are dictionary keys)
print(studs["Hermione"]) #should print Gryffindor
print(studs["Draco"]) #should print Slytherin

print()

#More efficient if we do it in a for loop:
for stud in studs: #here, stud is the key and studs is the dictionary
    print(stud, studs[stud], sep=",")
    #the 'stud' prints the keys (names)
    #the 'studs[stud]' prints the corresponding "definitions" (houses)
    #if we dont have sep=",", the key and the definition will be separated by just a space,
    #making it look like a last name to the names. The comma overwrites the space.

#what if there are more info for each student?
# we create a LIST that contains a DICTIONARY for each student

print() 

sts = [
    {"name": "Hermione","house": "Gryffindor", "patronous":"Otter"},
    {"name": "Draco","house": "Slytherin", "patronous": None} #None is actually a command in python
]

for s in sts: #here, s = a dictionary (in the list of dictionaries)
    print(s["name"], s["house"], s["patronous"], sep=", ")
    #name, house and patronous are keys here

