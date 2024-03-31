# main.py - Hugging Face Transformers example
# Example of usage
from transformers import pipeline

story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")
# supported genres: superhero, action, drama, horror, thriller, sci_fi
print(story_gen("<BOS> <action> Victor is a student."))

# # main.py - GPT attempt

# from flask import Flask, request, jsonify
# from transformers import pipeline

# app = Flask(__name__)

# @app.route('/generate_story', methods=['POST'])
# def generate_story():
#     data = request.get_json()
#     prompt = data['prompt']
#     story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")
#     story = story_gen(prompt)
#     return jsonify({"story": story})

# if __name__ == '__main__':
#     app.run(debug=True)
