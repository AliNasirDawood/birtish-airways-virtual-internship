import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
# Load and preprocess CSV data
data = pd.read_csv("data.csv")
reviews = data["Review"].tolist()

# Train a GPT-2 model (this is a simplified example)
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Chatbot interaction
user_input = input("You: ")
chat_history = user_input

while True:
    input_ids = tokenizer.encode(chat_history, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    print("Chatbot:", response)
    user_input = input("You: ")
    chat_history += "\n" + user_input
