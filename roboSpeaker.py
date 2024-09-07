import pyttsx3
if __name__ == '__main__':
    print("Welcome to RoboSpeaker creted by Aishwarya : ") 
    while True:
        x = input("Say, ")
        if(x=='q'):
              engine = pyttsx3.init()
              engine.say("Bye bye friend!")
              engine.runAndWait()
              break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()

