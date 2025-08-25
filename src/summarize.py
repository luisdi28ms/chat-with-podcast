from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

with open("files/output/VMP7679265734.txt","r") as text_file:
    transcript = text_file.read()

input_text = "summarize: " + transcript
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids)
summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(summary)
