This project is based on https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/rag-chatbot.ipynb

It is necessary to have an account on OpenAI and Pinecone in order to get the KEYS needed for the project that have to be included in an .env file; so please create an .env file and insert keys:
OPENAI_API_KEY=**USE YOUR KEY**
PINECONE_API_KEY=**USE YOUR KEY**
PINECONE_ENVIRONMENT=**USE YOUR ENV**

There are 2 main functions that can be called from main.py:

- simple_chat(llm)
- arxiv_papers(llm)

The llm model injected is the ChatOpenAI(model='gpt-3.5-turbo',temperature=0.7)

The simple_chat function uses a Q&A model in which previous messaes are "appended" but no information is given about the context, therefore we could face allucinations

The arxiv_papers function instead relies on a specific dataset "jamescalam/llama-2-arxiv-papers-chunked" that is cached locally; a pinecone index is created based (once created it is simply retrieved). For each query, an augmented prompt is created based on most "similar" chunks retrieved and the query itself, everything embedded in a specific template

Start from main: python main.py
