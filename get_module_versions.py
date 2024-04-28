import importlib.metadata

modules = [
    'langchain',
    'langchain-community',
    'langchain_openai',
    'requests',
    'bs4'
]

with open('requirements.txt', 'w') as f:
    for module in modules:
        try:
            version = importlib.metadata.version(module)
            f.write(f"{module}=={version}\n")
        except importlib.metadata.PackageNotFoundError:
            print(f"Warning: Module '{module}' not found.")
