import unittest
from feedback import TASKS, check_code


class FeedbackTests(unittest.TestCase):

    def test_supported_solutions(self):
        for task, data in TASKS.items():
            self.assertTrue(check_code(task, data["solution"])["correct"])

    def test_missing_return(self):
        result = check_code("Functions", TASKS["Functions"]["starter"])
        self.assertFalse(result["correct"])
        self.assertIn("return", result["issue"])

    def test_syntax_error(self):
        result = check_code("Functions", "def add(")
        self.assertIn("syntax", result["issue"])

    def test_alternative_solution(self):
        result = check_code("Functions", "def add(a,b):\n    return b+a")
        self.assertIn("cannot verify", result["issue"])

    def test_feedback_detail(self):
        code = TASKS["Functions"]["starter"]
        short = check_code("Functions", code)
        long = check_code("Functions", code, True)
        self.assertEqual(short["issue"], long["issue"])
        self.assertEqual(short["next_step"], long["next_step"])
        self.assertGreater(len(long["suggestion"]), len(short["suggestion"]))

    def test_empty_input(self):
        self.assertFalse(check_code("Functions", "")["correct"])


if __name__ == "__main__":
    unittest.main()
