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











