import openai
import speech_recognition as sr
import pyttsx3

# Set OpenAI API key
openai.api_key = "your-api-key"

def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def get_audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        text = r.recognize_sphinx(audio)
        print("You said: {}".format(text))
        return text
    except:
        print("Sorry, I didn't get that.")
        return None

def play_audio_output(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(text)
    engine.runAndWait()

print("Hi, I am Suzu, your personal voice assistant. How can I help you today?")
play_audio_output("Hi, I am Suzu, your personal voice assistant. How can I help you today?")

while True:
    user_input = get_audio_input()
    if user_input is None:
        print("Sorry, I didn't get that.")
        play_audio_output("Sorry, I didn't get that.")
        continue
    if "bye" in user_input.lower():
        print("Goodbye! Have a great day.")
        play_audio_output("Goodbye! Have a great day.")
        break
    response = chatbot("Suzu: " + user_input)
    print("Suzu: " + response)
    play_audio_output(response)

