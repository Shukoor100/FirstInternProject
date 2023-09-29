import tkinter as tk

sampleText = "This is Sample text"

# Write Your Speech to Text code here
def speechToText():
    return sampleText

# Write Sentiment Analysis code here
def getSentiment(rawText):
    return "Sample Sentiment"


root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("500x500")

mainTitle = tk.Label(root, anchor="center", text="Sentiment Analysis", font=("Roboto", 25)).pack()

subTitle1 = tk.Label(root, text="Speech to Text:", font=("Arial", 18), pady=10)

sentiment = tk.Label(root, text="No Sentiment", font=("Roboto, 15"), pady=20)

textBox = tk.Text(root, height=6, width=30, padx=5, pady=5)

def startButton():
    print("Button 1 is pressed")
    tempText = speechToText()
    textBox.delete("1.0", "end")
    textBox.insert("1.0", tempText)

def getSentimentButton():
    print("Button 2 is pressed")
    tempText = textBox.get("1.0", "end")
    resText = getSentiment(tempText)
    sentiment.config(text=resText)
    

btn1 = tk.Button(root, text="START", height=1, width=30, bg="#BDBDBD", command=startButton)

btn2 = tk.Button(root, text="GET SENTIMENT", height=1, width=30, bg="#BDBDBD", command=getSentimentButton)

subTitle1.pack()
textBox.pack()
btn1.pack()
sentiment.pack()
btn2.pack()

root.mainloop()