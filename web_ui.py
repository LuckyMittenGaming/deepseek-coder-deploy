%%writefile web_ui.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr

model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct")

def generate_code(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

gr.Interface(
    fn=generate_code,
    inputs="text",
    outputs="text",
    title="DeepSeek Coder 1.3B"
).launch()