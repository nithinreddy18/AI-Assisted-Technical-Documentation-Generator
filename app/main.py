from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware  # <-- NEW IMPORT
from app.models import CodeRequest, DocumentationResult, DocStringResponse
from app.parser import CodeParser
from app.generator import DocGenerator
import uvicorn

app = FastAPI(title='AI-Assisted Tech Doc Generator')

# --- NEW: ALLOW FRONTEND COMMUNICATION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------

parser = CodeParser()
generator = None

@app.on_event('startup')
async def startup_event():
    global generator
    generator = DocGenerator()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.post('/generate-docs', response_model=DocumentationResult)
async def generate_docs(request: CodeRequest):
    if not request.source_code:
        raise HTTPException(status_code=400, detail='Source code cannot be empty.')
    try:
        parsed_entities = parser.parse_code(request.source_code)
        results = []
        for entity in parsed_entities:
            doc_text = generator.generate_docstring(entity['code'])
            results.append(DocStringResponse(
                entity_name=entity['name'],
                entity_type=entity['type'],
                original_code=entity['code'],
                generated_docstring=doc_text
            ))
        return DocumentationResult(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)