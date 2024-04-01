# # main.py
# # # Example of usage
# from transformers import pipeline

# story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")
# # supported genres: superhero, action, drama, horror, thriller, sci_fi
# print(story_gen("<BOS> <action> Victor is a student."))

# # GPT - attempt 2
# from flask import Flask, render_template, request, jsonify
# from transformers import pipeline

# app = Flask(__name__)
# story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate_story():
#     user_input = request.form.get('user_input', '')  # Use request.form.get() to avoid KeyError
#     if not user_input:
#         return jsonify({'error': 'No input provided'})

#     generated_story = story_gen(f"<BOS> {user_input}")
#     return jsonify({'user_input': user_input, 'generated_story': generated_story[0]['generated_text']})

# if __name__ == '__main__':
#     app.run(debug=True)

# GPT - attempt 3
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
story_gen = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    user_input = request.form.get('user_input', '')  # Use request.form.get() to avoid KeyError
    genre = request.form.get('genre', 'superhero')  # Default to superhero if genre is not provided
    if not user_input:
        return jsonify({'error': 'No input provided'})

    generated_story = story_gen(f"<BOS> <{genre}> {user_input}")
    return jsonify({'user_input': user_input, 'generated_story': generated_story[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
