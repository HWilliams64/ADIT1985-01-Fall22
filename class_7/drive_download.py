import json
import gdown
import random


url = "https://drive.google.com/file/d/1MCB9nn6QE5uGTj30iVAf09Zjj8AStfAy/view?usp=share_link"
output = "./jokes.json"

gdown.download(url, output, quiet=True, fuzzy=True)

with open(output, 'r') as file:
    jokes = json.load(file)
    joke = random.choice(jokes)
    print(f"{joke['q']}\n{joke['a']}")