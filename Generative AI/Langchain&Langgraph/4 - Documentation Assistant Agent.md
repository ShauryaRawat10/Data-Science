## Commands
- git clone https://github.com/emarco177/documentation-helper.git -b 1-start-here **clone the repo with a specific branch in cursorAI**

## Pinecone
- Create Index: **langchain-doc-index**
  - Choose Embedding Config: text-embedding-3-small
  - Dimensions: 1536
  - Select Cloud, Region
- Create API Key: **dochelp**

## Note
- Repo already has pipefile.lock (with all packages,libraries needed)

## Commands
- pip install pipenv
- pipenv lock (create pipfile.lock)
- pipenv install (install from pipfile.lock)

What is pipfile vs pipfile.lock
- Pipfile is for humans. It defines your high-level project requirements and allows for flexibility (e.g., "I need LangChain, any version from version 0.1 onwards").
- Pipfile.lock is for machines. It guarantees deterministic builds by locking down the exact version of every single package and sub-dependency, down to the specific digital fingerprint (hash).
