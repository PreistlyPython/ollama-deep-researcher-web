from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from .configuration import Configuration, SearchAPI
from .utils import web_mcp_search, deduplicate_and_format_sources

@dataclass
class State:
    """State of the assistant."""
    messages: List[Dict[str, Any]] = field(default_factory=list)
    configuration: Configuration = field(default_factory=Configuration)
    llm: Optional[ChatOllama] = None
    search_results: List[Dict[str, Any]] = field(default_factory=list)
    search_loop_count: int = 0
    perplexity_search_loop_count: int = 0

    def add_message(self, message: Dict[str, Any]) -> None:
        """Add a message to the conversation history."""
        self.messages.append(message)

    def get_messages(self) -> List[Dict[str, Any]]:
        """Get all messages in the conversation history."""
        return self.messages

    def get_last_message(self) -> Optional[Dict[str, Any]]:
        """Get the last message in the conversation history."""
        if self.messages:
            return self.messages[-1]
        return None

    def clear_messages(self) -> None:
        """Clear all messages in the conversation history."""
        self.messages = []

    def set_llm(self, llm: ChatOllama) -> None:
        """Set the LLM model."""
        self.llm = llm

    def get_llm(self) -> Optional[ChatOllama]:
        """Get the LLM model."""
        return self.llm

    def search_web(self, query: str, max_tokens_per_source: int = 1000) -> str:
        """Search the web using the configured search API."""
        if self.search_loop_count >= self.configuration.max_web_research_loops:
            return "Exceeded maximum number of web search loops."

        self.search_loop_count += 1

        if self.configuration.search_api == SearchAPI.WEB_MCP:
            search_results = web_mcp_search(query)
            self.search_results.append(search_results)
            return deduplicate_and_format_sources(search_results, max_tokens_per_source)
        else:
            raise ValueError(f"Unsupported search API: {self.configuration.search_api}")

    def get_search_results(self) -> List[Dict[str, Any]]:
        """Get all search results."""
        return self.search_results

    def clear_search_results(self) -> None:
        """Clear all search results."""
        self.search_results = []
        self.search_loop_count = 0
        self.perplexity_search_loop_count = 0
