from flask import Flask, render_template, request, redirect, url_for, session
from .models import Resume
from .parser import Parser

# Generate and add secret key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['GET', 'POST'])
def home():

    # Get all available tags from master
    master = Resume.parse_file('db/master.json')
    all_tags = master.get_tags()

    # Get selected tags from session
    selected_tags = set(session.get('selected_tags', []))

    # Get available tags
    available_tags = all_tags - selected_tags

    if request.method == 'POST':
        # Get raw-text and parse it
        raw_text = request.form['raw-text']
        selected_tags = Parser.from_text(raw_text)
        print(selected_tags)

        # Save selected tags in session
        session['selected_tags'] = list(selected_tags & all_tags)
        print(session['selected_tags'])

        return redirect(url_for('home'))

    return render_template('home.html', available_tags=list(available_tags), selected_tags=list(selected_tags))