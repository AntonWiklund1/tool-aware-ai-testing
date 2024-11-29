from pydantic import BaseModel
from typing import List
from langchain_core.caches import BaseCache
from typing import Optional, Any

class SimpleCache(BaseCache):
    def __init__(self):
        self._cache = {}

    def lookup(self, prompt: str, llm_string: str) -> Optional[Any]:
        return self._cache.get((prompt, llm_string))

    def update(self, prompt: str, llm_string: str, return_val: Any) -> None:
        self._cache[(prompt, llm_string)] = return_val

    def clear(self) -> None:
        self._cache.clear()

class ToolSelectionData(BaseModel):
    prompt: str
    prompt_category: str
    correct_tools: List[str]