#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="llm",
    version="0.1.0",
    description="Foundation Language Model with PEER and MLA",
    author="LLM Team",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.12.0",
        "numpy>=1.20.0",
        "transformers>=4.20.0",
        "datasets>=2.0.0",
        "wandb>=0.13.0",
        "accelerate>=0.10.0",
        "safetensors>=0.2.0",
        "PyYAML>=6.0", # Provides the 'yaml' module
        "tqdm>=4.62.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.12.0",
        "pandas>=1.3.0",
        "tabulate>=0.8.0",
        "flash-attn>=2.0.0; platform_system=='Linux'", # flash-attn is often Linux-only
        "torchao>=0.10.0", # Use torchao for FP8 and other optimizations
        "pynvml>=11.0.0",  # For GPU monitoring
        "tiktoken>=0.7.0", # Added tiktoken dependency
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pandas>=1.3.0",    # Added for analysis
            "seaborn>=0.12.0",  # Added for analysis
            "black",
            "isort",
            "flake8",
            "mypy",
        ],
        "evals": [
            "evals",  # OpenAI's evals library
        ],
    },
    entry_points={
        "console_scripts": [
            "llm-train=scripts.train:main",
            "llm-eval=scripts.run_evaluation:main",
        ],
    },
)
