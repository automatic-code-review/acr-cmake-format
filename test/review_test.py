import unittest

from src import review


class MyTestCase(unittest.TestCase):
    def test_not_formated(self):
        config = {'config': 'cmake-format-config.json', 'path_output': 'not-formated', 'path_source': 'not-formated',
                  'path_target': 'not-formated'}
        comments = [
            {'comment': 'Formatação incorreta no arquivo CMakeLists.txt', 'id': 'eaecb3890e3b098f1213d7762b9015ae',
             'position': {'endInLine': 1, 'language': 'cmake', 'path': 'CMakeLists.txt', 'snipset': False,
                          'startInLine': 1}},

            {'comment': 'Formatação incorreta no arquivo test.cmake', 'id': '5d6ffea06b57c74f9823a3cdf638a519',
             'position': {'endInLine': 1, 'language': 'cmake', 'path': 'test.cmake', 'snipset': False,
                          'startInLine': 1}}
        ]

        self.assertEqual(review.review(config), comments)

    def test_formated(self):
        config = {'config': 'cmake-format-config.json', 'path_output': 'formated', 'path_source': 'formated',
                  'path_target': 'formated'}
        comments = []

        self.assertEqual(review.review(config), comments)


if __name__ == '__main__':
    unittest.main()
