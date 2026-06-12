# 🤖 Fine-Tuned NLP Model

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-green.svg)](https://huggingface.co/)

A fine-tuned natural language processing model stored in the `finished_triage_model/` directory.

## 📁 Model Files

The model consists of the following files in the `finished_triage_model/` directory:

- `config.json`: Model configuration file
- `model.safetensors`: Model weights in safe tensors format
- `special_tokens_map.json`: Special tokens mapping
- `tokenizer_config.json`: Tokenizer configuration
- `tokenizer.json`: Tokenizer data
- `vocab.txt`: Vocabulary file

## 🚀 Usage

To use this model, load with the Hugging Face Transformers library:

```python
from transformers import AutoTokenizer, AutoModel

model_path = "finished_triage_model/"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)

# Example: Tokenize text
inputs = tokenizer("Your input text here", return_tensors="pt")
outputs = model(**inputs)
```

## 📋 Notes

- This is a fine-tuned transformer-based NLP model
- Compatible with Hugging Face Transformers library
- Model weights are stored in the safe tensors format for security
