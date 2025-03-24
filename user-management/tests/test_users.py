import unittest
from services.utils import validate_email

class TestUtils(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("teste@email.com"))
        self.assertTrue(validate_email("usuario123@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("email_invalido"))
        self.assertFalse(validate_email("usuario@com"))

if __name__ == "__main__":
    unittest.main()
