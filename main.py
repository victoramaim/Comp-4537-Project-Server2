import sys
from transformers import AutoTokenizer, AutoModelForCausalLM


def generate_story(prompt_text):
    model_path = "./mpt-7b-storywriter"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, low_cpu_mem_usage=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, low_cpu_mem_usage=True)

    # Tokenize input
    inputs = tokenizer.encode(prompt_text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate story
    output = model.generate(inputs, max_length=1000, num_return_sequences=1, temperature=0.7)
    generated_story = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_story

if __name__ == "__main__":
    # Read input from stdin
    prompt_text = sys.stdin.read().strip()
    generated_story = generate_story(prompt_text)
    print(generated_story)  # Output the generated story
