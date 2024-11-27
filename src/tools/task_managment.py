from typing import Optional

def task_managment_tool(date: str, category: Optional[str] = None, priority: Optional[str] = None, **kwargs) -> str:
    """
    This tool manages tasks and to-do lists for specific dates.
    
    Args:
        date: The date to get tasks for (YYYY-MM-DD format)
        category: Optional category filter for tasks
        priority: Optional priority filter (low, medium, high)
    
    Returns:
        str:  task list for the specified date
    """
    mock_tasks = {
        "meetings": "Team standup at 10:00 AM\nClient presentation at 2:00 PM",
        "deadlines": "Project proposal due by 5:00 PM",
        "todos": "Review pull requests\nUpdate documentation",
        "all": """
 Task List for {date}:
- Team standup (10:00 AM) [category: meetings] [priority: high]
- Client presentation (2:00 PM) [category: meetings] [priority: high]
- Project proposal deadline (5:00 PM) [category: deadlines] [priority: high]
- Review pull requests [category: todos] [priority: medium]
- Update documentation [category: todos] [priority: low]
"""
    }

    return mock_tasks.get("all", "No tasks found for this date").format(date=date)