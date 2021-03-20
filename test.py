import unittest
import randomgame

class TestMain(unittest.TestCase):
    def test_checkAnswer(self):
        randomgame.initial_num = 1
        randomgame.final_num = 10
        randomgame.counter = 1
        randomgame.message = 'press enter'
        user_guess = 1
        game_answer = 2
        result = randomgame.check_answer(user_guess, game_answer)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()