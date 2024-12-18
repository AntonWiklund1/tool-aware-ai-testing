# Setup

1. Install postgres (if not already installed):

```bash
brew install postgresql@17
```

2. Start docker (if not already running)

3. Run the following command to start the postgres database:

```bash
docker compose up -d
```

3. Activate the venv and install the dependencies:

```bash
source .venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

# Initialize the database

```bash
python -m scripts.initialize_database
```

# Insert prompts

```bash
python -m streamlit run src/apps/prompt_manager.py
```

# Run experiments

1. Set the environment variables

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

(or set the environment variables in the `.env` file)

2. Run the experiments

```bash
python -m scripts.run_experiments
```
