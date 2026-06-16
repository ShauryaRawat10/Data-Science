
## Langchain
- Open source framework that simplifies for us to create complex LLM application
- Used to create Agents and RAG applications
  - Has abstrated classes and functions available
  - Prompt engineering templates
  - Has data extraction technique

## Course
- Build AI Agents with Langchain and Langgraph RAG, Tools, MCP, and Production-Ready Agentic AI Systems (Python)
- LLM Specialist @Google Cloud, Eden Marco

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

#### Langgraph
<img width="1601" height="572" alt="image" src="https://github.com/user-attachments/assets/5753425c-15ac-4658-95aa-60ed453e2476" />


#### Templates

```
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and former public official known for his leadership of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025 and became the first person with a net worth exceeding US$1 trillion in June 2026, Forbes estimates his net worth to be US$1.1 trillion.

    Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.

    In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left; growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired the social network Twitter, implementing significant changes, and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company The Boring Company, which he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if he meets specific goals.
    """

    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting fact about them
    """

    summary_prompt_template= PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # 0 temperature good for summarization and 1 is good for poetry and creativity
    llm= ChatOpenAI(temperature=0, model="gpt-5")

    # Langchain Expression language to chain together the components
    # Runnable chain - Runnable interface
    chain = summary_prompt_template | llm

    response=chain.invoke(input={"information": information})
    print(response.content)
```

#### Open weights model: Langchain with Ollama
- Download ollama from ollama.com
- CLI
  - ollama
  - ollama pull gemma3:270m
  - ollama list
  - ollama --help
  - ollama run gemma3:270m
    

#### Lanchain vs langsmith
LangChain is an open-source framework used to build and orchestrate LLM applications (like chatbots, RAG pipelines, and agents). LangSmith is a platform used to observe, debug, test, and monitor these AI applications in production



## The Gist of AI Agents

#### What are AI Agents?
- An agent is software system that uses LLMs as reason engine to decide what actions to take and execute those actions

-> React Agents

Query -> LLM (Reason) -> Action -> Observations -> LLM (Reason) -> Output


***
#### Langchain tavily: Connect Agent to Web
- Connect websearch to agent

#### Tools: Function AI can execute
- Agent can perform endless possibility of execution
- @tool decorator
  - API
  - Database Search


## Tavily Implementation (Tool)
- Websearch tool
- Monitor with langssmith 


```
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool 
def search(query: str) -> str:
    """
    Tool that serached over internet
    Args:
        query: The query to serach for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    # return "Tokyo Weather is Sunny"
    return tavily.search(query=query)


llm = ChatOpenAI()
tools= [search]
agent=create_agent(model=llm, tools=tools)

def main():
    result=agent.invoke({"messages":HumanMessage(content="What is weather in Tokyo") })
    print(result)

if __name__ == "__main__":
    main()

```


## Tavily Implementation with Langchain

Package: langchain-tavily

```
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOpenAI(model="gpt-5")
tools= [TavilySearch()]
agent=create_agent(model=llm, tools=tools)

def main():
    result=agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for an ai angineer in india") })
    print(result)

if __name__ == "__main__":
    main()
```


#### Pydantic 
- Structured Output

```
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from typing import List
# Import BaseModel and Field Class
from pydantic import BaseModel, Field


# Class Source is inheritred by Pydantic Class BaseModel
class Source(BaseModel):
    """ Schema for a source used by the agent"""
    url:str= Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str=Field(description="The agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


@tool 
def search(query: str) -> str:
    """
    Tool that serached over internet
    Args:
        query: The query to serach for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    # return "Tokyo Weather is Sunny"
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5")
tools= [TavilySearch()]
agent=create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    result=agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for an ai angineer in india") })
    print(result)

if __name__ == "__main__":
    main()

```

<img width="852" height="475" alt="image" src="https://github.com/user-attachments/assets/3555fa24-31c2-4089-9c5c-efd512bc6579" />


***

## Agents Under The hood
- This teaches how Agents works when they first came out. It will help in knowing Agents working behind the scenes better
- This one uses Ollama 

<img width="407" height="622" alt="image" src="https://github.com/user-attachments/assets/b7c71b40-479d-4c3c-afc6-656bbacad748" />

















