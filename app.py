# libraries
import numpy as np
from flask import Flask, render_template, request ,jsonify

from LLM_ import *
from Chatbot import *

Our_Context = JSON_Context()
Our_Context.load_context('data.json')


model = TinyLama()

print("==============================================================================")

model.Start_model("/home/amogh/luna-ai-llama2-uncensored.Q5_0.gguf")

app = Flask(__name__)
# run_with_ngrok(app) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    res = CreatePrompt(model,Our_Context,msg)
    

    return {'msg': res}


if __name__ == "__main__":
    app.run(debug=True)

