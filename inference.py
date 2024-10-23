from fastapi import FastAPI
from transformers import pipeline

# Create a FastAPI app instance
app = FastAPI()

# Load pre-trained model
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

# Inference route
@app.post("/summarize/")
async def summarize(text: str):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}