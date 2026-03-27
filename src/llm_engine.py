# Local LLM Engine using transformers/llama.cpp

from transformers import LlamaModel, LlamaTokenizer

class LLMEngine:
    def __init__(self, model_name):
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name)
        self.model = LlamaModel.from_pretrained(model_name)

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
