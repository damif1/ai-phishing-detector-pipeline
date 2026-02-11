import imaplib
import email
import os

class EmailIngestor:
    def __init__(self, method="file", credentials=None):
        self.method = method
        self.credentials = credentials

    def fetch_emails(self, source):
        """Yields raw email objects."""
        if self.method == "file":
            # Loop through a directory of .eml files
            for filename in os.listdir(source):
                if filename.endswith(".eml"):
                    with open(os.path.join(source, filename), 'rb') as f:
                        yield email.message_from_bytes(f.read())
        
        elif self.method == "imap":
            # Connect to Gmail/Outlook (Make sure to use App Passwords!)
            mail = imaplib.IMAP4_SSL(self.credentials['host'])
            mail.login(self.credentials['user'], self.credentials['pass'])
            mail.select('inbox')
            status, messages = mail.search(None, 'ALL')
            for num in messages[0].split():
                status, data = mail.fetch(num, '(RFC822)')
                yield email.message_from_bytes(data[0][1])