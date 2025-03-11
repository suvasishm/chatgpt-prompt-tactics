from openai import OpenAI

client = OpenAI()

def get_completion(prompt, model="gpt-4o"):
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    
    return response.choices[0].message.content 


address = f"""
555 N Michigan Ave, CHICAGO, IL 60600.
"""
prompt = f"""
Given a US address in tripple backquote,\
 please validate if the address exists.\
 Do not rush to an answer. Analyze before returning.\
 For example, if an apartment or suite or unit number\
 (secondary address designate) is given, analyze if it is highrise.\
 And if so, how many stories it has before returning.\

 Return the result in JSON format with the following keys: 
 isValid, reason, givenAddress, suggestedAddress

 The "isValid" to return true for valid address, false for invalid address, unknown if you do not know the answer.
 The "reason" key should brief the reason of invalidation.
 "givenAddress" should return the input address without change.
 "suggestedAddress" should return the address in correct format \
 when the address is valid. \
 Otherwise, if you have possible address suggestion, return that.\
 For example, if city / zip is not matching, \
 provide a suggested address with a correct zip code for the given city\
 and vice-versa. Leave it blank in all other cases.


 For example, if the given address is \
 "535 N Michigan Ave. Apt 3509. Chicago. IL 60611.",\
 your answer should be "Invalid address" because \
 the building has either 33 or 34 stories, Apt 3509 would not exist.\
 
 
 If the given address is \
 "535 N Michigan Ave. APT 1409. CHicago. IL 60611.",\
 your answer should be the correct formatted address \
 "535 N Michigan Ave. Apt 1409. Chicago. IL 60611.".\

```{address}```
"""
print("Address validation result:")
print(get_completion(prompt))



