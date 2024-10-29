
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


