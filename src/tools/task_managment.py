from typing import Optional
from src.utils.tracking import track_tool_usage

@track_tool_usage
def task_managment_tool(date: str, category: Optional[str] = None, priority: Optional[str] = None, **kwargs) -> str:
    """
    This tool manages tasks and to-do lists for specific dates.
    
    Args:
        date: The date to get tasks for (YYYY-MM-DD format)
        category: Optional category filter for tasks
        priority: Optional priority filter (low, medium, high)
    
    Returns:
        str: task list for the specified date
    """
    # Structured mock data for internal use
    structured_tasks = {
        "tasks": [
            {
                "title": "Team standup",
                "time": "10:00 AM",
                "category": "meetings",
                "priority": "high",
                "duration": 30,
                "participants": 8
            },
            {
                "title": "Client presentation",
                "time": "2:00 PM",
                "category": "meetings",
                "priority": "high",
                "duration": 60,
                "participants": 12
            },
            {
                "title": "Project proposal deadline",
                "time": "5:00 PM",
                "category": "deadlines",
                "priority": "high",
                "duration": 0
            },
            {
                "title": "Review pull requests",
                "category": "todos",
                "priority": "medium",
                "duration": 45
            },
            {
                "title": "Update documentation",
                "category": "todos",
                "priority": "low",
                "duration": 90
            }
        ]
    }

    # Filter tasks based on category and priority
    filtered_tasks = [
        task for task in structured_tasks["tasks"]
        if (not category or task["category"] == category) and
           (not priority or task["priority"] == priority)
    ]

    # If no tasks match the filters
    if not filtered_tasks:
        return "No tasks found for this date"

    # Format output string
    output = f" Task List for {date}:"
    for task in filtered_tasks:
        time_info = f" ({task['time']})" if "time" in task else ""
        output += f"\n- {task['title']}{time_info} [category: {task['category']}] [priority: {task['priority']}]"

    return output