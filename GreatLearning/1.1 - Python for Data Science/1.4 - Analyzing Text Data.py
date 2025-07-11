# Databricks notebook source
# MAGIC %md
# MAGIC Structured vs unstructured data
# MAGIC - How to convert unstaructured data to structured form that we can use
# MAGIC
# MAGIC Ex 01:
# MAGIC - Bag of words:
# MAGIC   - Documents simply represented by the words in the document and their frequencies. Disregards grammar and word order 
# MAGIC   - Bayseian SPAM filter
# MAGIC - Semantics: 
# MAGIC   - Mapping natural language rules to get formal representation of meaning of text
# MAGIC   - Name entity identification

# COMMAND ----------

# MAGIC %md
# MAGIC - Bag of words
# MAGIC   - separating words into -> Spam / not spam
# MAGIC   - spam -> Buy, stock
# MAGIC   - not spam -> meeting, dinner
# MAGIC
# MAGIC - Semantics
# MAGIC   - Can it understand the semantics, what people are talking about based on all documents
# MAGIC   - Powerful, but complex

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1-gram vs 2gram vs trigram
# MAGIC #### corpus : corpus is entire collection of documents/words
# MAGIC
# MAGIC - A: John likes to play soccer
# MAGIC - B: John is reading a book
# MAGIC
# MAGIC |      | John | likes | soccer | play | book | reading | a | is | to |
# MAGIC |------|------|--------|--------|------|------|---------|---|----|----|
# MAGIC | **A** | 1    | 1      | 1      | 1    |      |         |   |    | 1  |
# MAGIC | **B** |      |        |        |      | 1    | 1       | 1 | 1  |    |
# MAGIC
# MAGIC
# MAGIC - Bag of words method is orderless document representation. Only counts of words matter
# MAGIC - We could do this by choosing consecutive pairs (2-gram) and representing each pair
# MAGIC
# MAGIC |         | John likes | likes to | play soccer | to play | John is | is reading | reading a | a book |
# MAGIC |---------|------------|----------|-------------|---------|---------|------------|-----------|--------|
# MAGIC | **A** | 1          | 1        | 1           | 1       |         |            |           |        |
# MAGIC | **B** |            |          |             |         | 1       | 1          |           |    1    |
# MAGIC
# MAGIC
# MAGIC - Every document is a vector. Document by document having multiple terms
# MAGIC   - Document term matrix 
# MAGIC
# MAGIC - In BoW model, each term is called a dimension
# MAGIC
# MAGIC - text-cleaning
# MAGIC   - now word reading and read are same
# MAGIC   - Stop words removal : common words that are not useful in providing value or context eg: **the, an, in,etc**
# MAGIC   - Stemming: Returning words in their original stem. eg: **Chopping, Chopped** are all replaced by **Chop**
# MAGIC   - Lowercase conversion
# MAGIC   - remove punctuation
# MAGIC   - strip extra white spaces
# MAGIC   - remove numbers
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### **Original Text and Word Frequencies (Before Stop Word Removal)**
# MAGIC
# MAGIC ``
# MAGIC Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense. Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors.
# MAGIC ``
# MAGIC
# MAGIC | word      | freq |
# MAGIC |-----------|------|
# MAGIC | the       | 4    |
# MAGIC | and       | 3    |
# MAGIC | dursley   | 3    |
# MAGIC | they      | 3    |
# MAGIC | very      | 3    |
# MAGIC | was       | 3    |
# MAGIC | were      | 3    |
# MAGIC | mrs       | 2    |
# MAGIC | much      | 2    |
# MAGIC | neck      | 2    |
# MAGIC
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ##### **Text and Word Frequencies (After Stop Word Removal)**
# MAGIC
# MAGIC *Note: Words are typically filtered out from text data before processing*
# MAGIC
# MAGIC
# MAGIC ``
# MAGIC Mr. Mrs. Dursley, number four, Privet Drive, proud say perfect normal, thank much. They last peopl expect involv anyth strang mysterious, just hold nonsense. Mr. Dursley director firm call Grunnings, made drills. He big, beefi man hard neck, although larg mustache. Mrs. Dursley thin blond near twice usual amount neck, came use spent much time crane garden fences, spi neighbors.
# MAGIC ``
# MAGIC
# MAGIC | word      | freq |
# MAGIC |-----------|------|
# MAGIC | dursley   | 3    |
# MAGIC | mrs       | 2    |
# MAGIC | much      | 2    |
# MAGIC | neck      | 2    |
# MAGIC | although  | 1    |
# MAGIC | amount    | 1    |
# MAGIC | anyth     | 1    |
# MAGIC | beefi     | 1    |
# MAGIC | big       | 1    |
# MAGIC | blond     | 1    |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Sentiment Analysis** - Analyzing text to understand sentiment
# MAGIC - Detect polarity (eg: positive or negative opinion) or emotion (eg: happy, sad, angry) or even intent (query, complaint, sugesstion) within text
# MAGIC - The text could be a review (product, movie, book, restaurant, a whole document, paragraph, sentence, clause)
# MAGIC - Applications: Customer Service, Social media/reviews/email monitoring, market research
# MAGIC - Approcahes: Lexicon based, ML based 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Lexicon-Based Sentiment Analysis Notes**
# MAGIC
# MAGIC * A lexicon maps each word to a polarity (e.g., positive/negative).
# MAGIC * Count the number of positive and negative words.
# MAGIC * If number of positive is greater, conclude a positive sentiment.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Lexicon Example:**
# MAGIC
# MAGIC | #   | word        | sentiment |
# MAGIC |-----|-------------|-----------|
# MAGIC | 1   | abacus      | trust     |
# MAGIC | 2   | abandon     | fear      |
# MAGIC | 3   | abandon     | negative  |
# MAGIC | 4   | abandon     | sadness   |
# MAGIC | 5   | abandoned   | anger     |
# MAGIC | 6   | abandoned   | fear      |
# MAGIC | 7   | abandoned   | negative  |
# MAGIC | 8   | abandoned   | sadness   |
# MAGIC | 9   | abandonment | anger     |
# MAGIC | 10  | abandonment | fear      |
# MAGIC | ... |             |           |
# MAGIC |     | # with 13,891 more rows |           |
# MAGIC
# MAGIC ---
# MAGIC