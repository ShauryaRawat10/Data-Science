## RAG (Retrieval Augmentation Generation)
- Retrieval means retrieving chunks, Augmentation means augmenting retrieved chunks to user query and generation means generating highly accurate answer
- Problem of taking entire document:
  - Hard token limit
  - Neddle in the Haystack
  - Cost
  - Latency
- Take entrire document -> Split to smaller chunks -> chunks -> find most relevant chunk


#### Needle in the Haystack (NIAH)
- difficulty an AI model has in retrieving or extracting a specific, isolated fact (the needle) when it is buried deep within a massive volume of irrelevant or less important information

## Introduction to RAG Implementation

#### Introduction to Vector Databases
- Embeddings
- Vector Stores
- RetrievalQA Chain
- Langchain document loaders
- Langchain text splitters

#### Langchain Document Loaders
- Document is anything that holds text (image, pdf, etc all are document)
- Document loader is **abstraction** to help us load the data

#### Langchain Text Splitters
- Big document to chunks (semantically related)
- Text Splitter helps us in splitting text to chunks
- many methods and strategies

-> RAG -> User Query + Context = Output

![RAG Implemetation](https://github.com/ShauryaRawat10/Data-Science/blob/99c224311d5add9f41c0c9fdeadf55bbd0fa5962/Generative%20AI/Langchain%26Langgraph/storage/RAG.png)


#### Boilerplate setup
```
1. Clone Repo:
   -> git clone https://github.com/emarco177/langchain-course.git
2. Change Directory
   -> cd langchain-course
3. Switch to correct branch and to initial commit in it
   -> git checkout -b project/rag-gist 598dee435cb61dbb9c655644b0e05dd4cdaf833c
```

Terminal setup
```
uv lock (creates new lock uv.lock file with all the dependencies that we need)
uv sync (install all dependencies to .venv file by creating that .venv directory)


```

#### Pinecone setup steps:
- Create Index -> medium-blogs-embeddings-index
- Config: text-embedding-3-small
  - Vector Type: Dense
  - Max Input: 8191 tokens
  - Dimension: 1536
  - Metric: cosine
- Capacity mode: Serverless
- Cloud provider: AWS
- Region: us-east-1
- create index

***
## Exercise 1

### Load -> Split -> Embed -> Store

```
OPENAI_API_KEY=sk-proj-4FC4Yx
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_0e14
LANGSMITH_PROJECT="RAG Gist"
INDEX_NAME=medium-blogs-embeddings-index
PINECONE_API_KEY=pcsk_2ifB
```

```
import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import TextLoader 
from langchain_community.document_loaders.base_o365 import CHUNK_SIZE
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv(find_dotenv())

if __name__ == '__main__':
    print("Ingesting...")

    file_path = r"C:\Users\shaur\OneDrive\Desktop\langchain-course\mediumblog1.txt"
    
    loader = TextLoader(file_path, encoding='utf-8')
    document = loader.load()

    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")
    
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    
    print("ingesting...")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])

    print("finish!!")
```
























