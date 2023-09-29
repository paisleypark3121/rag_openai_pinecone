import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from utilities import *

load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.7)

#simple_chat(llm)
arxiv_papers(llm)