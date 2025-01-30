from enum import Enum
from typing import Optional
from dataclasses import dataclass
from langchain_core.runnables import RunnableConfig

class SearchAPI(str, Enum):
    TAVILY = "tavily"
    PERPLEXITY = "perplexity"
    WEB_MCP = "web-mcp"  # Added web-mcp as a new search option

@dataclass
class Configuration:
    """Configuration for the assistant."""
    local_llm: str = "mistral"  # Default LLM model
    search_api: SearchAPI = SearchAPI.WEB_MCP  # Changed default to web-mcp
    max_web_research_loops: int = 3  # Maximum number of research iterations

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None) -> "Configuration":
        """Create a Configuration from a RunnableConfig."""
        if not config:
            return cls()
        
        config_dict = config.get("configurable", {})
        
        # Get local_llm
        local_llm = config_dict.get("local_llm", cls.local_llm)
        
        # Get search_api
        search_api_value = config_dict.get("search_api", cls.search_api)
        # Handle both string and enum cases
        if isinstance(search_api_value, str):
            search_api = search_api_value
        else:
            search_api = search_api_value.value
            
        # Get max_web_research_loops
        max_web_research_loops = config_dict.get(
            "max_web_research_loops", 
            cls.max_web_research_loops
        )
        
        return cls(
            local_llm=local_llm,
            search_api=search_api,
            max_web_research_loops=max_web_research_loops
        )