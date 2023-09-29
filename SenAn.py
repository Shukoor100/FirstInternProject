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
    
if __name__ == '__main__':
    while True:
        text: str = input("Text: ")
        mood: Mood = get_mood(text, threshold=0.3)

        print(f'{mood.com} ({mood.sentiment})')