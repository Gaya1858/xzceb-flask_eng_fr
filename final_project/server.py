from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text = machinetranslation.translator.englishtofrench(textToTranslate)
    return text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text = machinetranslation.translator.frenchtoenglish(textToTranslate)
    return text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
