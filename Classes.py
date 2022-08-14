# Program to demonstrate classes

# Declare Hero class
class Hero:
    
    # Constructor
    def __init__(self, name, age, gender, race, vocation):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.vocation = vocation
        
    # Print character details
    def hero_details(self):
        print("Name of character is ", self.name)
        print("Age of character is ", self.age)
        print("Gender of character is ", self.gender)
        print("Race of character is ", self.race)
        print("Vocation of character is ", self.vocation)
    
    # Define attack
    def attack(self):
        print(self.name, " attacks!")
        
    # Define defense
    def defend(self):
        print(self.name, " defends!")
        
    # Define item use
    def item(self):
        print(self.name, " uses item!")
    
    # Define magic
    def magic(self):
        print(self.name, " casts magic!")
        
    # Define running
    def run(self):
        print(self.name, " runs away!")
        
# Define Hero subclass Druid
class Druid(Hero):
    
    # Override Hero constructor
    def assign_form_familiar(self, animal_form, familiar):
        self.animal_form = animal_form
        self.familiar = familiar
    
    # Show character is druid
    def show_druid_details(self):
        print(self.name, "is a druid.")
        print("Their animal form is a ", self.animal_form)
        print("Their familiar is a ", self.familiar)

# Define Hero subclass Mage
class Mage(Hero):
    
    # Override Hero constructor
    def assign_attributes(self, element):
        self.element = element
        
    # Show character is mage
    def show_mage(self):
        print(self.name, "is a mage.")
        print("Their element is ", self.element)
        
# Define hybrid class Beastmage
class Beastmage(Druid, Mage):
    
    # Beastmage constructor
    def assign_attributes(self, element, animal_form, familiar, hybrid_ability):
        self.element = element
        self.animal_form = animal_form
        self.familiar = familiar
        self.hybrid_ability = hybrid_ability
        
    def show_beastmage(self):
        print(self.name, "is a beastmage.")
        print("Their animal form is a ", self.animal_form)
        print("Their familiar is a ", self.familiar)
        print("Their element is ", self.element)
        print("Their hybrid ability is ", self.hybrid_ability)

# Define instance of hero
hero_jeremy = Beastmage("Jeremy", 38, "male", "human", "beastmage")

# Show hero attributes
hero_jeremy.hero_details()

# Assign druid details
hero_jeremy.assign_attributes("wood", "deer", "cat", "animagic")

# Show hero is a beastmage
hero_jeremy.show_beastmage()

# Print line break
print()

# Demonstrate hero actions
hero_jeremy.attack()
hero_jeremy.defend()
hero_jeremy.item()
hero_jeremy.magic()
hero_jeremy.run()