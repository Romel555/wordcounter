from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def count_words():
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(text.split())
        return render_template('word_counter.html', text=text, word_count=word_count)

if __name__ == "__main__":
    app.run(debug=True)
