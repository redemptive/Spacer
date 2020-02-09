import unittest
import Game
from Game import GameObject

class TestGameObject(unittest.TestCase):
    def test_x_pos(self):
        print("GameObject should take a parameter for x position")
        test_x = 10
        gameObject = GameObject(test_x, 2, 10, 10)
        self.assertEqual(test_x, gameObject.x)
    
    def test_y_pos(self):
        print("GameObject should take a parameter for y position")
        test_y = 10
        gameObject = GameObject(10, test_y, 10, 10)
        self.assertEqual(test_y, gameObject.y)

    def test_width(self):
        print("GameObject should take a parameter for width")
        test_width = 10
        gameObject = GameObject(10, 2, test_width, 10)
        self.assertEqual(test_width, gameObject.width)
    
    def test_height(self):
        print("GameObject should take a parameter for height")
        test_height = 10
        gameObject = GameObject(10, 10, 10, test_height)
        self.assertEqual(test_height, gameObject.height)

    def test_move(self):
        print("GameObject.move(dX, dY) should move the gameobject by the specified values")
        start_x = 10
        start_y = 20
        dX = 5
        dY = 2
        gameObject = GameObject(start_x, start_y, 10, 10)
        gameObject.move(dX, dY)
        self.assertEqual(start_x + dX, gameObject.x)
        self.assertEqual(start_y + dY, gameObject.y)

if __name__ == '__main__':
    unittest.main()