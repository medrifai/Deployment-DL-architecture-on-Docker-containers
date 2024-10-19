from fastapi import FastAPI
from transformers import pipeline
import gradio as gr

# Créer une instance de l'application FastAPI
app = FastAPI()

# Charger le modèle pré-entraîné
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

# Route pour l'inférence
@app.post("/summarize/")
async def summarize(text: str):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}

# Interface Gradio
def gradio_interface(input_text):
    result = summarize(input_text)
    return result["summary"]

# Lancer Gradio
iface = gr.Interface(fn=gradio_interface, inputs="text", outputs="text")
iface.launch(share=True)  # Mettre share=True pour partager l'interface en ligne
