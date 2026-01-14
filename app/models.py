from pydantic import BaseModel
from typing import List

class CodeRequest(BaseModel):
    source_code: str

class DocStringResponse(BaseModel):
    entity_name: str
    entity_type: str
    original_code: str
    generated_docstring: str

class DocumentationResult(BaseModel):
    results: List[DocStringResponse]
