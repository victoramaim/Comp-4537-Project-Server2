import sys
from transformers import AutoTokenizer, AutoModelForCausalLM


def generate_story(user_prompt_text):
    # Path to the local folder containing the tokenizer and model files
    model_path = "./mpt-7b-storywriter"

    # Load tokenizer and model from local folder
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    # Tokenize input
    inputs = tokenizer(user_prompt_text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate story
    generated_story_output = model.generate(**inputs, max_length=1000, num_return_sequences=1, temperature=0.7)
    generated_story_text = tokenizer.decode(generated_story_output[0], skip_special_tokens=True)

    return generated_story_text


if __name__ == "__main__":
    # Read input from stdin
    prompt_text = input("Enter prompt text: ").strip()  # Using input() for testing instead of sys.stdin.read()
    generated_story = generate_story(prompt_text)
    print("Generated Story:", generated_story)  # Output the generated story
