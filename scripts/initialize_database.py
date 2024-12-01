import psycopg2
import tqdm

def main():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432,
    )

    cursor = conn.cursor()

    # Split the SQL commands and execute them individually
    sql_commands = [
        "DROP TABLE IF EXISTS results CASCADE;",
        "DROP TABLE IF EXISTS test_runs CASCADE;",
        "DROP TABLE IF EXISTS prompts CASCADE;",

        """
        CREATE TABLE prompts (
            id SERIAL PRIMARY KEY,
            prompt TEXT NOT NULL,
            prompt_category TEXT NOT NULL,
            correct_tools TEXT[] NOT NULL,
            tools_available TEXT[] NOT NULL
        );
        """,

        """
        CREATE TABLE test_runs (
            id SERIAL PRIMARY KEY,
            model_name TEXT NOT NULL,
            instructions TEXT NOT NULL,
            started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            configuration JSONB
        );
        """,

        """
        CREATE TABLE results (
            id SERIAL PRIMARY KEY,
            prompt_id INTEGER NOT NULL REFERENCES prompts(id),
            test_run_id INTEGER NOT NULL REFERENCES test_runs(id),
            tool_calls TEXT[] NOT NULL,
            time_taken FLOAT NOT NULL,
            success_rate BOOLEAN,
            error_type TEXT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (prompt_id) REFERENCES prompts(id),
            FOREIGN KEY (test_run_id) REFERENCES test_runs(id)
        );
        """
    ]

    for command in tqdm.tqdm(sql_commands):
        cursor.execute(command)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()