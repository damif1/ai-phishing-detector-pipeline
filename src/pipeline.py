import json
from src.ingestor import EmailIngestor
from src.parser import EmailParser
from src.normalizer import Normalizer

def run_pipeline():
    # Setup
    ingestor = EmailIngestor(method="file")
    parser = EmailParser()
    normalizer = Normalizer()
    
    # Process
    print("Starting Phishing Scanner Pipeline...")
    emails = ingestor.fetch_emails("./data/raw_emails")
    
    results = []
    
    for i, email_obj in enumerate(emails):
        try:
            print(f"Processing email #{i+1}...")
            parsed = parser.parse(email_obj)
            normalized = normalizer.normalize(parsed)
            
            # --- AI ANALYSIS STEP (Placeholder) ---
            # In a real app, you would send 'normalized' to an LLM here.
            # prediction = ai_agent.scan(normalized) 
            # normalized['risk_score'] = prediction['score']
            
            results.append(normalized)
            
        except Exception as e:
            print(f"Error processing email #{i+1}: {e}")

    # Task 6: Persist results (JSONL is best for logs)
    with open("./data/logs/scan_results.jsonl", "w") as f:
        for entry in results:
            f.write(json.dumps(entry) + "\n")
            
    print(f"Done. Processed {len(results)} emails.")

if __name__ == "__main__":
    run_pipeline()