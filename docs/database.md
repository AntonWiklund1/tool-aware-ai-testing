# Database Structure

This document outlines the database structure used in the AI Agent Tool Selection project. The database is implemented using PostgreSQL.

## Tables

### 1. prompts

Stores the test prompts and their associated metadata.

| Column          | Type   | Description                                    |
| --------------- | ------ | ---------------------------------------------- |
| id              | SERIAL | Primary key                                    |
| prompt          | TEXT   | The actual prompt text                         |
| prompt_category | TEXT   | Category of the prompt (e.g., weather, coding) |
| correct_tool    | TEXT   | The expected correct tool for this prompt      |
| tools_available | TEXT[] | Array of tools available for this prompt       |

### 2. test_runs

Tracks individual test execution sessions.

| Column        | Type      | Description                                  |
| ------------- | --------- | -------------------------------------------- |
| id            | SERIAL    | Primary key                                  |
| model_name    | TEXT      | Name of the AI model used                    |
| instructions  | TEXT      | Instructions for the AI agent                |
| started_at    | TIMESTAMP | Start time of the test run                   |
| completed_at  | TIMESTAMP | End time of the test run (nullable)          |
| configuration | JSONB     | JSON blob for flexible configuration storage |

### 3. results

Stores the results of each prompt execution within a test run.

| Column       | Type      | Description                           |
| ------------ | --------- | ------------------------------------- |
| id           | SERIAL    | Primary key                           |
| prompt_id    | INTEGER   | Foreign key referencing prompts.id    |
| test_run_id  | INTEGER   | Foreign key referencing test_runs.id  |
| tool_calls   | TEXT[]    | Array of tools called by the AI       |
| time_taken   | FLOAT     | Execution time for this prompt        |
| success_rate | BOOLEAN   | Whether the correct tool was selected |
| error_type   | TEXT      | Description of error, if any          |
| created_at   | TIMESTAMP | Timestamp of result creation          |

## Relationships

- `results.prompt_id` references `prompts.id`
- `results.test_run_id` references `test_runs.id`

## Usage

1. First, insert prompts into the `prompts` table.
2. Create a new entry in `test_runs` when starting a new test session.
3. For each prompt execution, insert a row into the `results` table, linking it to the corresponding prompt and test run.

This structure allows for flexible analysis of AI performance across different prompts, models, and test configurations.
