def summary_tool(**kwargs) -> str:
    """
    Get a summary of the user's documents.

    Args:
        text (Optional[str]): The text to summarize. If not provided, a default  text is used.

    Returns:
        str:  summary of the text.
    """
    print("running summary_tool")

    #  summary response
    mock_summary = """
- The document discusses various topics.
- Key points include the importance of data analysis and effective communication.
- Concludes with future trends in technology.
"""

    return mock_summary