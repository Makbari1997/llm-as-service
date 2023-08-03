
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "model_name"  # Replace with the actual model name
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
