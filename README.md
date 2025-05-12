<!-- ─── BADGES ─────────────────────────────────────────────────────────── -->
<!-- Row 1 – package + CI/CD -->
[![PyPI Package Version](https://img.shields.io/pypi/v/langchain-litellm?label=PyPI%20package&style=flat)](https://pypi.org/project/langchain-litellm/)
[![PyPI Downloads](https://static.pepy.tech/badge/langchain-litellm)](https://pepy.tech/projects/langchain-litellm)
[![Release status](https://github.com/Akshay-Dongare/langchain-litellm/actions/workflows/release-publish-pypi.yml/badge.svg?branch=main&event=release)](https://github.com/Akshay-Dongare/langchain-litellm/actions/workflows/release-publish-pypi.yml)<br>

<!-- Row 2 – meta -->
[![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
![Platform](https://img.shields.io/badge/Platform-Linux%2C%20Windows%2C%20macOS-blue)
![Github Issues](https://img.shields.io/github/issues-closed/Akshay-Dongare/langchain-litellm)
![Github Issues](https://img.shields.io/github/issues/Akshay-Dongare/langchain-litellm)
![Github Pull Requests](https://img.shields.io/github/issues-pr/Akshay-Dongare/langchain-litellm)
![Github Pull Requests](https://img.shields.io/github/issues-pr-closed/Akshay-Dongare/langchain-litellm)
<!-- ─────────────────────────────────────────────────────────────────────── -->


# [langchain-litellm](https://pypi.org/project/langchain-litellm/)

This package contains the [LangChain](https://github.com/langchain-ai/langchain) integration with LiteLLM. [LiteLLM](https://github.com/BerriAI/litellm) is a library that simplifies calling Anthropic, Azure, Huggingface, Replicate, etc.

## Installation and setup

```bash
pip install langchain-litellm
```

## Chat Models
```python
from langchain_litellm import ChatLiteLLM
```

```python
from langchain_litellm import ChatLiteLLMRouter
```
See a [usage example](https://github.com/Akshay-Dongare/langchain-litellm/blob/main/docs/litellm.ipynb)
