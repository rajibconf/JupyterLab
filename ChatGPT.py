"""
1. pip install openai

Need to install above packages
"""

import openai

api_key = "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"  # Replace with your actual API key
openai.api_key = api_key


def chat_with_model(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000
    )
    return response.choices[0].text.strip()


prompt = "what is python?"
completion = chat_with_model(prompt)
print(completion)
