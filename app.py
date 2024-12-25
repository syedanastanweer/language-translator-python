from flask import Flask, render_template, request
from googletrans import Translator
from langdetect import detect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    detected_language = ''
    translated_text = ''
    
    if request.method == "POST":
        input_text = request.form['input_text']  # The text input from the user
        target_lang = request.form['target_lang']  # The selected target language
        
        # Detecting language using langdetect
        detected_language = detect(input_text)
        
        # Translating the text
        translator = Translator()
        translated_text = translator.translate(input_text, src=detected_language, dest=target_lang).text
    
    # Render index.html with the results
    return render_template('index.html', detected_language=detected_language, translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True)
