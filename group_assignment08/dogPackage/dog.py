
#dog.py

class Dog:
    def __init__(self, name="Barkington"):
        self.name = name
        self.mood = "happy" # Default mood
    def set_mood(self, new_mood): #Setter method that allows to change mood
        self.mood = new_mood
    def get_mood(self): #Getter method that returns dog mood
        return self.mood
    def bark(self): #Prints message  
        print(self.name + " barks: Woof!")
    def display(self): #Returns string that describes dog
        return self.name + " the Dog is " + self.mood
    def __str__(self):
        return f"Dog(name={self.name}, mood={self.mood})"
    def __repr__(self):
        return f"Dog({self.name!r})"
