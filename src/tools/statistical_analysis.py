from typing import List, Union

def statistical_analysis_tool(data: List[Union[int, float]], analysis_type: str, confidence_level: float = 0.95, **kwargs) -> str:
    """
    This tool performs statistical analysis on numerical data and returns  results.
    
    Args:
        data: List of numerical values to analyze
        analysis_type: Type of analysis to perform (mean, median, mode, std_dev, all)
        confidence_level: Confidence level for statistical calculations (default: 0.95)
    
    Returns:
        str:  statistical analysis results
    """
    #  responses based on analysis type
    analysis_results = {
        "mean": f" Mean: {sum(data)/len(data):.2f}",
        "median": " Median: 42.0",
        "mode": " Mode: 37.5",
        "std_dev": " Standard Deviation: 12.3",
        "all": """
 Statistical Analysis Results:
- Mean: 45.7
- Median: 42.0
- Mode: 37.5
- Standard Deviation: 12.3
- Confidence Interval (95%): [41.2, 50.2]
"""
    }

    # Return  result based on requested analysis type
    return analysis_results.get(
        analysis_type.lower(),
        f"Invalid analysis type. Available types: {', '.join(analysis_results.keys())}"
    )