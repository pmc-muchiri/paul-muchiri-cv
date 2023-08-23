from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

# Parse the HTML content from the template file
with open('templates/main.html', 'r') as template_file:
    html_content = template_file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class "word"
words = soup.find_all(class_="word")

# Initialize currentWordIndex and maxWordIndex
currentWordIndex = 0
maxWordIndex = len(words) - 1

# Set the opacity of the initial word to 1 if currentWordIndex is within bounds
if 0 <= currentWordIndex < len(words):
    words[currentWordIndex]['style'] = 'opacity: 1;'

# Render the HTML template with the modified content
@app.route('/')
def index():
    return render_template('main.html', soup=soup, currentWordIndex=currentWordIndex, maxWordIndex=maxWordIndex)

if __name__ == "__main__":
    app.run(debug=True)
