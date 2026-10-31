from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings


load_dotenv()

# urls = [
#     "https://lilianweng.github.io/posts/2023-06-23-agent/",
#     "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
#     "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
# ]

# docs = [WebBaseLoader(url).load() for url in urls]

# print(docs)

# doc_list = [item for doc in docs for item in doc]

# print(doc_list)

# text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#      chunk_size=250, chunk_overlap=0
# )


# doc_splits = text_splitter.split_documents(doc_list)

# ## to Store chunks into Chorma DB
# vector_store = Chroma.from_documents(
#     documents= doc_splits,
#     collection_name="c-rag",
#     embedding= OpenAIEmbeddings(),
#     persist_directory="./.chroma"
# )

## To Retrive data from chroma DB
vector_store = Chroma(
    collection_name="c-rag",
    embedding_function= OpenAIEmbeddings(),
    persist_directory="./.chroma"
)

retriever = vector_store.as_retriever()
