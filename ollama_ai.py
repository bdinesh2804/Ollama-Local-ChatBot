import ollama

while True:
    user = input('You: ')
    if user.lower() == 'bye':
        print('Bye!')
        break
    response = ollama.chat(model = 'llama3.2', messages=[{'role' : 'user', 'content': user}] )
    print('Chatbot:', response['message']['content'])