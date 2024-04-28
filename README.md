Here's the updated README.md with Unicode icons:

```markdown
# WebAISum 🌐🤖📝

WebAISum is a Python script that allows you to summarize web pages using AI models. It supports both local models like Ollama and remote services like OpenAI.

## Features ✨

- Summarize web pages using AI models 🌐🤖
- Support for local models (Ollama) and remote services (OpenAI) 🏠☁️
- Customizable model selection 🔧
- Debug mode for verbose output 🐛

## Requirements 📋

- Python 3.6 or higher 🐍
- `requests` library 📦
- `langchain_community` library 📚
- `langchain_openai` library 🔑

## Installation 💻

1. Clone the repository:

```bash
git clone https://github.com/dkruyt/webaisum.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage 🚀

To summarize a web page, run the `webaisum.py` script with the desired URL:

```bash
python webaisum.py https://example.com
```

### Optional Arguments 🛠️

- `--model`: Specify the AI model to use (default: llama3 for Ollama or gpt-4-turbo for OpenAI)
- `--server`: Specify the base URL of the remote AI server to use (for Ollama)
- `--debug`: Enable debug mode to print verbose output
- `--use-openai`: Use OpenAI instead of Ollama for summarization

### Examples 💡

Summarize a web page using the default Ollama model:

```bash
python webaisum.py https://example.com
```

Summarize a web page using a specific Ollama model and remote server:

```bash
python webaisum.py https://example.com --model llama2 --server http://ollama-server.com
```

Summarize a web page using OpenAI:

```bash
python webaisum.py https://example.com --use-openai
```

Summarize a web page using OpenAI with a specific model:

```bash
python webaisum.py https://example.com --use-openai --model gpt-3.5-turbo-16k
```

## Contributing 🤝

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE).
```
