python
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model and tokenizer
model_name = "gpt2"  # Replace with the desired model name
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route("/generate", methods=["POST"])
def generate_text():
    # Parse the input parameters
    data = request.get_json()
    prompt = data["prompt"]
    max_length = data.get("max_length", 100)
    temperature = data.get("temperature", 0.7)

    # Generate text using the model
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Return the generated text as a response
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
