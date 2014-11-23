import unittest

from ccn_safety2 import replace_ccn

class TestRegex(unittest.TestCase):

    text = ("Have you ever noticed, in television and movies, that phone numbers "
        "and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? "
        "It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers "
        "the attention of privacy and security experts.")
    
    expected_text = ("Have you ever noticed, in television and movies, that phone numbers "
        "and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? "
        "It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers "
        "the attention of privacy and security experts.")

    def test_replace(self):
        safe_text = replace_ccn(self.text)
        self.assertFalse("5555-5555-5555-5555" in safe_text, "Numbers not hidden!")
        self.assertFalse("1234-5678-1234-5678" in safe_text, "Numbers not hidden!")
        self.assertEqual(self.expected_text, safe_text, "Paragraphs match!")
        

if __name__ == "__main__":
    unittest.main()

