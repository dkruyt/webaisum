#!/usr/bin/env python3

import argparse
import requests
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain


def parse_arguments():
    parser = argparse.ArgumentParser(description='Summarize a web page using an AI model')
    parser.add_argument('url', type=str, help='The URL of the web page to summarize')
    parser.add_argument('--model', type=str, help='The AI model to use (default: llama3 or gpt-4-turbo)')
    parser.add_argument('--server', type=str, help='Base URL of the remote AI server to use')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode to print verbose output')
    parser.add_argument('--use-openai', action='store_true', help='Use OpenAI instead of Ollama for summarization')
    return parser.parse_args()


def load_web_page(url):
    headers = {"User-Agent": "WebAISum/1.0"}
    loader = WebBaseLoader(url, requests_kwargs={"headers": headers})
    return loader.load()


def initialize_llm(use_openai, model_name, server):
    if use_openai:
        return ChatOpenAI(model_name=model_name)
    else:
        if server:
            return Ollama(model=model_name, base_url=server)
        else:
            return Ollama(model=model_name)


def summarize_document(docs, llm, debug):
    chain = load_summarize_chain(llm, chain_type="stuff")
    result = chain.invoke(docs)

    if debug:
        print("Debug mode enabled. Printing result:")
        print(result)

    output_text = result['output_text']
    print("\n", output_text, "\n")


def main():
    args = parse_arguments()

    try:
        docs = load_web_page(args.url)

        model_name = args.model if args.model else ("gpt-4-turbo" if args.use_openai else "llama3")
        llm = initialize_llm(args.use_openai, model_name, args.server)

        summarize_document(docs, llm, args.debug)

    except requests.exceptions.ConnectionError as e:
        print("ERROR: Could not connect to the AI server. Please make sure the server is running and accessible.")
        print(f"Technical details: {e}")
    except Exception as e:
        print("ERROR: An unexpected error occurred while summarizing the document.")
        print(f"Technical details: {e}")


if __name__ == "__main__":
    main()
