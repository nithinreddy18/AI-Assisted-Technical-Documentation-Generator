from pydantic import BaseModel
from typing import List, Optional

class CodeRequest(BaseModel):
    source_code: str
    complexity: str = "concise"  # Options: "concise" or "detailed"

class DocStringResponse(BaseModel):
    entity_name: str
    entity_type: str
    original_code: str
    generated_docstring: str

class DocumentationResult(BaseModel):
    results: List[DocStringResponse]