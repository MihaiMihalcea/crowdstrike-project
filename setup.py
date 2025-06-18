# setup.py
from setuptools import setup, find_packages

setup(
    name="opportunity_pipeline",
    version="0.1.0",
    description="Generate and score synthetic sales opportunities via MEDDPICC + OpenAI",
    author="Your Name",
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
            "opp-generate = data_generator:main",
            "opp-score    = scorer:main",
            "opp-pipeline = main:main",
        ],
    },
)
