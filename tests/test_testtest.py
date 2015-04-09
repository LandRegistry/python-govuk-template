import unittest


class TestTestTest(unittest.TestCase):

    def test_should_fail(self):
        with self.assertRaises(RuntimeError):
            raise

    def test_should_pass(self):
        self.assertEquals(True, True)
