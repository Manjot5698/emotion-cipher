from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=2
)

def detect_emotion(text):
    results = emotion_classifier(text)[0]
    emotions = [(r["label"], round(r["score"], 2)) for r in results]
    return emotions