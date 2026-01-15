# AI-Assisted Technical Documentation Generator

## 1. Project Overview
This project is an automated documentation system designed to reduce manual drafting time by approximately 40%. It utilizes **FastAPI** for the backend logic and **Streamlit** for a user-friendly frontend. The system uses **AST (Abstract Syntax Tree)** parsing and the **Salesforce CodeT5** AI model to generate accurate, professional docstrings for Python code.

## 2. Key Features

- **Interactive Web Interface:** A clean, browser-based UI where users can paste code, view results side-by-side, and download documentation as a Markdown (`.md`) file.
- **Intelligent Parsing:** Extracts only top-level functions and classes, ignoring internal logic to keep docs clean.
- **AI-Powered:** Uses the `Salesforce/codet5-base-multi-sum` model for pure Code-to-English translation (no hallucinations).
- **Automated Logging:** Saves timestamped results of stress tests to a `results/` folder.
- **Dual-Mode:** Use via the Web UI or directly via API (Swagger/cURL).

## 3. Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interactive web dashboard. |
| **Backend** | FastAPI | High-performance API with CORS support. |
| **AI Model** | Transformers | CodeT5 (Summarization Model). |
| **Parsing** | Python `ast` | Structural code analysis. |

## 4. Directory Structure

```text
AIDocGenerator/
├── app/
│   ├── main.py            # API Entry point (CORS enabled)
│   ├── generator.py       # AI Model Logic
│   └── ...
├── frontend/
│   └── ui.py              # Streamlit Web Interface
├── results/               # Auto-generated logs
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## 5. Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd AIDocGenerator
   ```

2. **Set up Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 6. Usage (The Workflow)

To run the full system, you need **two terminal tabs** open.

### Step 1: Start the Backend (The Brain)
In the first terminal:
```bash
python3 -m app.main
```
*Wait for "Uvicorn running on http://127.0.0.1:8000"*

### Step 2: Start the Frontend (The Interface)
Open a new terminal tab (ensure `venv` is active) and run:
```bash
streamlit run frontend/ui.py
```
*This will automatically open the website in your browser.*

### Step 3: Use the Tool
1. Paste your Python code into the web interface.
2. Click **Generate Documentation**.
3. View the AI explanations and click **Download (.md)** to save them.

## 7. License
Distributed under the MIT License.
