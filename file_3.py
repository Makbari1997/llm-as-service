
import requests

url = "http://localhost:5000/generate"  # Replace with the actual API endpoint URL
data = {
    "input_text": "Input text here",
    "num_tokens": 100
}
response = requests.post(url, json=data)
generated_text = response.json()
print(generated_text)
