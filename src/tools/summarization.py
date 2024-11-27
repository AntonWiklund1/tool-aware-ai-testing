def summary_tool(**kwargs) -> str:
    """
    Get a summary of the user's documents.

    Args:
        text (Optional[str]): The text to summarize. If not provided, a default  text is used.

    Returns:
        str:  summary of the text.
    """
    #  text if none is provided
    if not text:
        text = "This is a  document containing various topics and information."

    #  summary response
    mock_summary = """
- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology.
"""

    return mock_summary