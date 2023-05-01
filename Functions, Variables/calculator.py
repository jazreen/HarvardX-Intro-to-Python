#x = input("whats x? ")
#y = input("whats y? ")
#inputs are always saved as strings
#so use int() function to convert them to numbers before calculating

#z = int(x) + int(y)
#cant just type x+y because python will think thats string concatenation

#print(z)

#make it more concise (see commented code above):
#switch type from int to flot (for decimals)
x = float(input("whats x? "))
y = float(input("whats y? "))

print(x + y)

#even more concise, though not preferred:
#print(int(input("whats x? ")) + int(input("whats y? ")))

z = round(x + y) #rounds to closest integer ....
print(f"{z}")

u = round((x + y), 3) #.... unless specified by parameter in function spec (optional)
print(f"method 1: {u}")

#another way to round things:
w = x + y
print(f"method 2: {w:.2f}") #NEW NOTATION, says to round to 2 dp in float

#if we want to add commas in big integer numbers:
comma = float(input("type in a number > 999: "))
print(f"{comma:,}") #NEW NOTATION



