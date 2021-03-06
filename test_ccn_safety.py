import unittest

from ccn_safety import replace_digits

class TestRegex(unittest.TestCase):

    text = ("Have you ever noticed, in television and movies, that phone numbers "
        "and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? "
        "It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers "
        "the attention of privacy and security experts.")
    
    expected_text = ("Have you ever noticed, in television and movies, that phone numbers "
        "and credit cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? "
        "It is because a number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers "
        "the attention of privacy and security experts.")

    def test_replace(self):
        safe_text = replace_digits(self.text)
        self.assertFalse("5555-5555-5555-5555" in safe_text, "Numbers not hidden!")
        self.assertFalse("1234-5678-1234-5678" in safe_text, "Numbers not hidden!")
        self.assertTrue("XXXX-XXXX-XXXX-5555" in safe_text, "Converted numbers are missing!")
        self.assertTrue("XXXX-XXXX-XXXX-5678" in safe_text, "Converted numbers are missing!")
        self.assertEqual(self.expected_text, safe_text, "Paragraphs do not match!")

if __name__ == "__main__":
    unittest.main()

 
