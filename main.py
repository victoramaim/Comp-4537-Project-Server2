from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("mosaicml/mpt-7b-storywriter", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("mosaicml/mpt-7b-storywriter", trust_remote_code=True)

# Prompt for text generation
prompt_text = "Once upon a time,"

# Encode the prompt text
input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

# Generate text based on the prompt
output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Story:")
print(generated_text)
