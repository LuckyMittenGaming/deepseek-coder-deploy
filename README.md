---
title: DeepSeek-Coder
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: web_ui.py  # or app.py if you renamed it
pinned: false
tags:
  - gradio
  - deepseek-coder
  - coding-ai
  - transformers
---

# DeepSeek-Coder 1.3B Interface

A Gradio web interface for the DeepSeek-Coder 1.3B AI model.

## Features
- 🖥️ Code generation in multiple languages
- ⚡ Optimized for CPU/GPU
- 🔄 Auto-sync with GitHub

## Usage
```python
def generate_code(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
