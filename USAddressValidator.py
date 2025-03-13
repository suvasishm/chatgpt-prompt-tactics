from openai import OpenAI

client = OpenAI()

instructions = f"""
    You are an address lookup assistant that validates and returns a well-formatted US address.
    - Ensure the response is **pure JSON** without any markdown formatting (no triple backticks, no "json" prefix).
    - Do **not** format the response as a code block. Just return valid JSON directly.
    - Validate:
    - The ZIP code is valid.
    - The state and city exist in the ZIP code.
    - The addressLine1 exists in the city, state, and ZIP code.
    - If the address has a secondary unit (apt, ste, unit), validate the aptNumber.
    - If aptNumber is missing but required, set "aptRequired: true".
    - If aptNumber is provided but does not match building floors, return "aptRequired: true" and omit the aptNumber.
    - If the address lacks a secondary unit but an aptNumber is provided, set "aptRequired: true" and remove aptNumber.
    - If minor corrections (like missing 'Ave' or 'St') are needed, return the corrected version.
    - If the address is **invalid**, return the given input **with reasoning** explaining why.
    - If the address is **valid**, return a well formatted address with "OK" for the "reasoning" field.
    
"""


def get_response(prompt, model="gpt-4o"):
    response = client.responses.create(
        model=model,
        instructions=instructions,  # 'instructions' instead of 'messages'
        input=prompt,
    )

    return response.output_text  # Corrected attribute access



prompt = f"""
555 N Michigan Ave, CHICAGO, IL 60611.
"""
print("Address validation result:")
print(get_response(prompt))



