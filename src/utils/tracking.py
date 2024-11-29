from functools import wraps
from typing import Callable, List, Dict, Any
import time
from datetime import datetime

class ToolTracker:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tool_calls = []
        return cls._instance
    
    def add_tool_call(self, tool_name: str, args: Dict[str, Any], duration: float, result: str):
        self.tool_calls.append({
            "tool_name": tool_name,
            "timestamp": datetime.now().isoformat(),
            "arguments": args,
            "duration": duration,
            "result": result
        })
    
    def get_tool_calls(self) -> List[Dict[str, Any]]:
        return self.tool_calls
    
    def clear(self):
        self.tool_calls = []

def track_tool_usage(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracker = ToolTracker()
        start_time = time.perf_counter()

        try:
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start_time
            
            # Combine args and kwargs for tracking
            all_args = {
                **{f"arg_{i}": arg for i, arg in enumerate(args)},
                **kwargs
            }
            
            tracker.add_tool_call(
                tool_name=func.__name__,
                args=all_args,
                duration=duration,
                result=str(result)
            )
            
            return result
            
        except Exception as e:
            duration = time.perf_counter() - start_time
            tracker.add_tool_call(
                tool_name=func.__name__,
                args=kwargs,
                duration=duration,
                result=f"Error: {str(e)}"
            )
            raise
    
    return wrapper