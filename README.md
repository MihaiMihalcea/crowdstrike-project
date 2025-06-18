CrowdStrike Project

This repository provides a complete end-to-end workflow to generate synthetic Salesforce-like opportunities and score them using OpenAI's GPT models, aligned with the MEDDPICC qualification framework.

📦 Installation

Ensure you have Python 3.8+ installed. Then:

# Clone the repository
git clone https://github.com/your-org/opportunity_pipeline.git
cd opportunity_pipeline

# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # on macOS/Linux
.venv\Scripts\Activate.ps1 # on Windows PowerShell

# Install package in editable mode
pip install -e .

🔧 Configuration

Create a .env file in the project root with:

OPENAI_API_KEY=sk-...your key...
OPENAI_MODEL=gpt-3.5-turbo  # or gpt-4o-mini, gpt-4, etc.

Ensure .env is listed in .gitignore.

📁 Project Structure

/your_project/
├── data_generator.py            # CLI: opportunities generator
├── prompts.py                   # Prompt templates and system messages
├── constants.py                 # company, stages, and lead source lists
├── opportunity_theme.py         # dataclass definition
├── opportunity_themes_data.py   # list of 50 themes
├── scorer.py                    # Scorer class and logic
├── main.py                      # CLI: opp-pipeline
├── openai_client.py             # OpenAI client wrapper
├── setup.py                     # Package installation config
├── .env                         # OpenAI API credentials
├── requirements.txt             # pinned dependencies
├── synthetic_opportunities.csv  # generated input data
└── scored_opportunities.csv     # scored output data

🚀 Usage

After installation, run one of the following commands:

python main.py                  # Generate data and score opportunities
python main.py --skip-generate  # Skip data generation, only score existing CSV
python main.py --skip-score     # Generate data only, skip scoring

🧩 Extensibility

Add new themes: Update opportunity_themes_data.py or point to a new data source.

Custom prompts: Edit or add templates in prompts.py.

Model variants: Change OPENAI_MODEL in your .env or pass --model if supported.

🧪 Testing & Development

Unit tests for Scorer, prompt parsing, and data generation can be added under a tests/ folder.

Use pip install -e . to pick up code changes automatically.