import tkinter as tk
from tkinter import scrolledtext

def simple_chatbot(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hi there! How can I help you today?"

    elif 'how are you' in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif 'your name' in user_input:
        return "I'm a chatbot. You can call me ChatGPT."

    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day."

    elif 'weather' in user_input:
        return "I'm sorry, I don't have real-time weather information."

    elif 'joke' in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif 'who are you' in user_input or 'what are you' in user_input:
        return "I am a simple rule-based chatbot designed to assist with basic queries."

    elif 'help' in user_input:
        return "Sure, I can help you with general information, jokes, or just chat!"

    elif 'python' in user_input:
        return "Python is a high-level programming language known for its readability and versatility."

    elif 'hobbies' in user_input:
        return "I don't have hobbies, but I enjoy helping you with your queries!"

    elif 'programming languages' in user_input:
        return "There are many programming languages, such as Python, Java, and C++, each with its own strengths."

    elif 'fun fact' in user_input:
        return "Fun fact:Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

def send_message():
    user_input = user_entry.get()

    if user_input.lower() == 'exit':
        chat_history.insert(tk.END, "Chatbot: Goodbye!\n")
        root.destroy()
    else:
        response = simple_chatbot(user_input)
        chat_history.insert(tk.END, f"You: {user_input}\n")
        chat_history.insert(tk.END, f"Chatbot: {response}\n")
        user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("JDN Chatbot")

welcome_message = "Welcome! I'm JDN BOT , your friendly chatbot. Ask me anything!"
welcome_label = tk.Label(root, text=welcome_message, font=('Helvetica', 12, 'bold'))
welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

chat_history = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
chat_history.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

user_entry = tk.Entry(root, width=40)
user_entry.grid(row=2, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
