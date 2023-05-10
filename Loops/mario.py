#making loops in loops

#code to create a "square" block with hashtags
def main():
    print_square(3)
    print()
    print_square2(4)
    print()
    print_square3(5)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="") 
            #the end="" prevents printing #s on a new line while its still on the same row 

        print()
        #this statement after the inner for loop prints a new line only after the row is complete

#alternative function
def print_square2(size):
    for _ in range(size):
        print("#" * size)


#alternative 2
def print_square3(size):
    for _ in range(size):
        print_row(size)


def print_row(size):
    print("#" * size)


main()

