import unittest
from decoder import Decoder

class MorseTester(unittest.TestCase):
    # Set up decoder class
    def setUp(self):
        self.decoder_ = Decoder()

    # Testing for right encoding
    def test_encode(self):
        message = "I am Groot! =)"
        self.assertEqual(self.decoder_.encode(message=message),
                         ".. / .- -- / --. .-. --- --- - -.-.-- / -...- -.--.-")
    # For right decoding
    def test_decode(self):
        message = ".. / .- -- / --. .-. --- --- - -.-.-- / -...- -.--.-"
        self.assertEqual(self.decoder_.decode(message=message),
                         "I Am Groot! =)")

    # Tests for Errors
    def test_encode_error(self):
        # In message middle letter "o" is not latin it is from cyrillic alphabet
        message = "I am Groоot! =)"
        self.assertEqual(self.decoder_.encode(message=message),
                         "Error, 'О' is unknown Symbol.")

    def test_decode_error(self):
        message = ".. / .- -- / --. .-. --- ---- - -.-.-- / -...- -.--.-"
        self.assertEqual(self.decoder_.decode(message=message),
                         'I Am Gro<"----" Is Unknown Symbol>T! =)')

if __name__ == '__main__':
    unittest.main()
