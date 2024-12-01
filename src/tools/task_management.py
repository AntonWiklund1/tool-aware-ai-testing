from typing import Optional
from src.utils.tracking import track_tool_usage

@track_tool_usage
def task_management_tool(date: str,
                        category: Optional[str] = None,
                        priority: Optional[str] = None,
                        assignee: Optional[str] = None,
                        status: Optional[str] = None,
                        due_within_days: Optional[int] = None,
                        **kwargs) -> str:
    """
    Task management tool with advanced filtering and organization.

    Use this tool to manage your tasks and to-do lists. Not for calendar management.
    
    Args:
        date: The date to get tasks for (YYYY-MM-DD)
        category: Filter by category
        priority: Filter by priority
        assignee: Filter by assigned person
        status: Filter by task status
        due_within_days: Filter tasks due within specified days
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
           (not priority or task["priority"] == priority) and
           (not assignee or task["assignee"] == assignee) and
           (not status or task["status"] == status) and
           (not due_within_days or task["due_within_days"] <= due_within_days)
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