from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def generate_story(prompt_text):
    tokenizer = AutoTokenizer.from_pretrained("mosaicml/mpt-7b-storywriter")
    model = AutoModelForCausalLM.from_pretrained("mosaicml/mpt-7b-storywriter")

    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

    output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

if __name__ == "__main__":
    prompt_text = "Once upon a time,"
    generated_story = generate_story(prompt_text)
    print("Generated Story:")
    print(generated_story)