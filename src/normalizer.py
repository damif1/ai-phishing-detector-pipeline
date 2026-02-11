import json
import hashlib

class Normalizer:
    def normalize(self, parsed_data):
        """Converts parsed data into the schema required by the AI."""
        # Create a unique ID for the email based on content (deduplication)
        content_hash = hashlib.md5((parsed_data['subject'] + parsed_data['date']).encode()).hexdigest()
        
        return {
            "id": content_hash,
            "metadata": {
                "sender": parsed_data['from'],
                "recipient": parsed_data['to'],
                "timestamp": parsed_data['date']
            },
            "content": {
                "subject": parsed_data['subject'],
                "body": parsed_data['body_text'],
                "urls_count": len(parsed_data['links']),
                "urls": parsed_data['links']
            },
            "attachments": parsed_data['attachments']
        }