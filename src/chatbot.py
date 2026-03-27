from llm_engine import LLMEngine
from memory_manager import MemoryManager
from feedback_processor import FeedbackProcessor

class Chatbot:
    def __init__(self, model_name):
        self.llm_engine = LLMEngine(model_name)
        self.memory_manager = MemoryManager()
        self.feedback_processor = FeedbackProcessor()

    def chat(self, user_input):
        response = self.llm_engine.generate_response(user_input)
        self.memory_manager.add_memory(user_input + ' -> ' + response)
        return response
