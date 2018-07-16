import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog('Bob')

    def test_animal_creation(self):

        self.assertIsInstance(self.bob, Dog)
        self.assertIsInstance(self.bob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_can_set_species(self):
        self.bob.set_species('kitty')
        self.assertEqual(self.bob.species, 'kitty')

    def test_animal_walk(self):
        self.bob.set_legs(4)
        # self.assertEqual(self.bob.speed, 0)
        self.bob.walk()
        self.assertEqual(self.bob.speed, .8)

if __name__=='__main__':
    unittest.main()