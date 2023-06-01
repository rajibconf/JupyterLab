"""
!pip install openai googletrans==4.0.0rc1

Need to install above packages
"""
from googletrans import Translator
import openai

api_key = "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"  # Replace with your actual API key
openai.api_key = api_key


def translate_to_bengali(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='bn')
    return translation.text


def chat_with_model(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000
    )
    return response.choices[0].text.strip()


prompt = "what is python?"
completion = chat_with_model(prompt)
bengali_translation = translate_to_bengali(completion)
print(bengali_translation)
