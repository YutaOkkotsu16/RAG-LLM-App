# RAG-LLM-App
# Retrieval Augmented Generation (RAG)

## Overview
Retrieval Augmented Generation (RAG) is a powerful technique that combines information retrieval with text generation to enhance the quality of generated responses. This project implements a RAG system using OpenAI's API for natural language processing tasks.

## Theory
RAG leverages a pre-built index of documents to retrieve relevant information based on a query. This retrieved information is then used to augment the text generation process, leading to more informative and contextually relevant responses.

## Setup
1. Install the required dependencies by running `pip install llama-index`.
2. Set up your OpenAI API key in a `.env` file in the project directory.

## Usage
1. Run the `rag_system.py` script to interact with the RAG system.
2. The system retrieves relevant information using a vector index and generates responses based on the retrieved data.

## Files
- `rag_system.py`: Contains the implementation of the RAG system.
- `data/`: Directory containing the data used for retrieval and generation.

Feel free to explore the code, experiment with different retrieval strategies, and customize the system for your specific use case.
