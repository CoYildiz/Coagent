# AI Agent
This project was created for educational purposes only.

The agent can read, modify, and execute files inside the configured working directory. Although basic safety mechanisms are implemented, this project should **not be used on large or important codebases** or trusted with sensitive files.

This project explores how modern AI coding assistants work internally by allowing an LLM to interact with a local codebase through controlled tools.

The agent does not directly execute actions by itself. Instead, the LLM decides which tool should be used, the agent executes the function, returns the result back to the model, and continues the reasoning process until a final response is generated.

## Features

### File System Interaction
The agent can inspect files and directories inside a restricted working directory.

Supported operations:
- List files and directories
- Read file contents
- Create and modify files
- Execute Python files

## Available Tools
| Tool | Description |
|------|-------------|
| `get_files_info` | Lists files and directories with metadata |
| `get_file_content` | Reads file contents with size limits |
| `write_file` | Creates or overwrites files |
| `run_python_file` | Executes Python files and captures output |

## How It Works
The agent follows a tool-calling architecture:
```
User
 |
 v
LLM
 |
 v
Tool Selection
 |
 v
Python Function Execution
 |
 v
Tool Result
 |
 v
LLM
 |
 v
Final Response
```

The LLM only decides which action should be performed.

The actual execution is handled by Python functions controlled by the agent.

## Example Usage
Run the agent:
```bash
uv run main.py "what files are in the project?"
```

Example prompts:
```
list the files in the calculator directory
```

```
read the contents of main.py
```

```
create a new file called test.py
```

```
run tests.py
```

Verbose mode:
```bash
uv run main.py "run tests.py" --verbose
```

Example output:
```
- Calling function: run_python_file

Final response:
All tests completed successfully.
```

## Installation
Clone the repository:
```bash
git clone <repository-url>
cd AIAgent
```

Install dependencies:
```bash
uv sync
```

Create a `.env` file:
```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the agent:
```bash
uv run main.py "your prompt"
```

## Security
This project is created for educational purposes.
The agent has the ability to:
- Read files
- Write files
- Execute Python code

To reduce risks, the following protections are implemented:
- Restricted working directory
- Path validation
- File type checking
- Execution timeout
- Output capturing

However, this is not a production-ready autonomous coding agent.

## Technologies
- Python
- OpenAI SDK
- OpenRouter API
- Function Calling
- JSON Schema Tools
- uv Package Manager

## Learning Goals
This project focuses on understanding:

- How LLM agents work
- Function calling architecture
- Tool execution pipelines
- Agent loops
- Prompt engineering
- AI coding assistant design
