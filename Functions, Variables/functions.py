#learning to write functions in python

#to call functions, make sure to include the main function AND call it at the end of the code
#unlike in c, main function won't run by itself unless called to at the end**

def main():
    name = input("what's your name? ")
    hello1(name) #should print name
    hello2() #should print 'world' as no input given
    hello2(name) #should print name

    x = int(input("what's x? "))
    print("x squared is", square(x))

    #another approach:
    print("x squared is %d" % square(x)) #NOTE: we DONT put a comma after the "" when using this syntax with %






def hello1(to): #no default setting present in this function
    print("hello,", to) 
    #this syntax seems to already place a space after the end of the print statement- no need to manually add a space
    # alternative syntax: print(f"hello, {to}")

#if we want to set a default value to the function, needed when no input is given to the function
def hello2(to = "world"):
    print("hello,", to) 

#functions with return values
def square(num):
    return num * num
    #2 alternative forms:

    #return num ** 2 
    # ** means 'to the power of'

    #return pow(num, 2)
    #using a pre-defined python function, pow



main() #DO NOT FORGET