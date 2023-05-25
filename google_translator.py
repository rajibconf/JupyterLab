from googletrans import Translator

def translate_to_bengali(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='bn')
    return translation.text

# Example usage
text = "how can i get a package who can traslate english to bengali number"
bengali_translation = translate_to_bengali(text)
print(bengali_translation)