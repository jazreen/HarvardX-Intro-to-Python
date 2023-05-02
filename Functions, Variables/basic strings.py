
#ignore till line 9, just me playing around
i = 0
while (i < 50):
    i = i + 10
    print("number is %d" % i)
    if (i == 30):
        print('bingo')
#######################

name = input("your name? ")
#age = input ("age?")
print("Hello, " + name) 
#the + can only be used to add at the end of the sentence. % is needed to insert in the middle. cant use both + and %
# + means concatenation

print(f"Hello {name}, this is a new format")
print("using \"quotes\"")

#what if you wanted to capitalise the name and remove white space?

#to remove whitespace
name = name.strip() 
#lstrip, rstrip can be used to strip on the left or right

#to capitalise (first word only)
name = name.capitalize()

#to capitlise the whole phrase
name = name.title()

print(f"{name}")

#split the string in two parts
first, last = name.split(" ") 
#the space in the quotes tells the function where to split (i.e. at the space)

print(f"Your first name is {first}")
print(f"Your last name is {last}")

#to do everything in one go:
province = input("whats your province? ").strip().title()

print(f"You live in {province}")

#to use the python interactive mode, click the + i the tab below, type in python and click enter
#when the >>> appears, type in something to execute e.g. 1+1 and click enter

#to create a new file, type in code in the terminal
