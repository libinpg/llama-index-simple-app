# llama-index-simple-app

Referenced [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local.html).

[中文文档](README_zh.md)

---

This repository provides a starter example for using LlamaIndex with a local model. LlamaIndex is a powerful tool for building search indexes and query engines using large language models. This example demonstrates how to load documents, set up a local embedding model and LLM, create an index, and perform queries.

Additionally, this repository includes instructions for using a custom embedding model. To get started:

1. Download the Hugging Face embedding model repository to the root directory of this project.
2. Modify the `main.py` file to update the path for the embedding model.
3. Run a backend service with the `llama2-chinese` model using Ollama.
4. After installing the required packages with `pip install -r requirements.txt`, you can directly run the application using `python main.py`.

This setup will allow you to use a custom Chinese language model for embedding and querying within the LlamaIndex application. The example provided in `main.py` will guide you through the process of setting up the index and performing queries against your indexed documents.

## Features

- Load documents from a specified directory.
- Set up a local embedding model and LLM using LlamaIndex.
- Create an index from the loaded documents.
- Perform queries and receive answers in a loop.

## Usage

1. Clone the repository to your local machine.
2. Follow the instructions above to set up the custom embedding model.
3. Place your documents in the `data` folder.
4. Run `main.py` to start the interactive query loop.
5. Enter your questions at the prompt, or type `exit` to terminate the program.

## Requirements

- Python 3.x
- Required packages (install using `pip install -r requirements.txt`)
- LlamaIndex and Ollama models (refer to the LlamaIndex documentation for setup instructions)
- A backend service running the `llama2-chinese` model for Ollama

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
