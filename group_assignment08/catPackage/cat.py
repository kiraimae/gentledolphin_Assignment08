
#cat.py

class Cat:
    def __init__(self, name="Uno"): # Constructor method
        self.name = name
        self.playful = False # Default playfulness
    def set_playful(self, is_playful): #Setter method to change playful status
        self.playful = is_playful
    def get_playful(self):  #Getter method that returns playful status
        return self.playful
    def meow(self): #Prints message
        print(f"{self.name} meows: Meow!")
    def display(self): #Returns string to decsribe cat
        playfulness_status = "wants to play" if self.playful else "is not in the mood to play"
        return f"{self.name} the Cat {playfulness_status}"
    def __str__(self):
        return f"Cat(name={self.name}, playful={self.playful})"
    def __repr__(self):
        return f"Cat({self.name!r})"