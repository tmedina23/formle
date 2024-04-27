from flask import Flask, render_template, Response, request, redirect, url_for
import random

all = []
with open('static/prompts2.txt') as f:
    [all.append(line.lower()) for line in f.readlines()]

app = Flask(__name__)

alpha = {
    "a": "\u2584",
    "b": "\u2588",
    "c": "\u2584",
    "d": "\u2588",
    "e": "\u2584",
    "f": "\u2588",
    "g": "_",
    "h": "\u2588",
    "i": "\u2588",
    "j": "_",
    "k": "\u2588",
    "l": "\u2588",
    "m": "\u2584",
    "n": "\u2584",
    "o": "\u2584",
    "p": "_",
    "q": "_",
    "r": "\u2584",
    "s": "\u2584",
    "t": "\u2588",
    "u": "\u2584",
    "v": "\u2584",
    "w": "\u2584",
    "x": "\u2584",
    "y": "_",
    "z": "\u2584"
}
#\u2584 low character
#\u2588 high character


@app.route('/', methods=['GET', 'POST'])
def index():
    skip_word = False
    global shapedWord
    global sentence
    shapedWord = ""
    sentence = random.choice(all).strip()
    for char in sentence:
        #if char is a letter and we are not skipping the word
        if char in alpha and skip_word == False:
            shapedWord += alpha[char]
        #if space, add space, and skip the next word
        elif char == " ":
            shapedWord += " "
            skip_word ^= True
        #if we are skipping the word, add the character as is
        else:
            shapedWord += char
    return render_template('index.html', result="", puzzle=shapedWord)

@app.route('/result', methods=['GET', 'POST'])
def result():
    guess = request.form['guess']
    if guess == sentence:
        print("Correct!")
        return render_template('index.html', result="Correct!", puzzle=sentence)
    else:
        return render_template('index.html', result="Incorrect, Try Again!", puzzle=shapedWord)
    
@app.route('/info', methods=['GET', 'POST'])
def info():
    return render_template('info.html')
    
#he quickly went to the store to grab some delicious milk

if __name__ == '__main__':
    app.run()