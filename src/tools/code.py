import subprocess
import tempfile
import os
import sys
from datetime import datetime
from src.utils.tracking import track_tool_usage

@track_tool_usage
def code_tool(code: str, language: str = "python", timeout: int = 30, **kwargs) -> str:
    """
    Executes code snippets in python or typescript.

    Args:
        code: The code to execute
        language: Programming language of the code (default: python)
        timeout: Maximum execution time in seconds (default: 30)
    
    Returns:
        str: Execution results
    """
    def get_version_info(lang: str) -> dict:
        versions = {
            "python": ["python", "--version"],
            "node": ["node", "--version"],
            "typescript": ["tsc", "--version"]
        }
        try:
            cmd = versions.get(lang)
            if cmd:
                result = subprocess.run(cmd, capture_output=True, text=True)
                return result.stdout.strip()
        except:
            return "Version unknown"

    def format_success_output(output: str, execution_time: float, lang: str) -> str:
        return f"""
{lang.title()} Execution Result:
> Output: {output}
> Execution time: {execution_time:.3f}s
> {lang.title()} version: {get_version_info(lang)}
"""

    def format_error_output(error: str, lang: str) -> str:
        return f"""
{lang.title()} Execution Error:
> Error: {error}
"""

    def execute_python(code: str, timeout: int) -> tuple[str, float]:
        start_time = datetime.now()
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name

            # Execute in a subprocess with timeout
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            if result.stderr:
                return format_error_output(result.stderr, "python"), execution_time
            return result.stdout, execution_time
            
        except subprocess.TimeoutExpired:
            return "Execution timed out", timeout
        except Exception as e:
            return str(e), 0
        finally:
            # Cleanup
            if 'temp_file' in locals():
                os.unlink(temp_file)

    def execute_typescript(code: str, timeout: int) -> tuple[str, float]:
        start_time = datetime.now()
        try:
            # Create temporary TypeScript file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.ts', delete=False) as f:
                f.write(code)
                temp_file = f.name

            # Compile TypeScript
            compile_result = subprocess.run(
                ['tsc', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            if compile_result.stderr:
                return format_error_output(compile_result.stderr, "typescript"), 0

            # Execute compiled JavaScript
            js_file = temp_file.replace('.ts', '.js')
            result = subprocess.run(
                ['node', js_file],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            if result.stderr:
                return format_error_output(result.stderr, "typescript"), execution_time
            return result.stdout, execution_time

        except subprocess.TimeoutExpired:
            return "Execution timed out", timeout
        except Exception as e:
            return str(e), 0
        finally:
            # Cleanup
            if 'temp_file' in locals():
                os.unlink(temp_file)
                js_file = temp_file.replace('.ts', '.js')
                if os.path.exists(js_file):
                    os.unlink(js_file)

    # Execute code based on language
    language = language.lower()
    if language == "python":
        output, execution_time = execute_python(code, timeout)
    elif language == "typescript":
        output, execution_time = execute_typescript(code, timeout)
    else:
        return f"Unsupported language: {language}. Supported languages: python, typescript"

    if "Error:" in output:
        return output
    return format_success_output(output, execution_time, language)