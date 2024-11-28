# AI Agent Tool Selection Framework Documentation

## 🔧 Tools Overview

### 1. Statistical Analysis Tool

**Name**: statistical_analysis_tool

**Purpose**: Performs statistical analysis on numerical data.
**Parameters**:

- `data`: List of numerical values or dictionaries to analyze
- `analysis_type`: Type of analysis (mean, median, mode, std_dev, all)
- `confidence_level`: Confidence level for calculations (default: 0.95)

**Mock Data Structure**:

- Can analyze numerical arrays directly
- Extracts numerical data from dictionaries with fields:
  - `duration`
  - `participants`
  - Any numerical values

**Example Response**:

```
Statistical Analysis Results:
- Mean: 45.7
- Median: 42.0
- Mode: 37.5
- Standard Deviation: 12.3
- Sample Size: 10
- Total: 457
```

**Example Prompts**:

- "Calculate the mean and standard deviation of these user engagement scores: [0.85, 0.72, 0.93]"
- "What's the median duration of all meetings in my calendar?"
- "Perform a complete statistical analysis on this dataset with a 99% confidence level"

### 2. Calendar Tool

**Name**: calendar_tool

**Purpose**: Retrieves calendar events for a specified date range.
**Parameters**:

- `start_date`: Start date for calendar events (YYYY-MM-DD)
- `days`: Number of days to look ahead (default: 7)
- `category`: Optional category filter for events

**Mock Data Structure**:

```json
{
  "title": "Team Planning Meeting",
  "day": "Monday",
  "time": "9:00 AM",
  "category": "meetings",
  "duration": 60,
  "participants": 10,
  "location": "Conference Room A"
}
```

**Example Response**:

```
Calendar Events (2024-03-20 to +7 days):
- Monday: Team Planning Meeting (9:00 AM) [category: meetings]
- Tuesday: Client Review (2:00 PM) [category: meetings]
```

**Example Prompts**:

- "Show me all meetings scheduled for next week"
- "What events do I have in the 'personal' category starting from 2024-03-15?"
- "List all events with more than 5 participants for the next 14 days"

### 3. Database Tool

**Name**: database_tool

**Purpose**: Executes SQL queries and returns results.
**Parameters**:

- `query`: The SQL query to execute

**Mock Data Structure**:

```json
{
  "user_id": 1,
  "number_of_posts": 156,
  "registered_at": "2023-01-15T10:30:00",
  "last_login": "2024-03-10T15:45:00",
  "country": "USA",
  "city": "Seattle",
  "language": "en",
  "gender": "F",
  "engagement_score": 0.85
}
```

**Example Response**:

```
| user_id | number_of_posts | country | city    |
|---------|----------------|---------|---------|
| 1       | 156            | USA     | Seattle |
| 2       | 89             | Canada  | Toronto |
```

**Example Prompts**:

- "SELECT number_of_posts, country FROM users WHERE engagement_score > 0.8"
- "Show me all users who registered in the last 3 months"
- "Get the average number of posts by country"

### 4. Task Management Tool

**Name**: task_managment_tool

**Purpose**: Manages tasks and to-do lists.
**Parameters**:

- `date`: The date to get tasks for (YYYY-MM-DD)
- `category`: Optional filter for task category
- `priority`: Optional priority filter (low, medium, high)

**Mock Data Structure**:

```json
{
  "title": "Team standup",
  "time": "10:00 AM",
  "category": "meetings",
  "priority": "high",
  "duration": 30,
  "participants": 8
}
```

**Example Response**:

```
Task List for 2024-03-20:
- Team standup (10:00 AM) [category: meetings] [priority: high]
- Client presentation (2:00 PM) [category: meetings] [priority: high]
```

**Example Prompts**:

- "Show me all high-priority tasks for 2024-03-15"
- "What meetings do I have scheduled for today?"
- "List all tasks in the 'deadlines' category for next week"

### 5. Web Search Tool

**Name**: search_web_tool

**Purpose**: Searches the web for information.
**Parameters**:

- `query`: The search query to look up information about

**Mock Data Categories**:

- technology
- business
- default

**Mock Data Structure**:

```json
{
  "title": "Latest Developments in AI Technology",
  "snippet": "Recent breakthroughs in artificial intelligence...",
  "link": "https://example.com/ai-developments",
  "published_date": "2024-03-01"
}
```

**Example Response**:

```
Search Results for: AI developments
1. Latest Developments in AI Technology
   Recent breakthroughs in artificial intelligence...
   Source: https://example.com/ai-developments
   Published: 2024-03-01
```

**Example Prompts**:

- "Show me all high-priority tasks for 2024-03-15"
- "What meetings do I have scheduled for today?"
- "List all tasks in the 'deadlines' category for next week"

### 6. Code Tool

**Name**: code_tool

**Purpose**: Executes code snippets and returns results.
**Parameters**:

- `code`: The code to execute
- `language`: Programming language (python, javascript, typescript)
- `timeout`: Maximum execution time in seconds (default: 30)

**Mock Data Structure**:

```json
{
  "success": {
    "output": "Hello, World!",
    "execution_time": 0.023,
    "memory_usage": 12.4,
    "cpu_usage": 2.1,
    "python_version": "3.9.5",
    "dependencies": ["numpy", "pandas"]
  },
  "error": {
    "type": "SyntaxError",
    "message": "invalid syntax",
    "line": 3,
    "traceback": "Traceback..."
  }
}
```

**Example Success Response**:

```
Python Execution Result:
> Output: Hello, World!
> Execution time: 0.023s
> Memory usage: 12.4 MB
> CPU usage: 2.1%
> Python version: 3.9.5
> Dependencies: numpy, pandas
```

**Example Error Response**:

```
Python Execution Error:
> Error Type: SyntaxError
> Message: invalid syntax
> Line: 3
> Details: Traceback (most recent call last)...
```

**Example Prompts**:
-```python
import statistics
data = [0.85, 0.72, 0.93]
mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")

```
- "Create a function that calculates all the prime numbers between 1 and 100 and returns the result"

### 7. Summary Tool

**Name**: summary_tool

**Purpose**: Generates summaries of user-uploaded documents (for example in law firms when a lawyer can have multiple documents to a case)
**Parameters**:
No parameters needed

**Mock Data Structure**:
```

- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology.

```


**Example Response**:

```

- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology.

```

**Example Prompts**:

- "Summarize my documents"

## 📝 Tool Integration Notes

- All tools return string output for LLM compatibility
- Tools with structured data can be analyzed using the Statistical Analysis Tool
- Calendar, Task, and Database tools contain numerical data (duration, participants, posts)
- Code tool provides execution metrics that can be analyzed
```
