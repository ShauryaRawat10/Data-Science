## Prompt Engineering Theory

#### Gist of LLM
- What is Language modeling?
  - Task of predicting, what word will come up next
  - Supersmart autocomplete
  - Given a sequence of words x1, x2, x3 .... Xt, compute the probability distribution of next word P(xt+1 | x1, x2, .... xt)
 
#### Prompt
- What is prompt?
  - A prompt in prompt engineering is a specific input or task given to a language model to generate a desired output
  - 4 different components
    - Instructions
    - Context
    - Input Data
    - Output Indicator
  - Instructions:
    - Heart of a prompt which tells what tasks need to be performed
    - eg: Summarize following text into 3 sentences or less
  - Context
    - Additional information to fine tune the instruction
  - Input Data
    - Input data for AI model
  - Output Indicator
    - eg: Positive, neural or negative

#### Zero Shot Prompting
- Zero shot prompt is a type of prompt in which the model generates an output for that task it has not been explicitly trained on
- Model performs task without a specific training data. **Model is guessing at its best effort without having seen any examples of result you want**
- Prompt does not contain any explicit instructions or examples for the model to follow. Instead, it relies on model's ability to understand and interpret natural language
- eg: Create a list of top 10 must visit cities in world in no particular order.
  - Zero shot prompt above has no examples, no input data and relies on model knowledge
- Limitation: Accuracy, Limited scope, no fine tune for specific use case


#### Few shot Prompting
- Works by presenting the model with a small number of examples or shots of a particular task or concept, along with prompt or instruction
- Used when limited data is available
  - One Shot Prompting: **Model is given just 1 example of the result you want**
  - Few Shot Prompting: **Model is given a few examples of the result you want**

#### Chain of Thought Prompting
- LLM limitations:
  - LLM can do Suummarization, Image generation, Code generation, Code optimization
  - LLM can not do Multi-Step reasoning, and Common sense
- COT Prompting aim to improve performance of LLM, and enables model to decompose multi-step problems into intermediate steps allowing model to solve complex reasoning problems
- Types:
  - Zero shots COT prompting
    - Prefixing the answer block with **"Let's think step by step"** This prompts the LLM to complete the output in that format
  - Few shots COT prompting
    - provides examples of **<question, answer>** pairs where the answer is explained **"step by step"**
   

#### ReAct Prompting
- Reasearch paper -> Synerziging reasoning and acting in language models
- ReAct is a paradigm that integrates language models with reasoning and acting capabilities, allowing for dynamic reasining and interaction with extrenal env to perform complex tasks
- ReAct -> COT + Action

![ReAct Prompting](https://github.com/ShauryaRawat10/Data-Science/blob/2b68813bf3b2d1a71b0e6fe1c1e161b28f661440/Generative%20AI/Langchain%26Langgraph/storage/ReAct_COT%2BAction.png)


#### Prompt Engineering tips
- Low hanging fruits tips to make prompts better
- Write a good prompt
  - **Context**: Contexual relevance for generating coherent and accurate responses. If not provided, LLM may generate its own which may not be relevant
  - **Clear, non ambiguous task**
  - **Iterations**
    - Also can do testing and quality check of prompt

#### Context Engineering
- Has context window, the context can come from n number of sources (types of context)
  - Instructions
  - Knowledge
  - Tools 
- Number of context sources is increasing everyday
- Every tool call has feedback from tool call, so the context window keeps on growing and start hallucination
- **Context Poisoning** : One tool/llm call introduces hallucination that makes it to context in terms degarding assistant
- **Context Confusion:** : Context which contradict and is irrelevant

![Context engineering](https://github.com/ShauryaRawat10/Data-Science/blob/a149623fb18005da12d44416aa350513fce6e5e6/Generative%20AI/Langchain%26Langgraph/storage/contextengineering.png)

![Context challenges](https://github.com/ShauryaRawat10/Data-Science/blob/a149623fb18005da12d44416aa350513fce6e5e6/Generative%20AI/Langchain%26Langgraph/storage/contextchanllenges.png)

















