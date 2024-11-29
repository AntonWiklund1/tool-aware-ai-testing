from typing import List, Union, Dict
from statistics import mean, median, mode, stdev
from src.utils.tracking import track_tool_usage

@track_tool_usage
def statistical_analysis_tool(data: List[Union[int, float, Dict]], analysis_type: str, confidence_level: float = 0.95, **kwargs) -> str:
    """
    This tool performs statistical analysis on numerical data and returns results.
    
    Args:
        data: List of numerical values or dictionaries with numerical values to analyze
        analysis_type: Type of analysis to perform (mean, median, mode, std_dev, all)
        confidence_level: Confidence level for statistical calculations (default: 0.95)
    
    Returns:
        str: Statistical analysis results
    """
    # Convert string input to list if needed
    if isinstance(data, str):
        try:
            # Remove brackets and split by comma
            data = [float(x.strip()) for x in data.strip('[]').split(',')]
        except ValueError:
            return "Error: Invalid data format. Please provide numerical values."

    # Ensure data is a list
    if not isinstance(data, list):
        return "Error: Data must be a list of numerical values"

    # Extract numerical data if input is a list of dictionaries
    numerical_data = []
    if data and isinstance(data[0], dict):
        for item in data:
            if "duration" in item:
                numerical_data.append(item["duration"])
            if "participants" in item:
                numerical_data.append(item["participants"])
    else:
        numerical_data = data

    if not numerical_data:
        return "No numerical data available for analysis"

    try:
        calculated_results = {
            "mean": round(mean(numerical_data), 2),
            "median": round(median(numerical_data), 2),
            "mode": round(mode(numerical_data), 2),
            "std_dev": round(stdev(numerical_data), 2) if len(numerical_data) > 1 else 0,
            "count": len(numerical_data),
            "sum": sum(numerical_data)
        }

        # Format output based on analysis type
        if analysis_type.lower() == "all":
            return f"""Statistical Analysis Results:
- Mean: {calculated_results['mean']}
- Median: {calculated_results['median']}
- Mode: {calculated_results['mode']}
- Standard Deviation: {calculated_results['std_dev']}
- Sample Size: {calculated_results['count']}
- Total: {calculated_results['sum']}"""
        
        elif analysis_type.lower() in calculated_results:
            return f"{analysis_type.title()}: {calculated_results[analysis_type.lower()]}"
        
        else:
            return f"Invalid analysis type. Available types: {', '.join(calculated_results.keys())}"

    except Exception as e:
        return f"Error performing statistical analysis: {str(e)}"