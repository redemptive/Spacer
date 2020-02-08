import unittest
import Game
from GameObject import GameObject

class TestGameObject(unittest.TestCase):
    def test_x_pos(self):
        test_x = 10
        gameObject = GameObject.GameObject(test_x, 2, 10, 10)
        self.assertEqual(test_x, gameObject.x)

if __name__ == '__main__':
    unittest.main()