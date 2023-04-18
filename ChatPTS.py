import tkinter as tk
import openai
import os
import threading
import datetime

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv('OPENAI_API_KEY') # to store your key as an environment variable on Windows, use setx OPENAI_API_KEY "<yourkey>" (and then reboot)
openai.api_base = os.getenv('OPENAI_API_BASE') # as before, use use setx OPENAI_API_BASE "https://<name>.openai.azure.com/" (and then reboot)

system_message = "Your name is ChatPTS, you are a large language model. You are using the GPT-4 preview via the Azure OpenAI Service. Answer as concisely as possible. Knowledge cutoff: September 2021. Current date: "+str(datetime.date.today())

chathistory = [{"role":"system","content":system_message}]

# Function to get the response from the OpenAI API after the 'Send' button is clicked
def send():
    # Get the user's prompt from the input box
    input_text = input_box.get("1.0", "end")

    output_box.configure(state="normal")
    output_box.insert("end", "User:\t"+input_text+"\n")
    output_box.configure(state="disabled")
    output_box.see("end")

    # Insert the user's prompt into the chat history
    inputdict = {"role":"assistant","content":input_text}
    chathistory.append(inputdict)

    # Clear the input box
    input_box.delete("1.0", "end")

    # Create a new thread for the API call
    api_thread = threading.Thread(target=call_api, args=(input_text,))
    api_thread.start()

# Function to call the OpenAI API in a separate thread to prevent locking-up the application while waiting for the API response
def call_api(input_text):
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=chathistory,
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    # Get the response from the API and insert it into the chat history
    response_dict = response.to_dict()
    content = response_dict['choices'][0]['message']['content']
    contentdict = {"role":"assistant","content":content}
    chathistory.append(contentdict)

    # Display the response in the output box
    display_response(content)

# Function to display the response in the output box
def display_response(content):

    output_box.configure(state="normal")
    # Insert the response into the output box
    output_box.insert("end", "ChatPTS:\t" + content + "\n\n")
    output_box.configure(state="disabled")
    output_box.see("end")

# Function to clear the chat boxes, and reset the chat history
def clear_chat():
    input_box.delete("1.0", "end")
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.configure(state="disabled")
    global chathistory
    chathistory = [{"role":"system","content":system_message}]

# Function to handle the "Return" key event
def handle_return(event):
    send()
    return "break"  # Prevents the default behavior of the "Return" key adding a stray carriage return after the input box has been cleared

# Create the GUI root window
root = tk.Tk()
root.title("ChatPTS")

# Create the output box with scrollbar
output_frame = tk.Frame(root)
output_frame.pack(side="top", fill="both", expand=True)
output_box = tk.Text(output_frame, wrap="word", font="Calibri 11")
output_box.pack(side="left", fill="both", expand=True)
output_scrollbar = tk.Scrollbar(output_frame, command=output_box.yview)
output_scrollbar.pack(side="right", fill="y")
output_box.config(yscrollcommand=output_scrollbar.set)
output_box.configure(state="disabled")

# Create the input box with scrollbar
input_frame = tk.Frame(root)
input_frame.pack(side="top", fill="both", expand=True)
input_box = tk.Text(input_frame, height=5, wrap="word", font="Calibri 11")
input_box.pack(side="left", fill="both", expand=True)
input_scrollbar = tk.Scrollbar(input_frame, command=input_box.yview)
input_scrollbar.pack(side="right", fill="y")
input_box.config(yscrollcommand=input_scrollbar.set)

# Bind the "Return" key to the "Send" button
input_box.bind("<Return>", handle_return)

# Create the "Ask ChatPTS" button aligned to the right of the form with 16px buffer space
ask_button = tk.Button(root, text="Send", command=send, height=2, width=10)
ask_button.pack(side="right", padx=16, pady=5)

# Create the "Clear chat" button aligned to the left of the form with 16px buffer space
clear_button = tk.Button(root, text="Clear chat", command=clear_chat, height=2, width=10)
clear_button.pack(side="left", padx=6, pady=5)

# Start the GUI event loop
root.mainloop()
