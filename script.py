import openai
import requests
import json
from get_env import print_env


env = print_env(["api_key"])

try:
    openai.api_key = env["api_key"]
except KeyError:
    print("A variável de ambiente 'api_key' não foi encontrada.")

openai.api_key = env["api_key"]

model = "text-davinci-003"

while True:
    prompt = input("Digite aqui: ")

    completion = openai.Completion.create(
        engine = model,
        temperature = 0.2,
        prompt = prompt,
        max_tokens = 1024
    )
    response = completion.choices[0].text
    print(response)