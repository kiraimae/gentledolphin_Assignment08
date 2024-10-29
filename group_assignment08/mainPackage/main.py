# Name: Alexis Tipkemper-Sparks / Kayla Wilson / Jared Rababy 
# email: Tipkemam@mail.uc.edu / Wilso5ky@mail.uc.edu / rababyjd@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024 HALLOWEENIE
# Course #/Section: IS4010
# Semester/Year:  Fall 2024
# Brief Description of the assignment: VS project in github repo

# Brief Description of what this module does: Tortures us relentlessly by having us practice committing/pushing 
# and pull requests through collaborating on Github 
# Citations: Prof. Nicholson / Past assignments / StackOverflow / GeeksforGeeks
# Anything else that's relevant: Nada
# ***********************************
#main.py

from dogPackage.dog import Dog
from catPackage.cat import Cat
if __name__ == "__main__": 


    def main():
       # Create instances of each pet 
       dog = Dog("Barkington") 
       cat = Cat("Uno") 
    # Display initial states 
       print(dog.display()) 
       print(cat.display())
    # Call unique methods 
       dog.bark() 
       cat.meow()
    # Use setters to change attributes 
       dog.set_mood("relaxed") 
       cat.set_playful(True) # Set playfulness to True 
    # Display updated states 
       print(dog.display()) 
       print(cat.display()) 
main()


