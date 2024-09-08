from abc import ABC

class AbstractAnimal(ABC):
    def sound(self):
        pass

class Dog(AbstractAnimal):
    def sound(self):
        return 'wonderful'

class Cat(AbstractAnimal):
    def sound(self):
        return 'nyami'
    
def animal_sound(animal: AbstractAnimal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
