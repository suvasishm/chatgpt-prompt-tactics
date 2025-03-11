# OpenAI Prompting Tactics

This document provides examples of effective prompting techniques when using the OpenAI API. Each tactic is demonstrated with an executable Python code block.

## Setup
Before running any of the examples, ensure you have installed the `openai` package and set up your API key:

1. python3 -m venv llmlearn
2. source llmlearn/bin/activate
3. pip install openai
4. export OPENAI_API_KEY=sk-..


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

## Tactic 5: Specify the Steps Required to Complete a Task

```python
text = f"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
```

### Example 1
```python
prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""
print("Completion for Tactic 5/1:")
print(get_completion(prompt))
```

### Example 2
```python
prompt = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
print("Completion for Tactic 5/2:")
print(get_completion(prompt))
```

## Tactic 6: Instruct the Model to Work Out Its Own Solution Before Rushing to a Conclusion

```python
prompt = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem including the final total. 
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
``` 
Student's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:
"""
print("Completion for Tactic 6:")
print(get_completion(prompt))
```