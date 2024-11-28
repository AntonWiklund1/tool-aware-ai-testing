from pydantic import BaseModel, Field
from typing import List, Optional, Union, Dict

class DatabaseToolParams(BaseModel):
    query: str = Field(..., description="The SQL query to execute")

class StatisticalAnalysisToolParams(BaseModel):
    data: List[Union[int, float, Dict]] = Field(..., description="List of numerical data points to analyze")
    analysis_type: str = Field(..., description="Type of analysis to perform (mean, median, mode, std_dev, all)")
    confidence_level: Optional[float] = Field(0.95, description="Confidence level for statistical calculations (0-1)")

class SearchWebToolParams(BaseModel):
    query: str = Field(..., description="The search query to look up information about")

class TaskManagmentToolParams(BaseModel):
    date: str = Field(..., description="The date to get tasks for (YYYY-MM-DD)")
    category: Optional[str] = Field(None, description="Filter tasks by category")
    priority: Optional[str] = Field(None, description="Filter tasks by priority (low, medium, high)")

class CodeToolParams(BaseModel):
    code: str = Field(..., description="The code to execute")
    language: str = Field("python", description="Programming language of the code")
    timeout: Optional[int] = Field(30, description="Maximum execution time in seconds")

class CalendarToolParams(BaseModel):
    start_date: str = Field(..., description="Start date for calendar events (YYYY-MM-DD)")
    days: Optional[int] = Field(7, description="Number of days to look ahead")
    category: Optional[str] = Field(None, description="Filter events by category")
