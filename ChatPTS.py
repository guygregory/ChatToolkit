import tkinter as tk
import os
import requests
import json
import openai

openai.api_key = "XXXXXXXXXXXXXXXXXXXXXXXX" # your API key, this can be found from the Azure OpenAI resource, under 'Resource Management > Keys and Endpoint. Either Key 1 or Key 2 can be used
openai.api_base =  "https://XXXXXXXXXX.openai.azure.com" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/

openai.api_type = 'azure'
openai.api_version = '2022-12-01' # this may change in the future

deployment_id='text-davinci-003' #This will correspond to the custom name you chose for your deployment when you deployed a model. 

def ask_chatpts():

    input_text = input_box.get("1.0", "end")

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=input_text,
    temperature=0.8,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1,
    stop=None)
 
    output_box.delete("1.0", "end")
    output_box.insert("1.0", response["choices"][0]["text"])

root = tk.Tk()
root.title("ChatPTS")

input_box = tk.Text(root, height=5, width=60, wrap="word", font="Calibri 11")
input_box.pack()

ask_button = tk.Button(root, text="Ask ChatPTS", command=ask_chatpts)
ask_button.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

output_box = tk.Text(root, height=35, width=60, wrap="word", font="Calibri 11", yscrollcommand=scrollbar.set)
output_box.pack()

scrollbar.config(command=output_box.yview)

root.mainloop()
