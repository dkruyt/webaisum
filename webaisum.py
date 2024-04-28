#!/usr/bin/env python3

import argparse
import requests
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

# Create an argument parser
parser = argparse.ArgumentParser(description='Summarize a web page using an AI model')
parser.add_argument('url', type=str, help='The URL of the web page to summarize')
parser.add_argument('--model', type=str, help='The AI model to use (default: llama3 or gpt-4-turbo)')
parser.add_argument('--server', type=str, help='Base URL of the remote AI server to use')
parser.add_argument('--debug', action='store_true', help='Enable debug mode to print verbose output')
parser.add_argument('--use-openai', action='store_true', help='Use OpenAI instead of Ollama for summarization')

# Parse the command line arguments
args = parser.parse_args()

# Load the web page
headers = {"User-Agent": "WebAISumm/1.0"}
loader = WebBaseLoader(args.url, requests_kwargs={"headers": headers})
docs = loader.load()

try:
    # Choose the AI model based on the flags
    if args.use_openai:
        # Set a default model for OpenAI and allow override if --model is specified
        model_name = args.model if args.model else "gpt-4-turbo"
        # Initialize OpenAI with the selected model
        llm = ChatOpenAI(model_name=model_name)
    else:
        # Set a default model for Ollama and allow override if --model is specified
        model_name = args.model if args.model else "llama3"
        # Initialize Ollama with the selected model and server if provided
        if args.server:
            llm = Ollama(model=model_name, base_url=args.server)
        else:
            llm = Ollama(model=model_name)
            
    chain = load_summarize_chain(llm, chain_type="stuff")

    # Run the summarization chain on the loaded documents
    result = chain.invoke(docs)

    # If debug is enabled, print the result
    if args.debug:
        print("Debug mode enabled. Printing result:")
        print(result)

    # Extract the output_text and print it nicely formatted
    output_text = result['output_text']
    print("\n", output_text, "\n")

except requests.exceptions.ConnectionError as e:
    print("ERROR: Could not connect to the AI server. Please make sure the server is running and accessible.")
    print(f"Technical details: {e}")
except Exception as e:
    # This block catches other exceptions that may occur
    print("ERROR: An unexpected error occurred while summarizing the document.")
    print(f"Technical details: {e}")
