import unittest
from email.message import EmailMessage
from src.parser import EmailParser

class TestEmailParser(unittest.TestCase):
    def test_link_extraction(self):
        # Create a fake email
        msg = EmailMessage()
        msg.set_content("Click here: http://malicious-site.com")
        msg['Subject'] = "Test Phishing"
        msg['From'] = "bad@guy.com"
        
        parser = EmailParser()
        result = parser.parse(msg)
        
        self.assertIn("http://malicious-site.com", result['links'])
        self.assertEqual(result['from'], "bad@guy.com")

if __name__ == '__main__':
    unittest.main()