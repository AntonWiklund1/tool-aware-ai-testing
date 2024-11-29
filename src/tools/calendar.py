from typing import Optional, Dict, List, Union
from src.utils.tracking import track_tool_usage

@track_tool_usage
def calendar_tool(start_date: str, days: int = 7, category: Optional[str] = None, **kwargs) -> str:
    """
    Get calendar events for a specified date range.
    
    Args:
        start_date: Start date for calendar events (YYYY-MM-DD)
        days: Number of days to look ahead (default: 7)
        category: Optional category filter for events
    
    Returns:
        str: Calendar events for the specified period
    """
    # Structured mock data for internal use
    structured_events = {
        "events": [
            {
                "title": "Team Planning Meeting",
                "day": "Monday",
                "time": "9:00 AM",
                "category": "meetings",
                "duration": 60,
                "participants": 10,
                "location": "Conference Room A"
            },
            {
                "title": "Client Review",
                "day": "Tuesday",
                "time": "2:00 PM",
                "category": "meetings",
                "duration": 90,
                "participants": 5,
                "location": "Virtual"
            },
            {
                "title": "Project Deadline",
                "day": "Wednesday",
                "time": "5:00 PM",
                "category": "deadlines",
                "duration": 0,
                "deliverables": ["Final Report", "Code Documentation"]
            },
            {
                "title": "Dentist Appointment",
                "day": "Thursday",
                "time": "11:00 AM",
                "category": "personal",
                "duration": 45,
                "location": "Downtown Dental"
            },
            {
                "title": "Team Retrospective",
                "day": "Friday",
                "time": "3:00 PM",
                "category": "meetings",
                "duration": 60,
                "participants": 8,
                "location": "Conference Room B"
            }
        ]
    }

    # Filter events based on category
    filtered_events = [
        event for event in structured_events["events"]
        if not category or event["category"] == category
    ]

    # If no events match the filter
    if not filtered_events:
        return f"No events found for the period {start_date} to +{days} days"

    # Format output string
    output = f"Calendar Events ({start_date} to +{days} days):"
    for event in filtered_events:
        output += f"\n- {event['day']}: {event['title']} ({event['time']}) [category: {event['category']}]"

    return output