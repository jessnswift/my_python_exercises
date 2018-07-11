# Create a Dog class that:
# 1) Inherits from Animal
# 2) Has its own prop of "breed"
# 3) initializes the Animal class with'species', 'leg_num' and 'domesticated' attributes

class Dog(Animal):
    def _init_(self, breed):
      self.breed = breed
      super().__init__("Dog", leg_num=4, domesticated=True)

    def spea():
      return f'I am a dog, and I like to say {self.say_something()}'


