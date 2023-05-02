#doing comparisons in python
x = int(input("x? "))
y = int(input("y? "))

if x > y:
    print("x is bigger than y")

#elif is only checked if the first (IF) condition is false
elif x < y:
    print("x is smaller than y")

#elif x == y:
else: #because if x isnt > y or < y, there's only 1 other possibility
    print("they're the same")

if x>y or x<y: #OR: if x!=y:
    print("x is not equal to y")
    #similarly, 'and' operator can be used

else: 
    print("x is equal to y")



#new example
score = int(input("SCORE: "))

if score >= 90:
    print("Grade: A")

#NOTE: the sequence of elifs matter. 
# We only enter the next elif statement if the first one in the sequence is false
elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")


