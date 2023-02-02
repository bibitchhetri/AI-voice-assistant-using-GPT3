import openai

# Set OpenAI API key
openai.api_key = "your-api-key"

def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

print("Hi, I am a chatbot powered by OpenAI GPT-3. How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = chatbot(user_input)
    print("Chatbot: " + response)
