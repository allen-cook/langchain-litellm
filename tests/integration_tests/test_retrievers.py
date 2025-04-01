from typing import Type

from langchain_litellm.retrievers import LitellmRetriever
from langchain_tests.integration_tests import (
    RetrieversIntegrationTests,
)


class TestLitellmRetriever(RetrieversIntegrationTests):
    @property
    def retriever_constructor(self) -> Type[LitellmRetriever]:
        """Get an empty vectorstore for unit tests."""
        return LitellmRetriever

    @property
    def retriever_constructor_params(self) -> dict:
        return {"k": 2}

    @property
    def retriever_query_example(self) -> str:
        """
        Returns a str representing the "query" of an example retriever call.
        """
        return "example query"
