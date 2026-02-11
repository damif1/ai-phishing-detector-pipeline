from bs4 import BeautifulSoup
import re

class EmailParser:
    def parse(self, email_obj):
        """Extracts safe content from an email object."""
        body = ""
        html_content = ""
        
        # 1. Get Body (Handle multipart)
        if email_obj.is_multipart():
            for part in email_obj.walk():
                ctype = part.get_content_type()
                if ctype == "text/plain":
                    body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
                elif ctype == "text/html":
                    html_content += part.get_payload(decode=True).decode('utf-8', errors='ignore')
        else:
            body = email_obj.get_payload(decode=True).decode('utf-8', errors='ignore')

        # 2. If no plain text, strip HTML to create it
        if not body and html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            body = soup.get_text()

        # 3. Extract Links (Safe extraction)
        links = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', body + html_content)

        return {
            "subject": email_obj["Subject"],
            "from": email_obj["From"],
            "to": email_obj["To"],
            "date": email_obj["Date"],
            "body_text": body.strip(),
            "links": list(set(links)), # Remove duplicates
            "attachments": self._get_attachments(email_obj)
        }

    def _get_attachments(self, email_obj):
        files = []
        for part in email_obj.walk():
            if part.get_content_maintype() == 'multipart': continue
            if part.get('Content-Disposition') is None: continue
            
            filename = part.get_filename()
            if filename:
                files.append({
                    "filename": filename,
                    "size_bytes": len(part.get_payload(decode=True) or b""),
                    "content_type": part.get_content_type()
                })
        return files