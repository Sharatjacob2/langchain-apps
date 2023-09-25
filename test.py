from langchain import HuggingFaceHub
from getpass import getpass
 
HUGGINGFACEHUB_API_TOKEN = "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"
 
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
 
repo_id = "gpt2"
 
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.9, "max_length":256})

# from langchain import PromptTemplate, LLMChain
prompt = "The cat sat on the"
# prompt_template = PromptTemplate.from_template(
#     "Tell me a {adjective} joke about {content}."
# )
# prompt_template.format(adjective="funny", content="chickens")
# llm_chain = LLMChain(prompt=prompt_template, llm=llm, verbose= True)
# prompt = prompt_template.format(adjective="funny", content="chickens")
print(llm(prompt))
print("All done, guys!")