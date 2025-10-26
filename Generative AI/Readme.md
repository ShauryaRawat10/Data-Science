# Stock Market News: Sentimental Analysis and Summarization

- Generative AI: Word2Vec, GloVe, SentenceTransformer, Lllama

## Problem Statement
Business Context
The prices of the stocks of companies listed under a global exchange are influenced by a variety of factors, with the company's financial performance, innovations and collaborations, and market sentiment being factors that play a significant role. News and media reports can rapidly affect investor perceptions and, consequently, stock prices in the highly competitive financial industry. With the sheer volume of news and opinions from a wide variety of sources, investors and financial analysts often struggle to stay updated and accurately interpret its impact on the market. As a result, investment firms need sophisticated tools to analyze market sentiment and integrate this information into their investment strategies.

## Problem Definition
With an ever-rising number of news articles and opinions, an investment startup aims to leverage artificial intelligence to address the challenge of interpreting stock-related news and its impact on stock prices. They have collected historical daily news for a specific company listed under NASDAQ, along with data on its daily stock price and trade volumes.

As a member of the Data Science and AI team in the startup, you have been tasked with analyzing the data, developing an AI-driven sentiment analysis system that will automatically process and analyze news articles to gauge market sentiment, and summarizing the news at a weekly level to enhance the accuracy of their stock price predictions and optimize investment strategies. This will empower their financial analysts with actionable insights, leading to more informed investment decisions and improved client outcomes.

## Data Dictionary
- Date : The date the news was released
- News : The content of news articles that could potentially affect the company's stock price
- Open : The stock price `(in $)` at the beginning of the day
- High : The highest stock price `(in $)` reached during the day
- Low : The lowest stock price `(in $)` reached during the day
- Close : The adjusted stock price `(in $)` at the end of the day
- Volume : The number of shares traded during the day
- Label : The sentiment polarity of the news content
  - 1: positive
  - 0: neutral
  - -1: negative
 





## **Overall Conclusions**
- Embedding ranking (by Validation): **Sentence Transformer** > GloVe > Word2Vec
- Sentence Transformer has same performance in tuned and base version for validation dataset
- Glove also has same performance in both base and tuned versions, Word2Vec has little increase in tuned version
- Test dataset Performance:
  - Test data has best performance with accuracy, precision and recall as 1

- Final model selection:
  - **Sentence Transformer** Base model is best for productionization, as both tuned and base model have same performance
- LLM Model for summarization:
  - **Mistral-7B-Instruct-v0.2-GGUF** worked perfect for summrization after fine tuning the prompts and model parameters, giving sigificantly better results for top positive and negative sentiments


---

#### Recommendation

  - Recommended **Champion** Model
    - Balanced classification (−1/0/+1 treated equally):
      - Champion = **Base Sentence Transformer** (best Val Accuracy = 0.52) and (Best Training and Test accuracy = 1)
  - Multiple ways of setting up the prompts is needed to do AB testing in result set and fine tunning of the model
  - It is important to explore and experiment with newer model version and LLM models from hugging face. The model **Mistral-7B-Instruct-v0.2-GGUF** is used and performed significantly better for our use case
  - Top market sentiments (Positive and Negative) identified by LLM based on all the news available for the stock can be stored in database for reporting and analysis
