# AI-Assisted Technical Documentation Generator

## 1. Project Overview
This project is an automated documentation system designed to reduce manual drafting time by approximately 40%. It utilizes **FastAPI** for the backend, **AST (Abstract Syntax Tree)** for precise structural analysis, and the **Salesforce CodeT5** model to generate professional, accurate docstrings for Python code.

## 2. Key Features
- **Interactive Web Interface:** A clean, browser-based UI where users can paste code, view results side-by-side, and download documentation as a Markdown (\`.md\`) file.
- **Intelligent AST Parsing:** - Extracts only top-level functions, classes, and methods.
  - Automatically ignores internal/nested helper functions to keep documentation clean.
  - Correctly handles decorators (e.g., `@staticmethod`, custom decorators) without confusion.
  
- **State-of-the-Art AI:** - Uses `Salesforce/codet5-base-multi-sum`, a specialized Text-to-Text Transfer Transformer trained specifically for code summarization.
  - Operates in "Raw Mode" (Direct Code-to-Text) to prevent hallucinations or conversational artifacts.

- **Automated Logging:** - Includes a stress-testing script that saves results to a `results/` folder.
  - Log files are timestamped (e.g., `run_complex_test_results_2025-10-27_10-30.txt`) for easy version tracking.

- **Developer Experience:** - Automatic redirect from the homepage (`/`) to the interactive API docs (`/docs`).
  - Asynchronous non-blocking architecture using FastAPI.

## 3. Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Framework** | FastAPI | High-performance web framework for building APIs. |
| **Parsing** | Python `ast` | Native library for abstract syntax tree processing. |
| **AI Model** | Transformers | Hugging Face library running `Salesforce/codet5-base-multi-sum`. |
| **Server** | Uvicorn | ASGI web server implementation. |

## 4. Directory Structure

```text
AIDocGenerator/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point & Redirect logic
│   ├── models.py          # Pydantic data schemas
│   ├── parser.py          # AST extraction logic
│   └── generator.py       # CodeT5 model integration
├── results/               # Auto-generated test logs
├── requirements.txt       # Project dependencies
├── run_complex_test.py    # Stress testing script
└── README.md              # Project documentation
```

## 5. Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd AIDocGenerator
   ```

2. **Set up the Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 6. Usage

### Starting the Server
Run the application using Uvicorn:
```bash
python3 -m app.main
```
*The first run will download the AI model (~900MB).*

### Interactive Testing (Browser)
1. Open your browser and visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
   *(You will be automatically redirected to the Swagger UI)*.
2. Click **POST /generate-docs** -> **Try it out**.
3. Paste a JSON object containing your code (ensure newlines are escaped as `\n`).
4. Click **Execute**.

### Automated Stress Testing & Logging
To test the system against complex code (classes, error handling, decorators) and save the output:

1. Run the included test script:
   ```bash
   python3 run_complex_test.py
   ```

2. Check the results:
   - The output will appear in the terminal.
   - A permanent log file will be created in the `results/` directory.

## 7. Troubleshooting

- **"Model not found" or Download Stuck:**
  Ensure you have a stable internet connection. The model download only happens on the first launch.

- **"Address already in use":**
  Another process is using port 8000. Kill the process or change the port in `app/main.py`.

- **Redirects not working:**
  Ensure you are visiting `http://127.0.0.1:8000/` (http, not https).

## 8. License
Distributed under the MIT License.
