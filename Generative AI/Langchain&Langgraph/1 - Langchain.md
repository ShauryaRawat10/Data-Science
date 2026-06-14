
## Langchain


#### Installation
1. Install Git
2. Install Cursur IDE

#### Git commands

Git Commands:
- Copy repo into local: git clone https://github.com/emarco177/langchain-course.git
- Create new branch:
  - cd langchain-course
  - cd checkout --orphan project/hello-world
    - output: switched to new branch
- Remove all file from branch: git rm -rf . 
- pip3 install uv
- uv --help

UV Commands:
- uv init
- uv add langchain
- uv add langchain-openai
- uv add python-dotenv
- uv add python-dotenv black isort

1. Create .env file:
OPENAI_API_KEY=APIKEY

2. Create .gitignore file
  - Add everything from github/python-gitignore

3. Execute code:
```
from dotenv import load_dotenv
import os 

load_dotenv()

def main():
    print(os.getenv("OPENAI_API_KEY"))
    print("Hello from langchain-course!")

if __name__ == "__main__":
    main()
```

















