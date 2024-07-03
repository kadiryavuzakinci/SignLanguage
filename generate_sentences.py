import openai
import yaml

class SentenceGenerator:
    def __init__(self, config_path="config.yaml"):
        self.api_key = self._load_api_key(config_path)
        openai.api_key = self.api_key

    def _load_api_key(self, config_path):
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                return config.get('api_key')
        except Exception as e:
            print(f"An error occurred while loading the API key: {e}")
            return None

    def generate_meaningful_sentence(self, words):
        try:
            prompt = "Generate a meaningful sentence with the given words: " + ', '.join(words)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            sentence = response.choices[0].message['content'].strip()
            return sentence
        except Exception as e:
            print(f"An error occurred while generating the sentence: {e}")
            return "Error generating sentence"

    def process_words_file(self, input_file="words.txt", output_file="meaningful.txt"):
        try:
            with open(input_file, 'r') as file:
                words = file.read().replace('\n', '').split(', ')
                sentence = self.generate_meaningful_sentence(words)
                
                with open(output_file, 'w') as out_file:
                    out_file.write(sentence)
        except Exception as e:
            print(f"An error occurred while processing words file: {e}")
