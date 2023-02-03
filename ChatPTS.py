import tkinter as tk
import os
import requests
import json
import openai

openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx" # API key for accessing OpenAI API
openai.api_base =  "https://xxxxxxxx.openai.azure.com" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure' # API type (for Azure API, it is "azure")
openai.api_version = '2022-12-01' # This may change in the future

deployment_id='text-davinci-003' # This will correspond to the custom name you chose for your deployment when you deployed a model. 

# Function to get the response from the OpenAI API
def ask_chatpts():

    # Get the user's prompt from the input box
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
    
    # Display the response in the output box
    output_box.delete("1.0", "end")
    output_box.insert("1.0", response["choices"][0]["text"])

# Create the GUI root window
root = tk.Tk()
root.title("ChatPTS")

# Create the input box
input_box = tk.Text(root, height=5, width=60, wrap="word", font="Calibri 11")
input_box.pack()

# Create the "Ask ChatPTS" button
ask_button = tk.Button(root, text="Ask ChatPTS", command=ask_chatpts)
ask_button.pack()

# Create the scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Create the output box
output_box = tk.Text(root, height=35, width=60, wrap="word", font="Calibri 11", yscrollcommand=scrollbar.set)
output_box.pack()

# Set the scrollbar command to the output box
scrollbar.config(command=output_box.yview)

# Start the GUI event loop
root.mainloop()
