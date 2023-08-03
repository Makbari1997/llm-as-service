python
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)
model_name = "openai-gpt"  # Replace with the appropriate LLM model name
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route("/generate", methods=["POST"])
def generate_text():
    input_text = request.json["input_text"]
    max_length = request.json.get("max_length", 100)
    temperature = request.json.get("temperature", 0.8)

    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run()
