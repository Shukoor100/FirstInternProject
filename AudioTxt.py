import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        
        r = sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
        except sr.UnknownValueError:
            print(" could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results ; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

root = tk.Tk()
root.geometry("300x200")

browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack(pady=20)

root.mainloop()