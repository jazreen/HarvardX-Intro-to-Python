#PART 1: introducing modulus operator (%) and bool data type
#bool can only have 2 values: true(1) or false(0)
#PART 2: match (case)

def main():
    x = int(input("x? " ))
    if is_even(x): #basically saying 'if is_even() function is true...'
        print("It's even")

    else:
        print("It's odd")

#CASE/MATCH STATEMENTS
name = input("your name?")
match name:
    case "harry"| "hermione"|"ron": # | means or
        print("Griffindor")

    case "drako":
        print("slytherin")

    case _: #_ means 'for any other cases'
        print("Who?")




def is_even(num):
    #if num % 2 == 0:
     #   return True
     

  #  else:
       # return False

   return True if num % 2 == 0 else False
    #OR since the modulus will only give 1 or 0, we can directly do:
    # return n % 2 == 0


main()
