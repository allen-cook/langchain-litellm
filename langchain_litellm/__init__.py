from importlib import metadata

from langchain_litellm.chat_models import ChatLitellm
from langchain_litellm.document_loaders import LitellmLoader
from langchain_litellm.embeddings import LitellmEmbeddings
from langchain_litellm.retrievers import LitellmRetriever
from langchain_litellm.toolkits import LitellmToolkit
from langchain_litellm.tools import LitellmTool
from langchain_litellm.vectorstores import LitellmVectorStore

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatLitellm",
    "LitellmVectorStore",
    "LitellmEmbeddings",
    "LitellmLoader",
    "LitellmRetriever",
    "LitellmToolkit",
    "LitellmTool",
    "__version__",
]
