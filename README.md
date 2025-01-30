# Ollama Deep Researcher with Web-MCP

A fork of the Ollama Deep Researcher project that integrates with the web-mcp server for enhanced web search capabilities.

## Overview

This project extends the original Ollama Deep Researcher by replacing the default search methods with the web-mcp server. This integration provides:

- More robust web scraping capabilities
- Improved content extraction
- Better handling of dynamic websites

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PreistlyPython/ollama-deep-researcher-web.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the web-mcp server is running and configured in your MCP settings.

## Usage

1. Import the necessary components:
   ```python
   from assistant import State, Configuration, SearchAPI
   ```

2. Configure the assistant to use the web-mcp search:
   ```python
   config = Configuration(search_api=SearchAPI.WEB_MCP)
   state = State(configuration=config)
   ```

3. Use the search functionality:
   ```python
   results = state.search_web("Your search query")
   print(results)
   ```

## Features

- Web-MCP Integration: Uses the web-mcp server for improved web scraping
- Knowledge Graph: Builds a graph of related information
- State Management: Keeps track of conversation and search history

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
