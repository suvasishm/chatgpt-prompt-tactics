# ChatGPT (LLM) Prompt Tactics and Various Example Usage 

Documenting some effective prompting tactics for different use cases as I am learning.

## Setup
Before running any of the examples, ensure you have installed the `openai` package and set up your API key:

```shell
python3 -m venv llmlearn
source llmlearn/bin/activate
pip install openai
python3 -m pip install --upgrade pip
```

```shell
export OPENAI_API_KEY=<sk-..>
```

## Option 1: To Use the Virtual Environment Inside Jupyter
```shell
pip install ipykernel
python -m ipykernel install --user --name=llmlearn --display-name "Python (llmlearn)"
```

Launch notebook 
```shell
jupyter-notebook
```

## Option 2: To run the individual python file

### Run GeneralGuidelines
```shell
python GeneralGuidelines.py
```

### Run USAddressValidator

Update the address specified in `prompt` within the file

```shell
python USAddressValidator.py
```

