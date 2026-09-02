## What is LangGraph
- Another dimension of freedom and complexity with cycles
- Flow Engineering: We define the flow and blend in with LangGraph
- Build language agents with Graphs (of cycles)

#### What is agent?
- Control flow controlled by LLM
- LLM provides reasoning on where to go
- Chain is sequential, Agents are cyclic

## Levels of Autonomy
![Levels of Autonomy](https://github.com/ShauryaRawat10/Data-Science/blob/adaf58eb23409b7d0d30cf2254dcd89e956be81d/Generative%20AI/Langchain%26Langgraph/storage/Levels-of-autonomy.png)
- Langgraph is in step 5

## LangGraph Introduction
![Langraph-intro](https://github.com/ShauryaRawat10/Data-Science/blob/adaf58eb23409b7d0d30cf2254dcd89e956be81d/Generative%20AI/Langchain%26Langgraph/storage/Langgraph-Intro.png)

#### Graph Data Structures
- Collection of vertices (nodes) and edges

#### State Machines
- Has States and Rules of transition between them
- States are nodes, transitions are edges

## Flow Engineering
- In artificial intelligence, flow engineering moves past single, massive prompts into structured, code-controlled multi-step workflows.
  - Deterministic architecture: Instead of letting an AI agent wander freely from start to finish, tasks are broken into rigid, programmatic steps.
  - Specialized usage: Traditional software handles logic and routing, while the LLM is used strictly for bounded micro-decisions and language processing.
  - Benefits: It reduces iterative loops, lowers operational costs, and increases reliability in generative AI agents. Frameworks like LangGraph often utilize this paradigm


- Future
  - 60% flow engineering (or architecture)
  - 35% Fine tuning
  - 5% prompt engineering


## LangGraph Core Components
- Nodes
  - Any code in Python, Deterministic code or LLM
  - __start__ and __end__ node do nothing, they are NOOP - No Operation
- Edges
  - Connects nodes within graph 
- Conditional Edges
  - Has conditions whether to go to Node A or B

#### State management in LangGraph
- It's a dictionary that has info of tracking graph
- Local to Graph, available on each edge
- eg: Chat history, Node execution results, Temporary results


## Cyclic Graph, Human in the Loop, Persistence (Built in function to persist graphs)






