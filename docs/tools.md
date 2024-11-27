This document outlines all available tools in the AI Agent Tool Selection Framework. Each tool is designed to specific functionality for testing purposes.

## 🔧 Tools Overview

### 1. Statistical Analysis Tool

**Purpose**: Performs statistical analysis on numerical data.
**Parameters**:

- `data`: List of numerical values to analyze
- `analysis_type`: Type of analysis (mean, median, mode, std_dev, all)
- `confidence_level`: Confidence level for calculations (default: 0.95)

**Example Response**:

```

 Statistical Analysis Results:

- Mean: 45.7
- Median: 42.0
- Mode: 37.5
- Standard Deviation: 12.3
- Confidence Interval (95%): [41.2, 50.2]

```

### 2. Calendar Tool

**Purpose**: Retrieves calendar events for a specified date range.
**Parameters**:

- `start_date`: Start date for calendar events (YYYY-MM-DD)
- `days`: Number of days to look ahead (default: 7)
- `category`: Optional category filter for events

**Example Response**:

```
Calendar Events (2024-03-20 to +7 days):

- Monday: Team Planning Meeting (9:00 AM) [category: meetings]
- Tuesday: Client Review (2:00 PM) [category: meetings]
- Wednesday: Project Deadline (5:00 PM) [category: deadlines]
- Thursday: Dentist Appointment (11:00 AM) [category: personal]
- Friday: Team Retrospective (3:00 PM) [category: meetings]
```

### 3. Database Tool

**Purpose**: Executes SQL queries and returns results.
**Parameters**:

- `query`: The SQL query to execute

**Example Response**:

```
| user_id | number_of_posts | country | city |
|---------|----------------|---------|---------|
| 1 | 156 | USA | Seattle |
| 2 | 89 | Canada | Toronto |
| 3 | 234 | UK | London |
```

### 4. Task Management Tool

**Purpose**: Manages tasks and to-do lists.
**Parameters**:

- `date`: The date to get tasks for (YYYY-MM-DD)
- `category`: Optional filter for task category
- `priority`: Optional priority filter (low, medium, high)

### 5. Web Search Tool

**Purpose**: Searches the web for information.
**Parameters**:

- `query`: The search query to look up information about

### 6. Code Tool

**Purpose**: Executes code snippets and returns results.
**Parameters**:

- `code`: The code to execute
- `language`: Programming language (default: python)
- `timeout`: Maximum execution time in seconds (default: 30)

### 7. Summary Tool

**Purpose**: Generates summaries of documents.
**Parameters**:

- `text`: Optional text to summarize

## 📝 Usage in Experiments

Tools can be configured in the experiments by setting up the `AVAILABLE_TOOLS` array. Each tool requires:

- `name`: Tool identifier
- `function`: The tool function
- `description`: Tool documentation
- `schema`: Pydantic model for parameter validation (if applicable)
- `enabled`: Boolean to toggle tool availability
