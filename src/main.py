from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import sys
import os

os.environ["OPENAI_API_KEY"] = '******'

# os.system("corecli core:build");

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

# read error from output.log file
file1 = open(r"/./demo/error.log", "r+")
r = file1.readline()

#query openapi and get the suggestion for error
response = chatbot(r);

print("*** corecli build failed with some issues ***");
print("*** please try this suggestion to resolve build issue ***")

#print the response reveived from openapi
print(response);
