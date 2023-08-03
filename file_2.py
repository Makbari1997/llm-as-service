
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=num_tokens)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
