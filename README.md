# OpenAI Prompting Tactics

This document provides examples of effective prompting techniques when using the OpenAI API. Each tactic is demonstrated with an executable Python code block.

## Setup
Before running any of the examples, ensure you have installed the `openai` package and set up your API key:

```python
from openai import OpenAI

client = OpenAI()

def get_completion(prompt, model="gpt-4o"):
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # This is the degree of randomness of the model's output
    )
    
    return response.choices[0].message.content  # Corrected attribute access
```

## Tactic 1: Use Delimiters to Clearly Indicate Distinct Parts of the Input

```python
text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""
print("Completion for Tactic 1:")
print(get_completion(prompt))
```

## Tactic 2: Ask for a Structured Output

```python
prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
print("Completion for Tactic 2:")
print(get_completion(prompt))
```

## Tactic 3: Ask the Model to Check Whether Conditions are Satisfied

```python
text_1 = f"""
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""
prompt = f"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

"""{text_1}"""
"""
print("Completion for Tactic 3:")
print(get_completion(prompt))
```

## Tactic 4: "Few-Shot" Prompting

```python
prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
print("Completion for Tactic 4:")
print(get_completion(prompt))
```

