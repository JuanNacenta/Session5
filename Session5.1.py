name= input("What is your name? ")
age= input("How old are you going to be this year? ")
#if we put a number in letter age(int) doesnt read it
# The mistake is not very problematic because only appears because values while running= Exceptions
# A severe mistake is when python doesnt let you run the code because an error.
try:
    age= int(age)
    birth_year = 2023 - age
except ValueError:
    print("sorry, that was not a valid number")
    exit(1)
except NameError:
    print("Oh, its not you, is me :'")
#Podemos mover estas ultimas lineas al try, entonces no será necesario el exit en except
else:
    print(name, "you were born in", birth_year)
#finally siempre aparecerá al final del codigo, aunque haya habiado un error
finally:
    print("Thanks for playing, cum again")
