import tkinter as tk
import speech_recognition as sr
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    com: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    good_thres: float = threshold
    bad_thres: float = -threshold

    if sentiment >= good_thres:
        return Mood("Positive", sentiment)
    elif sentiment <= bad_thres:
        return Mood("Negative", sentiment)
    else:
        return Mood("Neutral", sentiment)

sampleText = "This is Sample text"

def browse_file():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        
        r = sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                printText(text)
        except sr.UnknownValueError:
            print(" could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results ; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def speechToText():
    return sampleText

def getSentiment(rawText):
    mood: Mood = get_mood(rawText, threshold=0.3)
    res = mood.com + " " + str(mood.sentiment)
    return res


root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("500x500")

mainTitle = tk.Label(root, anchor="center", text="Sentiment Analysis", font=("Roboto", 25)).pack()

subTitle1 = tk.Label(root, text="Speech to Text:", font=("Arial", 18), pady=10)

sentiment = tk.Label(root, text="No Sentiment", font=("Roboto, 15"), pady=20)

textBox = tk.Text(root, height=6, width=30, padx=5, pady=5)

emptyIndent = tk.Label(root, height=1, width=30)

def printText(txt):
    textBox.delete("1.0", "end")
    textBox.insert("1.0", txt)

def startButton():
    print("Button 1 is pressed")
    tempText = speechToText()
    printText(tempText)
    

def getSentimentButton():
    print("Button 2 is pressed")
    tempText = textBox.get("1.0", "end")
    resText = getSentiment(tempText)
    sentiment.config(text=resText)
    

btn1 = tk.Button(root, text="START", height=1, width=30, bg="#BDBDBD", command=startButton)

btn2 = tk.Button(root, text="GET SENTIMENT", height=1, width=30, bg="#BDBDBD", command=getSentimentButton)

btn3 = tk.Button(root, text="BROWSE", height=1, width=30, bg="#BDBDBD", command=browse_file)

subTitle1.pack()
textBox.pack()
btn1.pack()
emptyIndent.pack()
btn3.pack()
sentiment.pack()
btn2.pack()

root.mainloop()
