# langchain-litellm

This package contains the LangChain integration with Litellm

## Installation

```bash
pip install -U langchain-litellm
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatLitellm` class exposes chat models from Litellm.

```python
from langchain_litellm import ChatLitellm

llm = ChatLitellm()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`LitellmEmbeddings` class exposes embeddings from Litellm.

```python
from langchain_litellm import LitellmEmbeddings

embeddings = LitellmEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```

## LLMs
`LitellmLLM` class exposes LLMs from Litellm.

```python
from langchain_litellm import LitellmLLM

llm = LitellmLLM()
llm.invoke("The meaning of life is")
```
