# setup.py
from setuptools import setup, find_packages

setup(
    name="CrowdStrike Project",
    version="0.1.0",
    description="Generate and score synthetic sales opportunities using MEDDPICC framework, via OpenAI",
    author="Mihai Mihalcea",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openai",
        "python-dotenv",
        "tqdm",
        # add any other runtime deps here
    ],
    entry_points={
        "console_scripts": [
            # After install, these commands become available
            "python main.py"
            "python main.py --skip-generate"
            "python main.py --skip-score"
        ],
    },
)
