import gradio as gr
import requests

def summarize(text):
    response = requests.post("http://inference:8000/summarize/", json={"text": text})
    return response.json()["summary"]

# Interface Gradio
iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch()
