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
.env file

OPENAI_API_KEY=sk-proj-4FC4Yx
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=lsv2_pt_0e14
LANGSMITH_PROJECT="RAG Gist"
INDEX_NAME=medium-blogs-embeddings-index
PINECONE_API_KEY=pcsk_2ifB
```

```
ingestion.py

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

-> Langchain Document Loaders: https://docs.langchain.com/oss/javascript/integrations/document_loaders

-> Langchain document loader code: find in github langchain document loaders implementation (whatsapp, slack, twitter, youtube, etc)

### Without RAG
```
import os 

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

print("Initializing components...")

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-5.2")

vectorstore = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"], embedding=embeddings
)

# Top 3 documents from pinecone
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the question based only on following context:
    {context}
    Question: {question}
    Provide a detailed answer:
    """
)

def format_docs(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


if __name__ == "__main__":
    print("Retrieving...")

    query = "what is pinecone in machine learning?"

    # =============================================
    # option 0: raw invocation without RAG
    # =============================================
    print("\n"+"=" * 70)
    print("IMEPLEMENTATION 0: Raw LLM Invocation (No RAG)")
    print("\n"+"=" * 70)
    result_raw = llm.invoke( [HumanMessage(content=query)] )
    print("\nAnswer:")
    print(result_raw.content)

```

### With RAG (No Langchain expression language)
```
import os 

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

print("Initializing components...")

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-5.2")

vectorstore = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"], embedding=embeddings
)

# Top 3 documents from pinecone
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the question based only on following context:
    {context}
    Question: {question}
    Provide a detailed answer:
    """
)

def format_docs(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)

# =====================================================================================
# IMPLEMENTATION 1: Without LCEL (Simple Function based approach)
# =====================================================================================
def retrieval_chain_without_lcel(query:str):
    # Without Langchain expression language: retrieve string and return response of llm 
    """
    Simple retrieval chain without LCEL.
    Manually retrieves documents, formats them and generates a response

    Limitations:
    - Manual step-by-step execution
    - No built-in streaming support
    - No async support without additional code
    - Harder to compose with other chains
    - More variance and error prone
    """
    # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: format_docs(docs)
    context = format_docs(docs)

    # Step 3: Format the prompt with context and question
    messages = prompt_template.format_messages(context=context, question=query)

    # Step 4: Invoke LLM with the formatted messages
    response = llm.invoke(messages)

    # Step 5: Return the content
    return response.content



if __name__ == "__main__":
    print("Retrieving...")

    query = "what is pinecone in machine learning?"

    # =============================================
    # option 0: raw invocation without RAG
    # =============================================
    print("\n"+"=" * 70)
    print("IMEPLEMENTATION 0: Raw LLM Invocation (No RAG)")
    print("\n"+"=" * 70)
    result_raw = llm.invoke( [HumanMessage(content=query)] )
    print("\nAnswer:")
    print(result_raw.content)

    # =============================================
    # option 1: use implementation without lcel (Disadv: Traces and debugging are separate for each call)
    # =============================================
    print('\n'+"="*70)
    print("Implementation 1: Without LCEL")
    print('\n'+"="*70)
    result_without_lcel = retrieval_chain_without_lcel(query)
    print("Answer:")
    print(result_without_lcel)


```

### With RAG - Langchain expression language
- Same answer as without LCEL, but is concise and built in traces
```
import os 

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from operator import itemgetter

load_dotenv()

print("Initializing components...")

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-5.2")

vectorstore = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"], embedding=embeddings
)

# Top 3 documents from pinecone
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the question based only on following context:
    {context}
    Question: {question}
    Provide a detailed answer:
    """
)

def format_docs(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)

# =====================================================================================
# IMPLEMENTATION 1: Without LCEL (Simple Function based approach)
# =====================================================================================
def retrieval_chain_without_lcel(query:str):
    # Without Langchain expression language: retrieve string and return response of llm 
    """
    Simple retrieval chain without LCEL.
    Manually retrieves documents, formats them and generates a response

    Limitations:
    - Manual step-by-step execution
    - No built-in streaming support
    - No async support without additional code
    - Harder to compose with other chains
    - More variance and error prone
    """
    # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: format_docs(docs)
    context = format_docs(docs)

    # Step 3: Format the prompt with context and question
    messages = prompt_template.format_messages(context=context, question=query)

    # Step 4: Invoke LLM with the formatted messages
    response = llm.invoke(messages)

    # Step 5: Return the content
    return response.content


# =====================================================================================
# IMPLEMENTATION 2: With LCEL (Langchain Expression Language) - Better approch
# =====================================================================================
def create_retrieval_chain_with_lcel():
    """
    Function type of Runnable
    Create a retrieval chain using (Langchain Expression Laguage)
    Returns a chain that can be invoked with {"question": "..."}

    Advantages over non-LCEL approach:
    - Declarative and composable: Easy to chain operations with pipe operator (|)
    - Built-in streaming: chain.stream() works out of the box
    - Built-in async: chain.ainvoke() and chain.astream() available
    - Batch processing: chain.batch() for multiple inputs
    - Type safety: Bettere integration with Langchain's type system
    - Less code: More concise and readable
    - Reusable: Chain can be saved, shared, and composed with other chain
    - Better debugging: Langchain provides better observablity tools

    StrOutputParser to access .content key of output
    retriever | format_docs | prompt_template => Langchain converts format_docs function into Runnable lambda underthehood even though its not runnable fun
    """
    
    retrieval_chain = (
        RunnablePassthrough.assign(
            context=itemgetter("question") | retriever | format_docs
        )
        | prompt_template
        | llm 
        | StrOutputParser()
    )
    return retrieval_chain




if __name__ == "__main__":
    print("Retrieving...")

    query = "what is pinecone in machine learning?"

    # =============================================
    # option 0: raw invocation without RAG
    # =============================================
    print("\n"+"=" * 70)
    print("IMEPLEMENTATION 0: Raw LLM Invocation (No RAG)")
    print("\n"+"=" * 70)
    result_raw = llm.invoke( [HumanMessage(content=query)] )
    print("\nAnswer:")
    print(result_raw.content)

    # =============================================
    # option 1: use implementation without lcel (Disadv: Traces and debugging are separate for each call)
    # =============================================
    print('\n'+"="*70)
    print("Implementation 1: Without LCEL")
    print('\n'+"="*70)
    result_without_lcel = retrieval_chain_without_lcel(query)
    print("Answer:")
    print(result_without_lcel)

    # =============================================
    # option 2: use implementation with lcel (Better approach)
    # =============================================
    print('\n'+"="*70)
    print("Implementation 2: With LCEL - Better Approach")
    print('\n'+"="*70)
    print("LCEL is better: Concise, declarative, Built-in Streaming, Built-in async, Easy to compose other chain, better production use")
    print('\n'+"="*70)
    
    chain_with_lcel = create_retrieval_chain_with_lcel()
    result_with_lcel = chain_with_lcel.invoke({"question": query})
    print("\nAnswer:")
    print(result_with_lcel)

```

### Documentation
- https://docs.langchain.com/oss/javascript/langchain/rag#rag-agents












