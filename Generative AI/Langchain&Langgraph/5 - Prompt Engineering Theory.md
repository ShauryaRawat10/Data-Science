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












