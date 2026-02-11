# AI-Powered Phishing Email Scanner (Backend Pipeline)

## 📌 Project Overview
This project is a Python-based security tool designed to automate the ingestion, parsing, and normalization of emails for phishing detection. It serves as the data pipeline that prepares raw email data (from `.eml` files or live IMAP servers) into a structured JSON format suitable for AI/ML analysis.

## 🚀 Features
* **Multi-Source Ingestion**: Supports local `.eml` file processing and live IMAP integration.
* **Robust Parsing**: Extracts headers (From, To, Subject, Date) and handles multipart MIME types.
* **Security-Focused Extraction**: Safely extracts URLs and attachment metadata without executing malicious code.
* **Data Normalization**: Standardizes email content into JSON for AI model consumption.
* **Logging**: Maintains a `scan_results.jsonl` log of all processed items.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **Libraries**: `BeautifulSoup4` (HTML parsing), `re` (Regex), `email` (MIME handling).

## 📁 Project Structure
```text
phishing-scanner/
├── data/
│   ├── raw_emails/       # Input: Drop .eml files here
│   └── logs/             # Output: scan_results.jsonl
├── src/
│   ├── ingestor.py       # Handles email fetching
│   ├── parser.py         # Extracts text and links
│   ├── normalizer.py     # Structures data for AI
│   └── pipeline.py       # Main execution script
├── tests/                # Unit tests for reliability
└── requirements.txt      # Project dependencies

```

## ⚙️ Installation & Usage

1. **Clone the repository**:
```bash
git clone <your-repo-link>
cd phishing-scanner

```


2. **Install Dependencies**:
```bash
pip install -r requirements.txt

```


3. **Run the Scanner**:
Place your `.eml` files in `data/raw_emails/` and run:
```bash
python -m src.pipeline

```


4. **Run Tests**:
```bash
python -m unittest discover tests

```



## 📝 Git Workflow

This project follows **Atomic Commit** principles. Each commit represents a single functional unit (e.g., `feat: add parser`, `test: add unit tests`) to ensure high readability for collaborating developers.


### **How to "Finish" and Test Everything**

1.  **Check your output**: After running `python -m src.pipeline`, open `data/logs/scan_results.jsonl`. It should look like this:
    ```json
    {"id": "a1b2...", "metadata": {"sender": "Security Alert..."}, "content": {"urls": ["http://paypa1..."]}}
    ```
2.  **Verify the GitHub History**: Your "Commits" tab on GitHub should now look like a timeline of your progress, starting from setup to testing.
