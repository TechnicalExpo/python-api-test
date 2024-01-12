from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_google_suggestions(query):
    base_url = "https://www.google.com/complete/search"
    params = {
        "q": query,
        "output": "toolbar",
        "hl": "en",  # Set the desired language
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract suggestions from the response
    suggestions = [item.get('data') for item in soup.find_all('suggestion')]

    return suggestions

@app.route('/get_suggestions', methods=['GET'])
def get_suggestions():
    query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    suggestions = get_google_suggestions(query)
    
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
