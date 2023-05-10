#using while loops
i = 0
while i < 3:
    print("meow")
    i += 1

#using for loops
for j in [0, 1, 2]: #the square bracket stuff is a list
    print("meow1")
#lists will be impractical when we want to loop for large amounts of times

#better alternative:
for j in range(3): 
    print("meow1")

#the var j here is unnecessary, in python we can replace it with a _
for _ in range(3): 
    print("meow1.5")


#a python alternative:
print("meow2\n" * 3)
#to avoid going to next line after printing for the last time:
print("moew3\n" * 3, end="") #just means put nothing at the end instead of newline


#what if we wanted to ask the user how many times to repeat?
while True: #this is an INFINITE LOOP unless broken out of
    n = int(input("n? "))
    if n > 0:
        break #it only breaks out of the while loop under which its called
    #alternatively we could do:
    #if n < 0:
        #continue
    #else:
        #break

for _ in range(n):
    print("meow4")

#a function to get the number of meows, n:
def get_num():
    while True:
        n = int(input("n? "))
        if n > 0:
            return n
            #or we can do: 
            # break
#return n


