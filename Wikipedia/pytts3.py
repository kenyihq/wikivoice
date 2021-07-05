from wikipedia.exceptions import PageError
import pyttsx3
import wikipedia
wikipedia.set_lang("es")


def search(keyword):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    try:
        result = wikipedia.summary(keyword, sentences = 1)
        print(result)
        engine.say(result)    
    except PageError:
        engine.say(f"Lo siento Ken-yi no pude encontrar {keyword}")

    engine.runAndWait()
keyword = input("Buscar: ")
search(keyword)

#engine.say("Hola TutankaDev")