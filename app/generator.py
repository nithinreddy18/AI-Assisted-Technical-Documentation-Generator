from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


class DocGenerator:
    def __init__(self):
        print('Loading AI Model (Salesforce/codet5-base-multi-sum)...')
        self.model_name = 'Salesforce/codet5-base-multi-sum'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to(self.device)
        except Exception as e:
            raise RuntimeError(f'Failed to load AI model: {e}')

    def generate_docstring(self, code_snippet: str) -> str:
        # CLEAN INPUT: Do not add conversational instructions to CodeT5.
        # It is trained to take raw code and output a summary.
        input_ids = self.tokenizer(code_snippet, return_tensors='pt').input_ids.to(self.device)

        generated_ids = self.model.generate(
            input_ids,
            max_length=256,
            min_length=30,  # FORCE the model to write more than a few words
            num_beams=8,  # Higher beams = smarter search for the best sentence
            length_penalty=1.5,  # Encourage longer sequences
            no_repeat_ngram_size=3,  # Prevent repeating phrases like "simple English"
            early_stopping=True
        )
        return self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)


