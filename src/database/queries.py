from typing import List, Optional, Dict, Any
from datetime import datetime
from .connection import get_connection
from .models import Prompt, TestRun, Result

def get_all_prompts() -> List[Dict[str, Any]]:
    """Retrieve all prompts from the database."""
    conn, cur = get_connection()
    try:
        cur.execute("""
            SELECT id, prompt, prompt_category, correct_tool, tools_available 
            FROM prompts
            ORDER BY id;
        """)
        prompts = cur.fetchall()
        return [
            {
                "id": row[0],
                "prompt": row[1],
                "prompt_category": row[2],
                "correct_tool": row[3],
                "tools_available": row[4]
            }
            for row in prompts
        ]
    finally:
        cur.close()
        conn.close()

def get_all_test_runs() -> List[Dict[str, Any]]:
    """Retrieve all test runs from the database."""
    conn, cur = get_connection()
    try:
        cur.execute("""
            SELECT id, model_name, instructions, started_at, completed_at, configuration
            FROM test_runs
            ORDER BY started_at DESC;
        """)
        test_runs = cur.fetchall()
        return [
            {
                "id": row[0],
                "model_name": row[1],
                "instructions": row[2],
                "started_at": row[3],
                "completed_at": row[4],
                "configuration": row[5]
            }
            for row in test_runs
        ]
    finally:
        cur.close()
        conn.close()

def get_all_results() -> List[Dict[str, Any]]:
    """Retrieve all results from the database."""
    conn, cur = get_connection()
    try:
        cur.execute("""
            SELECT id, prompt_id, test_run_id, tool_calls, time_taken, 
                   success_rate, error_type, created_at
            FROM results
            ORDER BY created_at DESC;
        """)
        results = cur.fetchall()
        return [
            {
                "id": row[0],
                "prompt_id": row[1],
                "test_run_id": row[2],
                "tool_calls": row[3],
                "time_taken": row[4],
                "success_rate": row[5],
                "error_type": row[6],
                "created_at": row[7]
            }
            for row in results
        ]
    finally:
        cur.close()
        conn.close()

def get_results_with_details() -> List[Dict[str, Any]]:
    """Retrieve all results with related prompt and test run details."""
    conn, cur = get_connection()
    try:
        cur.execute("""
            SELECT r.id, r.time_taken, r.success_rate, r.error_type, 
                   r.created_at, r.tool_calls,
                   p.prompt, p.prompt_category, p.correct_tool,
                   t.model_name, t.instructions
            FROM results r
            JOIN prompts p ON r.prompt_id = p.id
            JOIN test_runs t ON r.test_run_id = t.id
            ORDER BY r.created_at DESC;
        """)
        results = cur.fetchall()
        return [
            {
                "id": row[0],
                "time_taken": row[1],
                "success_rate": row[2],
                "error_type": row[3],
                "created_at": row[4],
                "tool_calls": row[5],
                "prompt": row[6],
                "prompt_category": row[7],
                "correct_tool": row[8],
                "model_name": row[9],
                "instructions": row[10]
            }
            for row in results
        ]
    finally:
        cur.close()
        conn.close()

def get_success_rate_by_model() -> List[Dict[str, Any]]:
    """Get success rate statistics grouped by model."""
    conn, cur = get_connection()
    try:
        cur.execute("""
            SELECT t.model_name,
                   COUNT(*) as total_runs,
                   SUM(CASE WHEN r.success_rate THEN 1 ELSE 0 END) as successful_runs,
                   AVG(CASE WHEN r.success_rate THEN 1 ELSE 0 END)::float * 100 as success_rate,
                   AVG(r.time_taken) as avg_time_taken
            FROM results r
            JOIN test_runs t ON r.test_run_id = t.id
            GROUP BY t.model_name
            ORDER BY success_rate DESC;
        """)
        stats = cur.fetchall()
        return [
            {
                "model_name": row[0],
                "total_runs": row[1],
                "successful_runs": row[2],
                "success_rate_percentage": row[3],
                "avg_time_taken": row[4]
            }
            for row in stats
        ]
    finally:
        cur.close()
        conn.close()