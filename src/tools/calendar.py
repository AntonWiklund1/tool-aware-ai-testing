from typing import Optional, Dict, List, Union
from src.utils.tracking import track_tool_usage

@track_tool_usage
def calendar_tool(start_date: str, days: int = 7, category: Optional[str] = None, 
                 location: Optional[str] = None, min_participants: Optional[int] = None,
                 max_duration: Optional[int] = None, **kwargs) -> str:
    """
    Gets calendar events for a specified date range with advanced filtering.
    
    Args:
        start_date: Start date for calendar events (YYYY-MM-DD)
        days: Number of days to look ahead (default: 7)
        category: Optional category filter for events
        location: Optional location filter (e.g., "Conference Room A", "Virtual")
        min_participants: Optional minimum number of participants
        max_duration: Optional maximum duration in minutes
    
    Returns:
        str: Calendar events for the specified period
    """
    # Add more mock events with diverse properties
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
            },
            {
                "title": "Product Launch",
                "day": "Wednesday",
                "time": "10:00 AM",
                "category": "marketing",
                "duration": 120,
                "participants": 50,
                "location": "Main Auditorium",
                "priority": "high",
                "notes": "Q&A session included"
            },
            {
                "title": "Training Workshop",
                "day": "Thursday",
                "time": "2:00 PM",
                "category": "training",
                "duration": 180,
                "participants": 15,
                "location": "Training Room",
                "required_equipment": ["Laptops", "Projector"]
            }
        ]
    }

    # Enhanced filtering
    filtered_events = [
        event for event in structured_events["events"]
        if (not category or event["category"] == category) and
           (not location or event["location"] == location) and
           (not min_participants or event.get("participants", 0) >= min_participants) and
           (not max_duration or event.get("duration", 0) <= max_duration)
    ]

    # Enhanced output format
    output = f"Calendar Events ({start_date} to +{days} days):"
    for event in filtered_events:
        output += f"\n- {event['day']}: {event['title']}"
        output += f" ({event['time']}, {event.get('duration', 'N/A')} mins)"
        output += f" [category: {event['category']}]"
        output += f" [location: {event.get('location', 'N/A')}]"
        if "participants" in event:
            output += f" [participants: {event['participants']}]"
        if "priority" in event:
            output += f" [priority: {event['priority']}]"

    return output if filtered_events else f"No events found matching the criteria"