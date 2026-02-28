# AI Agent Project

This project is me trying to build an AI agent from scratch using GitHub's playground models and Azure AI services. The agent is designed to interact with users, process their inputs, and provide intelligent responses using advanced AI models. This is a baseline but thinking on adding access to integrated tools later on.

## Features
- Utilization of Azure AI services for chat completions.
- Secure handling of API keys and endpoints using environment variables.

## Tools used
- Python 3.7+
- Dependencies listed in `requirements.txt`

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI-Agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following environment variables:
   ```env
   GITHUB_TOKEN=your_github_token_here
   AZURE_ENDPOINT=https://models.github.ai/inference
   ```

5. Run the project:
   ```bash
   python3 main.py
   ```

## Usage
- The AI agent interacts with users by processing their inputs and generating intelligent responses using GitHub's playground models.
- The `main.py` file contains the core logic for the AI agent.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License.