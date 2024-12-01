from src.utils.tracking import track_tool_usage

@track_tool_usage
def summary_tool(**kwargs) -> str:
    """
    Get a summary of the user's uploaded documents to the database. So no need to provide a text argument.

    Returns:
        str:  summary of the text.
    """
    #  summary response
    mock_summary = """
- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology.
"""

    return mock_summary