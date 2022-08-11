import unittest
from parameterized import parameterized
from stack.hw_stack import pairs, is_brackets_balanced


class TestFunctiuns(unittest.TestCase):

    @parameterized.expand(
        [
            ("(", ")", True),
            ("[", "}", False)
        ]
    )
    def test_pairs(self, open, close, result):
        c_result = pairs(open, close)
        self.assertEqual(c_result, result)

    @parameterized.expand(
        [
            ("(((([{}]))))", True),
            ("[([])((([[[]]])))]{()}", True),
            ("{{[()]}}", True),
            ("}{}", False),
            ("{{[(])]}}", False),
            ("[[{())}]", False)
        ]
    )
    def test_is_brackets_balanced(self, brackets_string, result):
        c_result = is_brackets_balanced(brackets_string)
        self.assertEqual(c_result, result)
