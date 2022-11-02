from machinetranslation import translator
from flask import Flask, render_template, request
import json
#import machinetranslation.translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.args.get('textToTranslate')
    # Write your code here
    french_text= translator.english_to_french(english_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.args.get('textToTranslate')
    # Write your code here
    english_text= translator.french_to_english(english_text)
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
