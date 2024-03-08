from llama_index.core import SimpleDirectoryReader
import os

sources= []
for dir in os.listdir("Docs"):
    print(dir)
    sdr = SimpleDirectoryReader(f"Docs/{dir}").load_data()
    sources.append(sdr)

print(sources)